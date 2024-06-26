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

Easy-to-use, AI-powered Github Actions - customized and supercharged using natural language.

## What is a Smart Action?

A Smart Action is a [GitHub Action](https://docs.github.com/en/actions) enhanced with **AI capabilities**, designed to automate Github projects in powerful new ways. You can use one of our curated, pre-defined actions or build your own.

### Ready-to-use Smart Actions

All the actions defined here are also actively used in this project.

| Action                                                                                                                     | How it helps you                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`format-issue`](https://github.com/PR-Pilot-AI/smart-actions/actions/workflows/issue_formatter.yaml)                      | When a new issue is created, an AI agent formats it, adds labels, checks for spelling errors, and more                                                                                      |
| [`pr-creation-handler`](https://github.com/PR-Pilot-AI/smart-actions/actions/workflows/auto_review_new_pull_requests.yaml) | An AI agent looks at every new PR and runs checks or actions that you define                                                                                                                |
| [`commit-monitor`](./commit-monitor)                                                                                       | Define a keyword / command (e.g. `/task`) and use it in commit messages to delegate follow-up work                                                                                          |
| [`replicator`](./replicator)                                                                                               | Take existing files / code and let AI generate something similar (Demo: [Smart Action Copy Cat](https://github.com/PR-Pilot-AI/smart-actions/actions/workflows/smart_action_copy_cat.yaml)) |
| [`quick-task`](./quick-task)                                                                                               | Quickly instruct AI agent to do work for you                                                                                                                                                |
| [`plan-and-execute`](./plan-and-execute)                                                                                   | Run more complex tasks by letting the agent create a plan first and then execute it                                                                                                         |
| [`respond-to-issue`](./respond-to-issue)                                                                                   | Reads the issue based on issue number, potentially takes action based on issue content, and adds a comment to the issue with a response                                                    |

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

You can create your own custom actions using the wizard action or manually.

### Using the Action Wizard

The wizard is a special Smart Action that generates new Smart Actions based on your input.

![Action Wizard](wizard.png)

To try it out, just fork the project, put your API Key in the repository secrets ([user guide](https://docs.pr-pilot.ai/user_guide.html)) and run the wizard action.


### Using the Python SDK
For full control and even more customization, you can use the **[PR Pilot Python SDK](https://github.com/PR-Pilot-AI/pr-pilot-python)**.

Every smart action has two components:

* **Action manifest** - A YAML file that describes the action, defines its inputs and what steps to run
* **PR Pilot Instructions** - You instruct the AI agent using the Python SDK

To see how it works, check out how we define our pre-defined actions:

* [Issue Formatter](./format-issue)
* [PR Creation Handler](./pr-creation-handler)
