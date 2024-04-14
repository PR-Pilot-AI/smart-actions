import os

from pr_pilot.util import create_task

task_description = os.getenv("TASK_DESCRIPTION")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
A commit has been made to the repository. Perform the following task based on the latest commit:
{task_description}
"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"Task to monitor the commit will be executed soon, monitor the task here: {dashboard_url}")