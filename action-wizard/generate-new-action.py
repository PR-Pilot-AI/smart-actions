import os

from pr_pilot.util import create_task

repo = os.getenv("GITHUB_REPOSITORY")
trigger = os.getenv("TRIGGER")
task_description = os.getenv("TASK_DESCRIPTION")

prompt = f"""
# Context
The user wants to create a new Smart Github Action.
A smart action is an action that is executed by a smart AI agent and has two components:

- Trigger: A natural language description of the event that should trigger the action.
- Task: What the AI agent should do when the trigger is detected.

Every smart action has two files:
- `<action-name>/<action-name>.py`: The code that executes the action
- `<action-name>/action.yaml`: The metadata that describes the action

# User Input
The user has provided the following information:

Trigger: 
`{trigger}`

Task Description:
```
{task_description}
```

# Your Job
Do the following:
1. Read an existing action and use it as a template for the new action: `format-issue/action.yaml` and `format-issue/format-issue.py`
2. Determine which input variables are needed for the new action
3. Based on the user input determine how the action should be triggered
4. Turn the user's task description into actionable, natural language instructions for the AI agent
5. Create the metadata file with a valid trigger and input variables
6. Create the code file with the AI agent instructions similar to the template
7. Create a new workflow that uses the action, use `.github/workflows/issue_formatter.yaml` as a template

# Additional Information
When translating the user's task description into instructions for the AI agent, the instructions should be clear and concise.
The AI agent is capable of:
- reading/writing files in the repository
- working with Github issues/PRs
- Searching for information on the internet

"""
print(prompt)

task = create_task(repo, prompt)
dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
print(f"A PR with the new action will be created soon. Monitor the task here: {dashboard_url}")