# Quick-Task Action

The `quick-task` action is designed to execute a simple task described directly in the action's inputs. This allows for a straightforward execution of tasks without the need for detecting specific keywords or commands within commit messages.

## Usage

To use the `quick-task` action in your project, you'll need to include it in your GitHub workflow files. Simply define the task you wish to run in the action's inputs.

### Inputs

- `task-description`: (Required) The description of the task to run as-is.

### Example Workflow

```yaml
name: Execute Quick Task

on:
  push:

jobs:
  run-quick-task:
    runs-on: ubuntu-latest
    steps:
      - name: Run Task
        uses: PR-Pilot-AI/smart-actions/quick-task@v1
        with:
          # Description of the task to run
          task-description: "Echo Hello World"
```
