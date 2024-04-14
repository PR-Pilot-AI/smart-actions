<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="PR Pilot Logo">
</div>

<p align="center">
  <a href="https://github.com/apps/pr-pilot-ai/installations/new"><b>Install</b></a> |
  <a href="https://docs.pr-pilot.ai">Documentation</a> | 
  <a href="https://www.pr-pilot.ai/blog">Blog</a> | 
  <a href="https://www.pr-pilot.ai">Website</a>
</p>


# Smart Github Actions

This project contains easy-to-use, customizable Github Actions that you can use to automate your project in powerful ways.

## What is a Smart Action?

A Smart Action is a GitHub Action enhanced with AI capabilities, designed to automate and streamline your GitHub workflows. These actions can perform tasks such as formatting issues, reviewing pull requests, and more, with minimal configuration.

## Using Smart Actions in Your Projects

To use a Smart Action in your project, you can reference it in your GitHub workflow files. For example, the `issue_formatter.yaml` workflow uses the `PR-Pilot-AI/smart-actions/format-issue@v1` action to ensure new issues are properly formatted according to predefined instructions.

```yaml
name: Ensure new issue is properly formatted

# Triggers the workflow on new issue creation
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

          # Instructions for formatting the issue
          formatting-instructions: |
            - Ensure the title begins with an appropriate emoji
            - Issue body should be properly Markdown-formatted
            - If the issue has no labels, add some
```

## Creating Custom Smart Actions

To create your own custom Smart Actions, you can start by forking this repository or using it as a template. Customize the actions according to your project's needs by modifying the action's code and parameters. For detailed instructions on creating and customizing actions, refer to the [GitHub Actions documentation](https://docs.github.com/en/actions).

By leveraging Smart Actions, you can significantly enhance the automation capabilities of your GitHub projects, making your development process more efficient and streamlined.