# -----------------------------------------------------
# services/modal_services/simple_modals.py
# Simple Analytics Modals
# -----------------------------------------------------

from dash import html
import pandas as pd


# =====================================================
# KPI Card
# =====================================================

def metric(title, value):

    return html.Div(

        [

            html.H4(title),

            html.H2(value),

        ],

        className="modal-card",

    )


# =====================================================
# Highest Revenue Month
# =====================================================

def highest_month_modal(df):

    temp = df.copy()

    temp["WorkDate"] = pd.to_datetime(
        temp["WorkDate"],
        dayfirst=True,
    )

    monthly = (

        temp.groupby(
            temp["WorkDate"].dt.to_period("M")
        )["TotalRevenue"]

        .sum()

    )

    month = monthly.idxmax()

    revenue = monthly.max()

    month_df = temp[
        temp["WorkDate"].dt.to_period("M") == month
    ]

    orders = month_df["OrderCount"].sum()

    pieces = month_df["NumberOfPieces"].sum()

    contribution = (

        revenue /

        df["TotalRevenue"].sum()

        * 100

    )

    body = html.Div(

        [

            html.Div(

                [

                    metric("Month", month.strftime("%B %Y")),

                    metric("Revenue", f"${revenue:,.2f}"),

                    metric("Orders", f"{orders:,}"),

                    metric("Pieces", f"{pieces:,}"),

                    metric("Revenue Share", f"{contribution:.2f}%"),

                ],

                className="modal-grid",

            ),

            html.H2(
                "Executive Insight",
                className="modal-heading",
            ),

            html.P(

                f"{month.strftime('%B %Y')} generated the highest "
                f"revenue in the dataset with "
                f"${revenue:,.0f}. High shipment volume and strong "
                f"customer demand contributed to this performance.",

                className="modal-summary",

            ),

            html.H2(
                "Recommendations",
                className="modal-heading",
            ),

            html.Ul(

                [

                    html.Li("Analyze demand patterns during this month."),

                    html.Li("Prepare inventory before similar peak periods."),

                    html.Li("Increase workforce during high-demand months."),

                ],

                className="summary-list",

            ),

        ]

    )

    return "📈 Highest Revenue Month", body


# =====================================================
# Lowest Revenue Month
# =====================================================

def lowest_month_modal(df):

    temp = df.copy()

    temp["WorkDate"] = pd.to_datetime(
        temp["WorkDate"],
        dayfirst=True,
    )

    monthly = (

        temp.groupby(
            temp["WorkDate"].dt.to_period("M")
        )["TotalRevenue"]

        .sum()

    )

    month = monthly.idxmin()

    revenue = monthly.min()

    month_df = temp[
        temp["WorkDate"].dt.to_period("M") == month
    ]

    orders = month_df["OrderCount"].sum()

    pieces = month_df["NumberOfPieces"].sum()

    body = html.Div(

        [

            html.Div(

                [

                    metric("Month", month.strftime("%B %Y")),

                    metric("Revenue", f"${revenue:,.2f}"),

                    metric("Orders", f"{orders:,}"),

                    metric("Pieces", f"{pieces:,}"),

                ],

                className="modal-grid",

            ),

            html.H2(
                "Executive Insight",
                className="modal-heading",
            ),

            html.P(

                f"{month.strftime('%B %Y')} recorded the lowest "
                f"revenue in the dataset. Lower shipment volume and "
                f"reduced order activity affected business performance.",

                className="modal-summary",

            ),

            html.H2(
                "Recommendations",
                className="modal-heading",
            ),

            html.Ul(

                [

                    html.Li("Review seasonal demand fluctuations."),

                    html.Li("Improve customer acquisition strategies."),

                    html.Li("Optimize transportation costs."),

                ],

                className="summary-list",

            ),

        ]

    )

    return "📉 Lowest Revenue Month", body
# =====================================================
# Average Revenue Per Order
# =====================================================

def avg_revenue_modal(df):

    avg = df["TotalRevenue"].mean()

    median = df["TotalRevenue"].median()

    maximum = df["TotalRevenue"].max()

    minimum = df["TotalRevenue"].min()

    body = html.Div(

        [

            html.Div(

                [

                    metric("Average Revenue", f"${avg:,.2f}"),

                    metric("Median Revenue", f"${median:,.2f}"),

                    metric("Maximum Revenue", f"${maximum:,.2f}"),

                    metric("Minimum Revenue", f"${minimum:,.2f}"),

                ],

                className="modal-grid",

            ),

            html.H2(

                "Executive Insight",

                className="modal-heading",

            ),

            html.P(

                "Average revenue per order provides a useful indicator of "
                "overall business performance. Monitoring unusually large "
                "or small orders helps identify revenue opportunities and "
                "operational inefficiencies.",

                className="modal-summary",

            ),

            html.H2(

                "Recommendations",

                className="modal-heading",

            ),

            html.Ul(

                [

                    html.Li("Increase average order value through bundled services."),

                    html.Li("Focus on retaining high-value customers."),

                    html.Li("Investigate unusually low-value orders."),

                ],

                className="summary-list",

            ),

        ]

    )

    return "💰 Average Revenue Per Order", body


# =====================================================
# Average Pieces Per Order
# =====================================================

def avg_pieces_modal(df):

    avg = df["NumberOfPieces"].mean()

    maximum = df["NumberOfPieces"].max()

    minimum = df["NumberOfPieces"].min()

    total = df["NumberOfPieces"].sum()

    body = html.Div(

        [

            html.Div(

                [

                    metric("Average Pieces", f"{avg:.2f}"),

                    metric("Maximum Pieces", f"{maximum:,}"),

                    metric("Minimum Pieces", f"{minimum:,}"),

                    metric("Total Pieces", f"{total:,}"),

                ],

                className="modal-grid",

            ),

            html.H2(

                "Executive Insight",

                className="modal-heading",

            ),

            html.P(

                "Shipment size remains relatively stable across the dataset. "
                "Monitoring changes in average shipment size helps optimize "
                "warehouse capacity and transportation planning.",

                className="modal-summary",

            ),

            html.H2(

                "Recommendations",

                className="modal-heading",

            ),

            html.Ul(

                [

                    html.Li("Optimize truck utilization."),

                    html.Li("Reduce partially filled shipments."),

                    html.Li("Improve warehouse packing efficiency."),

                ],

                className="summary-list",

            ),

        ]

    )

    return "📦 Average Pieces Per Order", body


# =====================================================
# Dataset Summary
# =====================================================

def dataset_summary_modal(df):

    temp = df.copy()

    temp["WorkDate"] = pd.to_datetime(

        temp["WorkDate"],

        dayfirst=True,

    )

    start = temp["WorkDate"].min().strftime("%d %b %Y")

    end = temp["WorkDate"].max().strftime("%d %b %Y")

    body = html.Div(

        [

            html.Div(

                [

                    metric("Rows", f"{len(df):,}"),

                    metric("Customers", df["Customer"].nunique()),

                    metric("Locations", df["Location"].nunique()),

                    metric("Business Types", df["BusinessType"].nunique()),

                    metric("Date Range", f"{start}\n{end}"),

                ],

                className="modal-grid",

            ),

            html.H2(

                "Executive Insight",

                className="modal-heading",

            ),

            html.P(

                "This dataset contains historical supply chain transactions "
                "covering multiple customers, business types and locations. "
                "The available time span is sufficient for operational, "
                "financial and trend analysis.",

                className="modal-summary",

            ),

            html.H2(

                "Recommendations",

                className="modal-heading",

            ),

            html.Ul(

                [

                    html.Li("Continue collecting historical shipment data."),

                    html.Li("Track additional logistics KPIs such as delivery time."),

                    html.Li("Include profitability metrics in future releases."),

                ],

                className="summary-list",

            ),

        ]

    )

    return "📊 Dataset Summary", body