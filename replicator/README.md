# Replicator Action

The `replicator` action is designed to automate the process of creating new files or code snippets based on existing templates with specified characteristics. This action can significantly streamline the development process by allowing for the quick replication of code or file structures with minimal manual intervention.

## Workflow Ideas

- **Template-based File Creation** Use a template path and characteristics to automatically generate files or code snippets.
- **Automate Code Snippets** Automatically create code snippets based on predefined templates and characteristics.
- **Custom File Generation** Use custom templates to generate new files with specific characteristics defined by the user.

## Usage

To use the `replicator` action in your project, you'll need to include it in your GitHub workflow files. Specify the template path, result path, and characteristics of the result to configure the action for your specific needs.

### Inputs

- `template`: (Required) Path to the template file or code snippet to replicate.
- `characteristics`: (Required) Characteristics of the result, described in natural language.
- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.0.3`.
- `api-key`: (Required) Your API key for PR Pilot.

### Example Workflow

```yaml
name: Replicate Template

on:
  workflow_dispatch:
    inputs:
      template:
        description: 'Path to the template file or code snippet to replicate'
        required: true
      characteristics:
        description: 'Characteristics of the result, described in natural language'
        required: true

jobs:
  replicate:
    runs-on: ubuntu-latest
    steps:
      - name: Replicate Template
        uses: PR-Pilot-AI/smart-actions/replicator@v1
        with:
          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          # Inputs for the replicator action
          template: ${{ github.event.inputs.template }}
          characteristics: ${{ github.event.inputs.characteristics }}
```
