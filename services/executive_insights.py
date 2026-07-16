# -----------------------------------------------------
# services/executive_insights.py
# Executive Business Insights Service
# -----------------------------------------------------

import pandas as pd


class ExecutiveInsights:
    """
    Computes executive-level business insights
    for the dashboard.
    """

    @staticmethod
    def generate(df):
        """
        Generate all executive insights.

        Returns
        -------
        dict
        """

        if df is None or df.empty:
            return {}

        data = df.copy()

        # ------------------------------------------
        # Convert Date
        # ------------------------------------------

        data["WorkDate"] = pd.to_datetime(
            data["WorkDate"],
            dayfirst=True,
            errors="coerce",
        )

        data = data.dropna(subset=["WorkDate"])

        # ------------------------------------------
        # Revenue Metrics
        # ------------------------------------------

        total_revenue = data["TotalRevenue"].sum()

        total_orders = data["OrderCount"].sum()

        total_pieces = data["NumberOfPieces"].sum()

        avg_revenue_order = (
            total_revenue / total_orders
            if total_orders
            else 0
        )

        avg_pieces_order = (
            total_pieces / total_orders
            if total_orders
            else 0
        )

        # ------------------------------------------
        # Customer
        # ------------------------------------------

        customer = (
            data.groupby("Customer")["TotalRevenue"]
            .sum()
            .sort_values(ascending=False)
        )

        top_customer = customer.index[0]

        top_customer_revenue = customer.iloc[0]

        # ------------------------------------------
        # Location
        # ------------------------------------------

        location = (
            data.groupby("Location")["TotalRevenue"]
            .sum()
            .sort_values(ascending=False)
        )

        top_location = location.index[0]

        top_location_revenue = location.iloc[0]

        # ------------------------------------------
        # Business Type
        # ------------------------------------------

        business = (
            data.groupby("BusinessType")["TotalRevenue"]
            .sum()
            .sort_values(ascending=False)
        )

        top_business_type = business.index[0]

        top_business_revenue = business.iloc[0]

        # ------------------------------------------
        # Monthly Revenue
        # ------------------------------------------

        monthly = (
            data.groupby(
                pd.Grouper(
                    key="WorkDate",
                    freq="ME",
                )
            )["TotalRevenue"]
            .sum()
        )

        highest_month = monthly.idxmax()

        highest_month_revenue = monthly.max()

        lowest_month = monthly.idxmin()

        lowest_month_revenue = monthly.min()

        # ------------------------------------------
        # Dataset Statistics
        # ------------------------------------------

        total_customers = data["Customer"].nunique()

        total_locations = data["Location"].nunique()

        total_business_types = (
            data["BusinessType"].nunique()
        )

        # ------------------------------------------
        # Return
        # ------------------------------------------

        return {

            "total_revenue": total_revenue,

            "total_orders": total_orders,

            "total_pieces": total_pieces,

            "avg_revenue_per_order":
                avg_revenue_order,

            "avg_pieces_per_order":
                avg_pieces_order,

            "top_customer":
                top_customer,

            "top_customer_revenue":
                top_customer_revenue,

            "top_location":
                top_location,

            "top_location_revenue":
                top_location_revenue,

            "top_business_type":
                top_business_type,

            "top_business_revenue":
                top_business_revenue,

            "highest_revenue_month":
                highest_month.strftime("%B %Y"),

            "highest_revenue":
                highest_month_revenue,

            "lowest_revenue_month":
                lowest_month.strftime("%B %Y"),

            "lowest_revenue":
                lowest_month_revenue,

            "total_customers":
                total_customers,

            "total_locations":
                total_locations,

            "total_business_types":
                total_business_types,

        }