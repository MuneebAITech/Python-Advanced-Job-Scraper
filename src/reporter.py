from datetime import datetime


def generate_report(
    stats,
    excel_file,
    csv_file
):

    report_file = "logs/report.txt"

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "ADVANCED JOB SCRAPER REPORT\n"
        )

        file.write(
            "=" * 40 + "\n"
        )

        file.write(
            f"Generated: {datetime.now()}\n\n"
        )

        file.write(
            f"Original Jobs: {stats['original_jobs']}\n"
        )

        file.write(
            f"Filtered Jobs: {stats['filtered_jobs']}\n"
        )

        file.write(
            f"Duplicates Removed: {stats['duplicates_removed']}\n"
        )

        file.write(
            f"Final Jobs: {stats['final_jobs']}\n\n"
        )

        file.write(
            f"Excel File: {excel_file}\n"
        )

        file.write(
            f"CSV File: {csv_file}\n"
        )

    return report_file