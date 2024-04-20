# Plan and Execute Action

The `Plan and Execute` action implements a pattern common in AI-driven workflows. It uses two steps to execute high-level instructions:

1. **Plan**: The agent plans the task based on the provided description and expected result.
2. **Execute**: The agent executes the plan

This has proven to be a useful pattern for more complex tasks that require careful planning and research.

## Workflow Ideas

- **Tutorial-Driven Implementation** - Let the AI agent find and read a tutorial on the internet and then implement the tutorial's instructions in your project
- **Automatic Bug Research** - Let the agent read all new issues labeled as `bug`, find the root cause, and suggest a fix
- **Automated Code Refactoring** - Let the agent analyze your codebase and suggest refactoring opportunities

## Usage

To use the `Plan and Execute` action in your project, you'll need to include it in your GitHub workflow files. Define the task description and expected result, and configure the action to perform the planning and execution phases.

### Inputs

- `task-description`: (Required) The description of the task to plan.
- `expected-result`: (Required) The expected result of the execution phase.

### Example Workflow

```yaml
# .github/workflows/build_from_tutorial.yaml

name: "🚀 Build from Tutorial"

on:
  workflow_dispatch:
    inputs:
      what-to-build:
        description: 'Find a tutorial online and use it to build:'
        required: true

jobs:
  build-from-tutorial:
    runs-on: ubuntu-latest
    steps:
      - name: Find tutorial and build
        uses: PR-Pilot-AI/smart-actions/plan-and-execute@v1
        with:
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          task-description: |
            Find a tutorial online on how to build:
            
            ```
            ${{ github.event.inputs.what-to-build }}
            ```
          expected-result: |
            New and updated files in the repository that implement the task based on the tutorial.
```