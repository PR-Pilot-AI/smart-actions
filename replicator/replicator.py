import os

from pr_pilot.util import create_task, wait_for_result

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
print(wait_for_result(create_task(repo, prompt)))