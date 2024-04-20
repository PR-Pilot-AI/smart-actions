import os

from pr_pilot.util import create_task, wait_for_result

repo = os.getenv("GITHUB_REPOSITORY")
task_description = os.getenv("TASK_DESCRIPTION")
expected_result = os.getenv("EXPECTED_RESULT")
agent_hints = os.getenv("AGENT_HINTS")

prompt = f"""
We want to create a step-by-step plan for you to achieve the following:

```
{task_description}
```

The expected result is:
```
{expected_result}
```

The user gave you hints for creating the plan:
```
{agent_hints}
```

Make sure the plan is within your own abilities.
Create an actionable, step-by-step plan to achieve the expected result.
"""
plan = wait_for_result(create_task(repo, prompt))
print(f"Plan created: \n\n{plan}\n\nExecuting plan...")

prompt = f"""
We made a plan for you to achieve the following:

```
{task_description}
```

The expected result is:
```
{expected_result}
```

The user gave you hints for creating the plan:
```
{agent_hints}
```

Execute the following plan to achieve the expected result:

```
{plan}
```
"""

execution_result = wait_for_result(create_task(repo, plan))
