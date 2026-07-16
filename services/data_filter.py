# -----------------------------------------------------
# services/data_filter.py
# Dashboard Data Filtering Service
# -----------------------------------------------------

import pandas as pd


def filter_dataframe(
    df,
    customers=None,
    locations=None,
    business_types=None,
    start_date=None,
    end_date=None,
):
    """
    Filter dashboard dataframe based on user selections.
    """

    if df is None or df.empty:
        return df

    data = df.copy()

    # ==============================================
    # Ensure WorkDate is datetime
    # ==============================================

    if not pd.api.types.is_datetime64_any_dtype(data["WorkDate"]):
        data["WorkDate"] = pd.to_datetime(
            data["WorkDate"],
            dayfirst=True,
            errors="coerce",
        )

    # ==============================================
    # Date Filter
    # ==============================================

    if start_date is not None:
        data = data[
            data["WorkDate"] >= pd.to_datetime(start_date)
        ]

    if end_date is not None:
        data = data[
            data["WorkDate"] <= pd.to_datetime(end_date)
        ]

    # ==============================================
    # Customer Filter
    # ==============================================

    if customers:
        data = data[
            data["Customer"].isin(customers)
        ]

    # ==============================================
    # Location Filter
    # ==============================================

    if locations:
        data = data[
            data["Location"].isin(locations)
        ]

    # ==============================================
    # Business Type Filter
    # ==============================================

    if business_types:
        data = data[
            data["BusinessType"].isin(
                business_types
            )
        ]

    return data