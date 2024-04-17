import os

from pr_pilot.util import create_task, wait_for_result

# Assuming GitHub Actions sets an environment variable for the commit message
# If not, this approach needs to be adjusted accordingly
commit_message = os.getenv("COMMIT_MESSAGE")
trigger_keyword = os.getenv("TRIGGER_KEYWORD")
repo = os.getenv("GITHUB_REPOSITORY")

if trigger_keyword and trigger_keyword not in commit_message:
    print(f"Commit message does not contain the trigger keyword '{trigger_keyword}'. Skipping task creation.")
else:
    prompt = f"""
    A commit has been made to the repository. Perform the following task based on the latest commit:
    {commit_message}
    """
    print(prompt)
    print(wait_for_result(create_task(repo, prompt)))
