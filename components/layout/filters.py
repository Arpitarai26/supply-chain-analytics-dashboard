# -----------------------------------------------------
# components/layout/filters.py
# Dashboard Filters
# -----------------------------------------------------

from dash import html, dcc


def filters(df):
    """
    Dashboard filter section.
    """

    return html.Div(

        [

            html.Div(

                [

                    # ======================================
                    # Theme
                    # ======================================

                    html.Div(

                        [

                            html.Label(
                                "Theme",
                                className="filter-label",
                            ),

                            dcc.RadioItems(

                                id="theme-toggle",

                                options=[
                                    {
                                        "label": "🌙 Dark",
                                        "value": "dark",
                                    },
                                    {
                                        "label": "☀️ Light",
                                        "value": "light",
                                    },
                                ],

                                value="dark",

                                inline=True,

                            ),

                        ],

                        className="filter-item",

                    ),

                    # ======================================
                    # Date Range
                    # ======================================

                    html.Div(

                        [

                            html.Label(
                                "Date Range",
                                className="filter-label",
                            ),

                            dcc.DatePickerRange(

                                id="date-range",

                                min_date_allowed=df["WorkDate"].min(),

                                max_date_allowed=df["WorkDate"].max(),

                                start_date=df["WorkDate"].min(),

                                end_date=df["WorkDate"].max(),

                                display_format="DD-MM-YYYY",

                            ),

                        ],

                        className="filter-item",

                    ),

                    # ======================================
                    # Customer
                    # ======================================

                    html.Div(

                        [

                            html.Label(
                                "Customer",
                                className="filter-label",
                            ),

                            dcc.Dropdown(

                                id="customer-dropdown",

                                options=[
                                    {
                                        "label": c,
                                        "value": c,
                                    }
                                    for c in sorted(
                                        df["Customer"].unique()
                                    )
                                ],

                                multi=True,

                                placeholder="All Customers",

                            ),

                        ],

                        className="filter-item",

                    ),

                    # ======================================
                    # Location
                    # ======================================

                    html.Div(

                        [

                            html.Label(
                                "Location",
                                className="filter-label",
                            ),

                            dcc.Dropdown(

                                id="location-dropdown",

                                options=[
                                    {
                                        "label": c,
                                        "value": c,
                                    }
                                    for c in sorted(
                                        df["Location"].unique()
                                    )
                                ],

                                multi=True,

                                placeholder="All Locations",

                            ),

                        ],

                        className="filter-item",

                    ),

                    # ======================================
                    # Business Type
                    # ======================================

                    html.Div(

                        [

                            html.Label(
                                "Business Type",
                                className="filter-label",
                            ),

                            dcc.Dropdown(

                                id="business-dropdown",

                                options=[
                                    {
                                        "label": c,
                                        "value": c,
                                    }
                                    for c in sorted(
                                        df["BusinessType"].unique()
                                    )
                                ],

                                multi=True,

                                placeholder="All Business Types",

                            ),

                        ],

                        className="filter-item",

                    ),

                    # ======================================
                    # Reset
                    # ======================================

                    html.Div(

                        [

                            html.Button(

                                "Reset Filters",

                                id="reset-button",

                                n_clicks=0,

                                className="reset-button",

                            ),

                        ],

                        className="filter-item",

                    ),

                ],

                className="filters-grid",

            ),

        ],

        className="filters-container",

    )