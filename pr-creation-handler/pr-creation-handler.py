import os

from pr_pilot.util import create_task

pr_number = os.getenv("PR_NUMBER")
review_instructions = os.getenv("REVIEW_INSTRUCTIONS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The following PR was created: #{pr_number}

Read the PR, then review it according to the following instructions:
{review_instructions}
"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"PR #{pr_number} will be handled soon, monitor the task here: {dashboard_url}")