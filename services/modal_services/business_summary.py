# -----------------------------------------------------
# services/modal_services/business_summary.py
# Business Executive Summary Generator
# -----------------------------------------------------

import pandas as pd


def business_summary(df, business):
    """
    Generate executive insights for the selected business type.
    """

    # =====================================================
    # Filter Dataset
    # =====================================================

    business_df = df[df["BusinessType"] == business].copy()

    # =====================================================
    # Revenue
    # =====================================================

    total_revenue = business_df["TotalRevenue"].sum()

    company_revenue = df["TotalRevenue"].sum()

    contribution = (
        (total_revenue / company_revenue) * 100
        if company_revenue
        else 0
    )

    # =====================================================
    # Customers
    # =====================================================

    customer_revenue = (
        business_df.groupby("Customer")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
    )

    top_customer = customer_revenue.index[0]
    top_customer_revenue = customer_revenue.iloc[0]

    customer_count = business_df["Customer"].nunique()

    # =====================================================
    # Locations
    # =====================================================

    location_revenue = (
        business_df.groupby("Location")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
    )

    top_location = location_revenue.index[0]
    top_location_revenue = location_revenue.iloc[0]

    location_count = business_df["Location"].nunique()

    # =====================================================
    # Orders
    # =====================================================

    total_orders = business_df["OrderCount"].sum()

    total_pieces = business_df["NumberOfPieces"].sum()

    avg_revenue = (
        total_revenue / total_orders
        if total_orders
        else 0
    )

    # =====================================================
    # Monthly Trend
    # =====================================================

    temp = business_df.copy()

    temp["WorkDate"] = pd.to_datetime(
        temp["WorkDate"],
        dayfirst=True,
        errors="coerce",
    )

    monthly = (
        temp.groupby(
            temp["WorkDate"].dt.to_period("M")
        )["TotalRevenue"]
        .sum()
    )

    trend = "stable"

    if len(monthly) >= 2:

        if monthly.iloc[-1] > monthly.iloc[-2]:
            trend = "increasing"

        elif monthly.iloc[-1] < monthly.iloc[-2]:
            trend = "decreasing"

    # =====================================================
    # Summary
    # =====================================================

    return [

        f"{business} generated ${total_revenue:,.0f} in total revenue.",

        f"It contributes {contribution:.2f}% of company revenue.",

        f"The leading customer is {top_customer} (${top_customer_revenue:,.0f}).",

        f"The strongest location is {top_location} (${top_location_revenue:,.0f}).",

        f"{customer_count:,} unique customers generated {total_orders:,} orders.",

        f"{location_count:,} locations participate in this business segment.",

        f"{total_pieces:,} pieces were shipped through this business type.",

        f"Average revenue per order is ${avg_revenue:,.2f}.",

        f"The recent monthly trend is {trend}.",

        "Recommendation: Focus investment on high-performing locations and strengthen relationships with top customers.",

    ]