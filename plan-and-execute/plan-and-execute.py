import os

from pr_pilot.util import create_task, wait_for_result

repo = os.getenv("GITHUB_REPOSITORY")
task_description = os.getenv("TASK_DESCRIPTION")
expected_result = os.getenv("EXPECTED_RESULT")

prompt = f"""
We want to create a plan to achieve the following:

```
{task_description}
```

The expected result is:
```
{expected_result}
```

Your plan MUST only include actions that use the following capabilities:
- Searching the code base
- CRUD operations on files
- Reading, editing and creating Github issues
- Searching the internet for information

Create an actionable, step-by-step plan to achieve the expected result.
"""
plan = wait_for_result(create_task(repo, prompt))
print(f"Plan created: \n\n{plan}\n\nExecuting plan...")

prompt = f"""
The user wants you to fulfill the following task:

```
{task_description}
```

The expected result is:
```
{expected_result}
```

Use the following plan to achieve the expected result:

```
{plan}
```
"""

execution_result = wait_for_result(create_task(repo, plan))
