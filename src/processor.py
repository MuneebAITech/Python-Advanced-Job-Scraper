def filter_jobs(jobs, keywords):

    filtered_jobs = []

    for job in jobs:

        title = job["title"].lower()

        for keyword in keywords:

            if keyword.lower() in title:

                filtered_jobs.append(job)

                break

    return filtered_jobs


def remove_duplicates(jobs):

    unique_jobs = []
    seen = set()

    for job in jobs:

        key = (
            job["title"],
            job["company"],
            job["location"]
        )

        if key not in seen:

            seen.add(key)

            unique_jobs.append(job)

    return unique_jobs

def generate_statistics(
    original_jobs,
    filtered_jobs,
    final_jobs
):

    return {
        "original_jobs": original_jobs,
        "filtered_jobs": filtered_jobs,
        "duplicates_removed":
            filtered_jobs - final_jobs,
        "final_jobs": final_jobs
    }