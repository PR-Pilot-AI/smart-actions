# Quick-Task Action

The `quick-task` action is designed to streamline your workflow by allowing you to define tasks directly from your GitHub actions. This action takes a task description as input and uses it to create a new PR Pilot task automatically.

## Workflow Ideas

- **Automate Task Creation** Use this action to automatically create tasks based on specific triggers within your GitHub workflow.

## Usage

To use the `quick-task` action in your project, you'll need to include it in your GitHub workflow files. Define the task description you wish to automate and configure the action to create a new task when triggered.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.0.3`.
- `api-key`: (Required) Your API key for PR Pilot.
- `task-description`: (Required) The description of the task to create.

### Example Workflow

```yaml
name: Create a quick task

on:
  push:

jobs:
  create-task:
    runs-on: ubuntu-latest
    steps:
      - name: Quick Task
        uses: PR-Pilot-AI/smart-actions/quick-task@v1
        with:
          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          # Description of the task to be created
          task-description: "Update documentation"
```