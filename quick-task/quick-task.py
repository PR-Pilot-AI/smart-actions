import os

from pr_pilot.util import create_task, wait_for_result

repo = os.getenv("GITHUB_REPOSITORY")
task_description = os.getenv("TASK_DESCRIPTION")

print(task_description)
print(wait_for_result(create_task(repo, task_description)))
