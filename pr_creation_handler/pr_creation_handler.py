import os

from pr_pilot.util import create_task

pr_number = os.getenv("PR_NUMBER")
task_instructions = os.getenv("TASK_INSTRUCTIONS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The following PR was created: #{pr_number}

Read the PR, then perform the following tasks:
{task_instructions}
"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"PR #{pr_number} will be handled soon, monitor the task here: {dashboard_url}")