# General Code Best Practices (Adapted from Anthropic Claude Guide)

These best practices are adapted from Anthropic's Claude Code Best Practices, reworded for general context and applicable to various code-writing and code-review situations.

---

## 1. Be Explicit and Unambiguous

- **Clarify requirements**: Specify input, output, constraints, and any edge cases.
- **State assumptions**: If something is unclear, clarify it rather than guessing.
- **Prefer clarity over brevity**: Write code and documentation that is easy to read and understand.

## 2. Write Simple, Readable Code

- **Simplicity first**: Use the simplest approach that solves the problem.
- **Readable naming**: Choose descriptive names for variables, functions, and classes.
- **Consistent style**: Follow a consistent code style (indentation, naming, etc.).

## 3. Structure and Organize Code Logically

- **Group related code**: Organize code into logical blocks, functions, or modules.
- **Limit function size**: Keep functions focused and not too long.
- **Decompose problems**: Break down complex problems into smaller, manageable pieces.

## 4. Handle Errors and Edge Cases

- **Anticipate failure**: Check for invalid inputs and potential error conditions.
- **Graceful handling**: Handle errors explicitly, avoiding silent failures.
- **Test boundaries**: Consider edge cases, such as empty inputs or large data.

## 5. Write Descriptive Comments and Documentation

- **Explain intent**: Comment on non-obvious logic and decisions, not trivial code.
- **Document interfaces**: Provide docstrings or comments for public APIs and functions.
- **Update comments**: Keep comments accurate as code evolves.

## 6. Think About Testing

- **Write tests**: Provide tests for important functionality and edge cases.
- **Automate where possible**: Use automated tests to verify correctness.
- **Test coverage**: Strive for meaningful coverage, especially on critical paths.

## 7. Optimize for Maintainability

- **Refactor as needed**: Improve and clean up code as requirements change.
- **Avoid duplication**: Reuse code where appropriate.
- **Encapsulate complexity**: Hide implementation details behind clear interfaces.

## 8. Ensure Security and Privacy

- **Validate inputs**: Always validate data from untrusted sources.
- **Limit exposure**: Avoid leaking sensitive information in logs or errors.
- **Follow best practices**: Stay up to date with security recommendations for your tech stack.

## 9. Collaborate and Seek Feedback

- **Peer review**: Request code reviews and be open to suggestions.
- **Communicate clearly**: Discuss design choices and alternatives with peers.
- **Learn and adapt**: Incorporate feedback and update practices as needed.

## 10. Stay Current and Pragmatic

- **Use proven tools**: Prefer well-supported libraries and frameworks.
- **Balance idealism and pragmatism**: Make reasonable trade-offs between code quality and delivery.
- **Keep learning**: Stay updated with evolving best practices in your field.

---

*Adapted from Anthropic's Claude Code Best Practices: [original source](https://www.anthropic.com/engineering/claude-code-best-practices)*