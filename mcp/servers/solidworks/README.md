# SolidWorks MCP Server

MCP server for integrating AI assistants with SolidWorks CAD software.

## Features

- Read model parameters and properties
- Access drawing dimensions and annotations
- Query material assignments and properties
- Extract geometric features and constraints
- Limited parameter modification capabilities

## Installation

```bash
# Install dependencies
pip install model-context-protocol
pip install win32com.client  # For SolidWorks API access

# Install this server
cd servers/solidworks
pip install -e .
```

## Configuration

```yaml
# config.yaml
solidworks:
  application_path: "C:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/SLDWORKS.exe"
  timeout: 30
  permissions:
    read: ["models", "drawings", "parameters", "materials"]
    write: ["parameters"]  # Limited write access
  security:
    require_confirmation: true
    log_all_operations: true
```

## Usage Examples

### Reading Model Parameters
```python
from mcp import Client

client = Client()

# Get all parameters from active model
parameters = client.call_tool("solidworks", "get_parameters", {
    "model": "active"
})

print(f"Model parameters: {parameters}")
```

### Querying Material Properties
```python
# Get material properties for current part
material_info = client.call_tool("solidworks", "get_material", {
    "model": "bracket_v1.sldprt"
})

print(f"Material: {material_info.name}")
print(f"Density: {material_info.density}")
print(f"Yield Strength: {material_info.yield_strength}")
```

### Modifying Parameters
```python
# Update design parameters
result = client.call_tool("solidworks", "set_parameter", {
    "model": "bracket_v1.sldprt",
    "parameter": "thickness",
    "value": 5.0,
    "units": "mm"
})

if result.success:
    print("Parameter updated successfully")
    print(f"New value: {result.new_value}")
```

## Available Tools

### Model Information
- `get_models()` - List open models
- `get_active_model()` - Get currently active model
- `get_model_info(model_name)` - Get model metadata

### Parameters and Features
- `get_parameters(model)` - Get all model parameters
- `set_parameter(model, name, value)` - Modify parameter value
- `get_features(model)` - List all features in model
- `get_feature_info(model, feature_name)` - Get feature details

### Materials and Properties
- `get_material(model)` - Get assigned material
- `set_material(model, material_name)` - Assign material
- `get_mass_properties(model)` - Calculate mass, volume, center of gravity

### Geometry and Dimensions
- `get_dimensions(model)` - Get all dimensions
- `get_constraints(model)` - Get geometric constraints
- `export_geometry(model, format)` - Export to STEP, IGES, STL

## Server Implementation

The server is implemented using the SolidWorks API and follows MCP best practices:

```python
import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent
import win32com.client as win32

class SolidWorksServer:
    def __init__(self):
        self.app = None
        self.server = Server("solidworks")
        self._setup_tools()
    
    def _setup_tools(self):
        """Register available tools with the MCP server."""
        tools = [
            Tool(
                name="get_parameters",
                description="Get all parameters from a SolidWorks model",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "model": {"type": "string", "description": "Model name or 'active'"}
                    },
                    "required": ["model"]
                }
            ),
            # Additional tools...
        ]
        
        for tool in tools:
            self.server.register_tool(tool)
    
    async def get_parameters(self, model: str):
        """Get parameters from SolidWorks model."""
        try:
            if not self.app:
                self.app = win32.Dispatch("SldWorks.Application")
            
            if model == "active":
                doc = self.app.ActiveDoc
            else:
                doc = self.app.OpenDoc(model, 1)  # 1 = part document
            
            # Extract parameters
            parameters = {}
            equations = doc.GetEquationMgr()
            
            for i in range(equations.GetCount()):
                equation = equations.Equation(i)
                name = equations.Variable(i)
                value = equations.Value(i)
                parameters[name] = value
            
            return {"parameters": parameters, "success": True}
            
        except Exception as e:
            return {"error": str(e), "success": False}

async def main():
    server = SolidWorksServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
```

## Security Considerations

### Access Control
- Read-only access by default
- Parameter modifications require explicit permission
- All operations are logged for audit
- User confirmation required for write operations

### Best Practices
- Run server on local machine only
- Use Windows authentication for SolidWorks access
- Regular security audits of server configuration
- Backup models before allowing AI modifications

## Troubleshooting

### Common Issues

**SolidWorks Not Found**
```
Error: SolidWorks application not found
Solution: Ensure SolidWorks is installed and licensed
```

**Permission Denied**
```
Error: Access denied to SolidWorks API
Solution: Run as administrator or check SolidWorks API settings
```

**Model Not Found**
```
Error: Cannot open model file
Solution: Check file path and ensure model is not corrupted
```

### Debug Mode
```bash
# Run server with debug logging
python solidworks_server.py --debug

# Test individual tools
python test_tools.py --tool get_parameters --model bracket.sldprt
```

## Development

### Adding New Tools
1. Define tool schema in `_setup_tools()`
2. Implement tool handler method
3. Add error handling and validation
4. Update documentation and tests

### Testing
```bash
# Run unit tests
pytest tests/

# Integration tests (requires SolidWorks)
pytest tests/integration/ --solidworks
```

---

*This MCP server enables seamless integration between AI assistants and SolidWorks, allowing engineers to get AI assistance directly within their CAD workflow.*
