# Quick-Task Action

The `quick-task` action is designed to execute tasks described directly in your commit messages or through issue comments. Simply include a task description, and the action will run it as specified.

## Workflow Ideas

- **Execute Simple Tasks** Use a task description to run small, predefined tasks automatically.
- **Run Scripts** Commit or comment with a task to run specific scripts in your repository.
- **Automate Responses** Use task descriptions to automate responses to common repository events.

## Usage

To use the `quick-task` action in your project, you'll need to include it in your GitHub workflow files. Define the task you wish to execute directly in your commit messages or issue comments.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.2.0`.
- `api-key`: (Required) Your API key for PR Pilot.
- `task-description`: (Required) The description of the task to run.

### Example Workflow

```yaml
name: Execute Quick Task

on: workflow_dispatch

jobs:
  run-quick-task:
    runs-on: ubuntu-latest
    steps:
      - name: Run Task
        uses: PR-Pilot-AI/smart-actions/quick-task@v1
        with:
          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          # Description of the task to execute
          task-description: "Automatically respond to issue"
```