import pandas as pd
from datetime import datetime


def export_data(jobs):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    dataframe = pd.DataFrame(jobs)

    excel_file = (
        f"output/jobs_{timestamp}.xlsx"
    )

    csv_file = (
        f"output/jobs_{timestamp}.csv"
    )

    dataframe.to_excel(
        excel_file,
        index=False
    )

    dataframe.to_csv(
        csv_file,
        index=False
    )

    return excel_file, csv_file