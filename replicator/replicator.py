import os

from pr_pilot.util import create_task

template = os.getenv("TEMPLATE")
characteristics = os.getenv("CHARACTERISTICS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The user wants you to take existing file/code/text and replicate it with different characteristics.

What to replicate:
```
{template}
```

Read and understand it, then replicate it with the following characteristics:
```
{characteristics}
```

"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"Replicator is running, monitor the task here: {dashboard_url}")
print(f"::set-output name=task-link::{dashboard_url}")