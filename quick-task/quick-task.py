import os

from pr_pilot.util import create_task, wait_for_result

repo = os.getenv("GITHUB_REPOSITORY")
agent_instructions = os.getenv("AGENT_INSTRUCTIONS")
pr_number = os.getenv("PR_NUMBER")

print(agent_instructions)
print(wait_for_result(create_task(repo, agent_instructions, pr_number=pr_number)))
