import os

from pr_pilot.util import create_task

template_path = os.getenv("TEMPLATE_PATH")
result_path = os.getenv("RESULT_PATH")
characteristics = os.getenv("CHARACTERISTICS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
Use the template at '{template_path}' to create a new file or code snippet. The new creation should be saved at '{result_path}' and must have the following characteristics:
{characteristics}
"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"New creation based on template will be processed soon, monitor the task here: {dashboard_url}")