# Commit-Monitor Action

The `commit-monitor` action is designed to enhance your workflow by allowing you to define specific keywords or commands (e.g., `/task`) within your commit messages. When these are detected, the action can automatically delegate follow-up work based on the content of your commit message. 

## Workflow Ideas

- **Generate Documentation** Use a `/document` command to automatically create documentation for the code you committed
- **Let AI finish your work** Commit code stubs and use an `/implement` command to let the AI agent build the rest
- **Create issues from commits** Use the `/issue` keyword to generate a new Github issue

## Usage

To use the `commit-monitor` action in your project, you'll need to include it in your GitHub workflow files. Define the keywords or commands you wish to monitor in your commit messages, and configure the action to perform the desired follow-up tasks when those keywords are detected.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.3.2`.
- `api-key`: (Required) Your API key for PR Pilot.
- `trigger-keyword`: (Required) The keyword to trigger task creation.

### Example Workflow

```yaml
name: Listen for /document command

on:
  push:

jobs:
  monitor-commit:
    runs-on: ubuntu-latest
    steps:
      - name: Monitor Commit
        uses: PR-Pilot-AI/smart-actions/commit-monitor@v1
        with:
          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}
          # Keyword that the AI agent will react to
          trigger-keyword: /document
```
