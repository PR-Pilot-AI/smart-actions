import os

from pr_pilot.util import create_task, wait_for_result

repo = os.getenv("GITHUB_REPOSITORY")
agent_instructions = os.getenv("AGENT_INSTRUCTIONS")

print(agent_instructions)
print(wait_for_result(create_task(repo, agent_instructions)))
