## Agent OS Documentation

### Product Context
- **Mission & Vision:** @.agent-os/product/mission.md
- **Technical Architecture:** @.agent-os/specs/2025-07-31-agent-os-integration/sub-specs/technical-spec.md
- **Development Roadmap:** @.agent-os/specs/2025-07-31-agent-os-integration/spec.md

### Development Standards
- **Code Style:** @.agent-os/standards/code-style.md
- **Best Practices:** @.agent-os/standards/best-practices.md

### Project Management
- **Active Specs:** @.agent-os/specs/
- **Spec Planning:** Use `@.agent-os/instructions/create-spec.md`
- **Tasks Execution:** Use `@.agent-os/instructions/execute-tasks.md`

## AI-Native Engineering Context

This repository focuses on AI integration into traditional engineering:
- **Framework:** AI integration patterns and modernization strategies
- **Audience:** Traditional engineering teams adopting AI capabilities
- **Approach:** Structured AI adoption with proven patterns
- **Tools:** AI-assisted engineering workflows and decision support

When working on AI engineering features, ensure compatibility with traditional engineering practices and provide clear adoption pathways.

## Available Commands

- **Create-Module-Agent:** Available via `/create-module-agent` command

## Enhanced Features Available

This project supports enhanced Agent OS workflows including:
- **Enhanced Spec Creation**: Prompt summaries, executive summaries, mermaid diagrams, module organization
- **Cross-Repository Integration**: Shared components from AssetUtilities hub (@assetutilities: references)
- **Enhanced Task Execution**: Task summaries, performance tracking, real-time documentation
- **Template Variants**: minimal, standard, enhanced, api_focused, research
- **Visual Documentation**: Auto-generated system architecture and workflow diagrams

### Command Examples
```bash
# Enhanced spec creation
/create-spec feature-name module-name enhanced

# Traditional spec creation (backward compatible)  
/create-spec feature-name

# Enhanced task execution with summaries
/execute-tasks @specs/modules/module-name/spec-folder/tasks.md
```

### Cross-Repository References
- Shared components: @assetutilities:src/modules/agent-os/enhanced-create-specs/
- Sub-agent registry: @assetutilities:agents/registry/sub-agents/workflow-automation
- Hub configuration: @assetutilities:hub-config.yaml


## Self-Contained Agent OS

This repository includes a complete, self-contained Agent OS framework. All slash commands work immediately after `git clone` with no additional setup required.

### Available Slash Commands
- `/create-spec <spec-name>` - Create detailed specification documents
- `/execute-tasks <tasks-file>` - Execute tasks from specification
- `/create-module-agent <agent-name>` - Create specialized AI agents

### Local Agent OS Structure
- **Standards**: @.agent-os/standards/ (code style, best practices)
- **Instructions**: @.agent-os/instructions/ (workflow guidance)
- **Product Context**: @.agent-os/product/ (mission, roadmap, decisions)
- **Specifications**: @.agent-os/specs/ (feature specifications and tasks)

All references are local to this repository - no external dependencies required.
