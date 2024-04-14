# Quick-Task Action

The `quick-task` action is designed to enhance your workflow by allowing you to define a task description within your action configuration. When triggered, the action can automatically execute the task as specified.

## Workflow Ideas

- **Automate Tasks** Use the action to run predefined tasks quickly and efficiently.
- **Custom Scripts** Execute custom scripts based on the task description provided.

## Usage

To use the `quick-task` action in your project, you'll need to include it in your GitHub workflow files. Define the task you wish to automate and configure the action to execute it.

### Inputs

- `task-description`: (Required) The description of the task to run.

### Example Workflow

```yaml
name: Run Quick Task

on:
  workflow_dispatch:

jobs:
  quick-task:
    runs-on: ubuntu-latest
    steps:
      - name: Execute Task
        uses: PR-Pilot-AI/smart-actions/quick-task@v1
        with:
          # Description of the task to run
          task-description: "Automate build process"
```