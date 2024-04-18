import os

from pr_pilot.util import create_task, wait_for_result

pr_number = os.getenv("PR_NUMBER")
review_instructions = os.getenv("REVIEW_INSTRUCTIONS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The following PR was created: #{pr_number}

Read the PR, then review it according to the following instructions:
{review_instructions}
"""
print(prompt)
print(wait_for_result(create_task(repo, prompt, pr_number=pr_number)))