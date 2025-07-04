"""
Base agent class for AI-native engineering applications.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import logging


@dataclass
class AgentConfig:
    """Configuration for AI agents."""
    name: str
    model: str = "gpt-4"
    temperature: float = 0.1
    max_tokens: int = 2000
    tools: List[str] = None
    domain: str = "general"
    
    def __post_init__(self):
        if self.tools is None:
            self.tools = []


class BaseAgent(ABC):
    """
    Abstract base class for all AI engineering agents.
    
    Provides common functionality for agent initialization, task processing,
    logging, and error handling.
    """
    
    def __init__(self, config: AgentConfig):
        """
        Initialize the agent with configuration.
        
        Args:
            config: Agent configuration including model settings and tools
        """
        self.config = config
        self.logger = logging.getLogger(f"agent.{config.name}")
        self.tools = self._initialize_tools()
        self._setup_logging()
    
    def _setup_logging(self):
        """Configure logging for the agent."""
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def _initialize_tools(self) -> Dict[str, Any]:
        """
        Initialize tools based on configuration.
        
        Returns:
            Dictionary of initialized tool instances
        """
        tools = {}
        for tool_name in self.config.tools:
            try:
                tool = self._create_tool(tool_name)
                tools[tool_name] = tool
                self.logger.info(f"Initialized tool: {tool_name}")
            except Exception as e:
                self.logger.error(f"Failed to initialize tool {tool_name}: {e}")
        return tools
    
    def _create_tool(self, tool_name: str) -> Any:
        """
        Factory method for creating tool instances.
        
        Args:
            tool_name: Name of the tool to create
            
        Returns:
            Tool instance
            
        Raises:
            NotImplementedError: If tool creation is not implemented
        """
        raise NotImplementedError(f"Tool creation for {tool_name} not implemented")
    
    @abstractmethod
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process an engineering task.
        
        Args:
            task: Task specification and parameters
            
        Returns:
            Task results and analysis
        """
        pass
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate input data for the agent.
        
        Args:
            input_data: Input data to validate
            
        Returns:
            True if valid, False otherwise
        """
        # Basic validation - override in subclasses for specific requirements
        required_fields = getattr(self, 'required_fields', [])
        for field in required_fields:
            if field not in input_data:
                self.logger.error(f"Missing required field: {field}")
                return False
        return True
    
    def handle_error(self, error: Exception, context: str = "") -> Dict[str, Any]:
        """
        Handle errors during task processing.
        
        Args:
            error: Exception that occurred
            context: Additional context about the error
            
        Returns:
            Error response dictionary
        """
        error_msg = f"Error in {context}: {str(error)}"
        self.logger.error(error_msg)
        
        return {
            "success": False,
            "error": error_msg,
            "error_type": type(error).__name__,
            "context": context
        }
    
    def log_performance(self, task_id: str, duration: float, success: bool):
        """
        Log performance metrics for the task.
        
        Args:
            task_id: Unique identifier for the task
            duration: Task execution time in seconds
            success: Whether the task completed successfully
        """
        status = "SUCCESS" if success else "FAILED"
        self.logger.info(f"Task {task_id} - {status} - Duration: {duration:.2f}s")
