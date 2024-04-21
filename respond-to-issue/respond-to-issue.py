import os

from pr_pilot.util import create_task, wait_for_result

issue_number = os.getenv("ISSUE_NUMBER")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
Read the following issue: #{issue_number}

Based on the issue content, take any necessary action and add a comment to the issue with your response.
"""
print(prompt)
print(wait_for_result(create_task(repo, prompt, issue_number=issue_number)))
