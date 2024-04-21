import os

from pr_pilot.util import create_task, wait_for_result, comment_on_issue

issue_number = os.getenv("ISSUE_NUMBER")
response_template = os.getenv("RESPONSE_TEMPLATE")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
Read the following issue: #{issue_number}

Based on the issue content, take any necessary action and prepare a response using the template:
{response_template}
"""
print(prompt)

# Assuming the action taken can be simulated or is not required for this script.
# The focus is on generating a response and commenting on the issue.

comment = wait_for_result(create_task(repo, prompt, issue_number=issue_number))
comment_on_issue(repo, issue_number, comment)
