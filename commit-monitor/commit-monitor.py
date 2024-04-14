import os

from pr_pilot.util import create_task

# Assuming GitHub Actions sets an environment variable for the commit message
# If not, this approach needs to be adjusted accordingly
commit_message = os.getenv("GITHUB_COMMIT_MESSAGE")
trigger_keyword = os.getenv("INPUT_TRIGGER-KEYWORD")  # Environment variable for action input
repo = os.getenv("GITHUB_REPOSITORY")

if trigger_keyword and trigger_keyword not in commit_message:
    print(f"Commit message does not contain the trigger keyword '{trigger_keyword}'. Skipping task creation.")
else:
    prompt = f"""
    A commit has been made to the repository. Perform the following task based on the latest commit:
    {commit_message}
    """
    print(prompt)

    task = create_task(repo, prompt)
    dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
    print(f"Task to monitor the commit will be executed soon, monitor the task here: {dashboard_url}")
