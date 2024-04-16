# Workflow-Wizard Action

The `workflow-wizard` action is designed to automatically generate a new Github workflow based on a given description. This action simplifies the process of creating workflows by interpreting natural language descriptions and converting them into a functional workflow file.

## Workflow Ideas

- **Simplify Workflow Creation** Use a simple description like "Build and test my project on every push" to generate a corresponding workflow.
- **Customize Workflows** Provide detailed descriptions to create complex workflows tailored to your project's needs.
- **Automate Workflow Management** Streamline the process of updating and managing workflows by describing the changes you want.

## Usage

To use the `workflow-wizard` action in your project, you'll need to include it in your GitHub workflow files. Provide a description of the workflow you want to create, and the action will handle the rest.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.0.3`.
- `api-key`: (Required) Your API key for PR Pilot.
- `description`: (Required) The natural language description of the workflow you want to generate.

### Example Workflow

```yaml
name: Generate Workflow from Description

on:
  issue_comment:
    types: [created]

jobs:
  generate-workflow:
    runs-on: ubuntu-latest
    steps:
      - name: Generate Workflow
        uses: PR-Pilot-AI/smart-actions/workflow-wizard@v1
        with:
          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          # Description of the workflow to generate
          description: 'Automatically build and test on every push'
```
