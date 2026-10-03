import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from config import BASE_URL
from logger import log_success, log_failed
from scraper import scrape_jobs
from config import BASE_URL, KEYWORDS
from processor import filter_jobs, remove_duplicates
from exporter import export_data
from processor import (
    filter_jobs,
    remove_duplicates,
    generate_statistics
)
from reporter import generate_report



print("Advanced Job Scraper Started")
print(f"Website: {BASE_URL}")

try:

    jobs = scrape_jobs(BASE_URL)

    print(f"\nOriginal Jobs: {len(jobs)}")

    original_count = len(jobs)

    jobs = filter_jobs(
        jobs,
        KEYWORDS
    )

    filtered_count = len(jobs)

    print(
        f"After Keyword Filter: {len(jobs)}"
    )

    jobs = remove_duplicates(
        jobs
    )

    final_count = len(jobs)

    print(
        f"After Duplicate Removal: {len(jobs)}"
    )

    print("\nSample Results:\n")

    for job in jobs[:5]:

        print(
            f"{job['title']} | "
            f"{job['company']} | "
            f"{job['location']}"
        )

        print(
            f"Apply: {job['apply_link']}"
        )

        print("-" * 80)


    excel_file, csv_file = export_data(
        jobs
    )

    print(
        f"\nExcel File Saved: {excel_file}"
    )

    print(
        f"CSV File Saved: {csv_file}"
    )

    stats = generate_statistics(
    original_count,
    filtered_count,
    final_count
    )

    report_file = generate_report(
        stats,
        excel_file,
        csv_file
    )

    print(
        f"\nReport Saved: {report_file}"
    )

    print("\n")
    print("=" * 40)
    print("SCRAPING SUMMARY")
    print("=" * 40)

    print(
        f"Original Jobs: "
        f"{stats['original_jobs']}"
    )

    print(
        f"Filtered Jobs: "
        f"{stats['filtered_jobs']}"
    )

    print(
        f"Duplicates Removed: "
        f"{stats['duplicates_removed']}"
    )

    print(
        f"Final Jobs: "
        f"{stats['final_jobs']}"
    )

    print("=" * 40)

    log_success(
        f"{len(jobs)} jobs processed successfully"
    )

except Exception as error:

    log_failed(str(error))

    print(error)

