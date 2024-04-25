# Quick-Task Action

The `quick-task` action that allows you to directly issue tasks to PR Pilot.

## Workflow Ideas

- **Execute Simple Tasks** Use a task description to run small tasks instantly.
- **Generate new Issues** Let the bot open a new issue based on your instructions
- **Answer a Question** Have a question about your code? Let PR Pilot look at the code and answer it for you

## Usage

To use the `quick-task` action in your project, you'll need to include it in your GitHub workflow files. Define the task you wish to execute directly in your commit messages or issue comments.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.3.2`.
- `api-key`: (Required) Your API key for PR Pilot.
- `agent-instructions`: (Required) The description of the task to run.

### Example Workflow

```yaml
name: Execute Quick Task

on:
  workflow_dispatch:
    inputs:
      agent-instructions:
        description: 'What should PR Pilot do for you?'
        required: true

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
          agent-instructions: ${{ github.event.inputs.agent-instructions }}
```
