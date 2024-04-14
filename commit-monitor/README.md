# Commit-Monitor Action

The `commit-monitor` action is designed to enhance your workflow by allowing you to define specific keywords or commands (e.g., `/task`) within your commit messages. When these are detected, the action can automatically delegate follow-up work, such as creating issues, triggering other workflows, or notifying team members. This feature is particularly useful for automating routine tasks and ensuring that important follow-up actions are not overlooked in the development process.

## How It Helps You

- **Automate Follow-Up Tasks:** Automatically trigger specific actions or tasks based on keywords in commit messages.
- **Improve Workflow Efficiency:** Reduce manual oversight and intervention by automating the delegation of follow-up work.
- **Enhance Collaboration:** Ensure that team members are promptly notified or assigned tasks relevant to the commit, improving team collaboration and project management.

## Usage

To use the `commit-monitor` action in your project, you'll need to include it in your GitHub workflow files. Define the keywords or commands you wish to monitor in your commit messages, and configure the action to perform the desired follow-up tasks when those keywords are detected.

### Inputs

- `sdk-version`: (Optional) Specifies the PR Pilot SDK version to use. Default is `1.0.3`.
- `api-key`: (Required) Your API key for PR Pilot.
- `trigger-keyword`: (Required) The keyword to trigger task creation.

### Example Workflow

```yaml
name: Commit Monitor Workflow
on: [push]

jobs:
  commit-monitor:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: PR-Pilot-AI/smart-actions/commit-monitor@main
      with:
        api-key: ${{ secrets.PR_PILOT_API_KEY }}
        trigger-keyword: '/task'
