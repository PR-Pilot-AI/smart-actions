# Smart Github Actions

This project contains easy-to-use, customizable Github Actions that you can use to automate your project in powerful ways.

## What is a Smart Action?

A Smart Action is a [GitHub Action](https://docs.github.com/en/actions) enhanced with AI capabilities, designed to automate Github projects in powerful new ways. You can use one of our curated, pre-defined actions or build your own.

Ready-to-use Smart Actions:

| Action    | How it helps you |
| -------- | ------- |
| `format-issue`  | Formats a Github issue, adds labels, checks for spelling errors, and more |
| `pr-creation-handler` | An AI agent looks at newly created PRs and runs checks or actions you define |


## Using Smart Actions in Your Projects

To use a Smart Action in your project, you can reference it in your GitHub workflow files under [`.github/workflows`](https://github.com/PR-Pilot-AI/smart-actions/tree/main/.github/workflows).

Here's a simple example that instructs an AI agent to automatically format and label every new issue in your project:

```yaml
# .github/workflows/issue_formatter.yaml`

name: Ensure new issue is properly formatted and labeled

on:
  issues:
    types: [opened]

jobs:
  format-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Format GitHub Issue
        uses: PR-Pilot-AI/smart-actions/format-issue@v1
        with:

          # API key for PR Pilot must be defined as a secret in the repository
          api-key: ${{ secrets.PR_PILOT_API_KEY }}

          # Number of the issue to be formatted
          issue-number: ${{ github.event.issue.number }}

          # Customize the instructions to your needs
          formatting-instructions: |
            - Ensure the title begins with an appropriate emoji
            - Issue body should be properly Markdown-formatted
            - If the issue has no labels, add some
```

Smart Actions use [PR Pilot](https://github.com/PR-Pilot-AI/pr-pilot) to execute the AI agent on your repository. Follow the **[user guide](https://docs.pr-pilot.ai/user_guide.html)** to get your API key!

## Creating Custom Smart Actions

To create a custom Smart Action, follow these steps:

1. **Identify the Trigger and Task**: Determine the event that should trigger the action and what the AI agent should do when the trigger is detected.

2. **Use an Existing Action as a Template**: Start by copying the `format-issue` action files (`format-issue/format-issue.py` and `format-issue/action.yaml`) as a template.

3. **Define Input Variables**: Decide which input variables your action will need.

4. **Configure the Trigger**: Based on your trigger, configure how the action should be triggered in the `action.yaml` file.

5. **Write Instructions for the AI Agent**: Turn your task description into clear, concise instructions for the AI agent in the `<action-name>.py` file.

6. **Create the Metadata File**: Fill out the `action.yaml` file with the valid trigger and input variables.

7. **Implement the Action Code**: Write the code in `<action-name>.py` that instructs the AI agent, using the template as a guide.

8. **Create a New Workflow**: Use the `.github/workflows/issue_formatter.yaml` as a template to create a new workflow that uses your custom action.

For additional guidance, refer to the `action-wizard/generate-new-action.py` script, which outlines the process of creating a new Smart Action, including translating task descriptions into instructions for the AI agent.