# -----------------------------------------------------
# services/modal_services/location_summary.py
# Location Executive Summary Generator
# -----------------------------------------------------

import pandas as pd


def location_summary(df, location):
    """
    Generate executive insights for the selected location.
    """

    # =====================================================
    # Filter Location
    # =====================================================

    location_df = df[df["Location"] == location].copy()

    # =====================================================
    # Revenue
    # =====================================================

    total_revenue = location_df["TotalRevenue"].sum()

    company_revenue = df["TotalRevenue"].sum()

    contribution = (

        total_revenue /

        company_revenue *

        100

    )

    # =====================================================
    # Customers
    # =====================================================

    customer_count = (

        location_df["Customer"]

        .nunique()

    )

    top_customer = (

        location_df

        .groupby("Customer")["TotalRevenue"]

        .sum()

        .idxmax()

    )

    top_customer_revenue = (

        location_df

        .groupby("Customer")["TotalRevenue"]

        .sum()

        .max()

    )

    # =====================================================
    # Business Type
    # =====================================================

    business = (

        location_df

        .groupby("BusinessType")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

    )

    top_business = business.index[0]

    business_share = (

        business.iloc[0] /

        business.sum() *

        100

    )

    # =====================================================
    # Orders
    # =====================================================

    total_orders = (

        location_df["OrderCount"]

        .sum()

    )

    total_pieces = (

        location_df["NumberOfPieces"]

        .sum()

    )

    avg_revenue = (

        total_revenue /

        total_orders

        if total_orders

        else 0

    )

    # =====================================================
    # Trend
    # =====================================================

    temp = location_df.copy()

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
    # Executive Summary
    # =====================================================

    return [

        f"{location} generated ${total_revenue:,.0f} in revenue.",

        f"It contributes {contribution:.2f}% of total company revenue.",

        f"{customer_count:,} unique customers were served from this location.",

        f"The highest revenue customer is {top_customer} (${top_customer_revenue:,.0f}).",

        f"{top_business} contributes {business_share:.2f}% of this location's revenue.",

        f"{total_orders:,} orders resulted in {total_pieces:,} shipped pieces.",

        f"Average revenue per order is ${avg_revenue:,.2f}.",

        f"The recent monthly revenue trend is {trend}.",

        "Recommendation: Increase logistics capacity and inventory allocation during high-demand periods.",

    ]