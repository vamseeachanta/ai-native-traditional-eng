# Examples

Domain-specific code examples and practical implementations of AI-native engineering approaches.

## Engineering Domains

### Mechanical Engineering (`/mechanical/`)
- CAD automation and generative design
- Finite Element Analysis (FEA) optimization
- Predictive maintenance systems
- Materials selection and testing

### Electrical Engineering (`/electrical/`)
- Circuit design automation
- Power system optimization
- Smart grid applications
- Signal processing and control systems

### Civil Engineering (`/civil/`)
- Structural analysis and optimization
- Traffic flow and transportation systems
- Infrastructure monitoring and maintenance
- Urban planning and development

### Chemical Engineering (`/chemical/`)
- Process optimization and control
- Reaction prediction and modeling
- Safety system automation
- Quality control and assurance

### AI Agents Integration
- Agent-based design assistance
- Autonomous analysis workflows
- Collaborative engineering agents
- Real-time monitoring and optimization agents

## Model Context Protocol (MCP) Integration

AI assistants can be seamlessly integrated with your existing engineering tools through the Model Context Protocol. See the **[mcp/](../mcp/)** folder for:

- **MCP Servers** - Connect AI to CAD, FEA, and database systems
- **Configuration Examples** - Ready-to-use configs for different engineering environments  
- **Integration Guides** - Step-by-step setup for popular engineering tools
- **Security Best Practices** - Safe deployment in engineering environments

### Quick MCP Examples

**CAD Integration:**
```python
# AI can read and modify your SolidWorks models
mcp_client.call_tool("solidworks", "get_parameters", {"model": "bracket.sldprt"})
```

**Material Database Access:**
```python
# AI can query your material databases
materials = mcp_client.call_tool("database", "find_materials", {"strength": ">250MPa"})
```

**Analysis Automation:**
```python
# AI can set up and run FEA analysis
analysis = mcp_client.call_tool("ansys", "run_analysis", {"model": "bracket.step"})
```

See **[mcp/README.md](../mcp/README.md)** for complete implementation details.
