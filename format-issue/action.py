import os

from pr_pilot.util import create_task

issue_number = os.getenv("ISSUE_NUMBER")
formatting_instructions = os.getenv("FORMATTING_INSTRUCTIONS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The following issue was opened: #{issue_number}

Read the issue, then edit it according to the following instructions:
{formatting_instructions}
"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"Issue #{issue_number} will be formatted soon, monitor the task here: {dashboard_url}")