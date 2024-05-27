# 3 Job sequencing

def job_sequencing(jobs):
    # Sort jobs by profit in descending order.
    sorted_jobs = sorted(jobs.items(), key=lambda x: x[0], reverse=True)

    # Initialize variables.
    max_profit = 0
    scheduled_jobs = [None] * max(jobs.values())

    # Iterate through sorted jobs.
    for profit, deadline in sorted_jobs:
        # Find a slot for the job.
        for i in range(min(deadline - 1, len(scheduled_jobs) - 1), -1, -1):
            if scheduled_jobs[i] is None:
                # Schedule the job and update max profit.
                scheduled_jobs[i] = profit
                max_profit += profit
                break

    # Filter out None values to get the scheduled job profits.
    scheduled_jobs = [job for job in scheduled_jobs if job is not None]

    return scheduled_jobs, max_profit


# Test the function.
jobs = {20: 2, 10: 3, 40: 2, 30: 1, 5: 1}
scheduled_jobs, max_profit = job_sequencing(jobs)

print("Scheduled jobs (profits):", scheduled_jobs)
print("Maximum profit:", max_profit)
