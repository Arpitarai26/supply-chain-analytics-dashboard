# -----------------------------------------------------
# services/modal_services/summary_generator.py
# Executive Summary Generator
# -----------------------------------------------------

import pandas as pd


def customer_summary(df, customer):

    subset = df[df["Customer"] == customer]

    revenue = subset["TotalRevenue"].sum()

    total = df["TotalRevenue"].sum()

    share = revenue / total * 100

    top_location = (

        subset.groupby("Location")["TotalRevenue"]

        .sum()

        .idxmax()

    )

    top_business = (

        subset.groupby("BusinessType")["TotalRevenue"]

        .sum()

        .idxmax()

    )

    orders = subset["OrderCount"].sum()

    pieces = subset["NumberOfPieces"].sum()

    return [

        f"{customer} generated ${revenue:,.0f} in total revenue.",

        f"It contributes {share:.2f}% of overall company revenue.",

        f"The strongest operating location is {top_location}.",

        f"{top_business} is the dominant business segment.",

        f"The customer placed {orders:,} orders involving {pieces:,} shipped pieces.",

        "Recommendation: Prioritize capacity planning for this customer during peak demand periods.",

    ]