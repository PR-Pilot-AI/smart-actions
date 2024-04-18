import os

from pr_pilot.util import create_task, wait_for_result

issue_number = os.getenv("ISSUE_NUMBER")
formatting_instructions = os.getenv("FORMATTING_INSTRUCTIONS")
repo = os.getenv("GITHUB_REPOSITORY")

prompt = f"""
The following issue was opened: #{issue_number}

Read the issue, then edit it according to the following instructions:
{formatting_instructions}
"""
print(prompt)

print(wait_for_result(create_task(repo, prompt, issue_number=issue_number)))