analyze and fix the Github issue: $ARGUMENTS

Steps:

# Plan
- use 'gh issue view' to get the issue details
- analyze the issue description and comments
- ask clarifying questions if necessary
- understand the prior art for this issue
 - search scratchpad for previous thoughts related to the issue
 - search PRs to see if there are any related pull requests
 - search codebase for relevant files
 - search issues to see if there are any related issues
 - search discussions to see if there are any related discussions
- think harder on how to break down the issue into series of smaller, manageable tasks
- Document plan in a new scratchpad
  - include the issue name in the filename
  - include link to the issue in the scratchpad

# Create
- create a new branch for the issue
- solve the issue in small, manageable steps, according to the plan
- commit changes with clear, descriptive commit messages after each step
- push changes to the remote branch
- create a pull request with a clear, descriptive title and description


# Test

- write tests for the changes made


# Deploy


# References

https://www.anthropic.com/engineering/claude-code-best-practices
