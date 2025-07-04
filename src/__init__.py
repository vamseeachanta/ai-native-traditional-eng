"""
AI-Native Traditional Engineering Package

A comprehensive framework for implementing AI-native approaches in traditional engineering disciplines.
"""

__version__ = "0.1.0"
__author__ = "AI-Native Engineering Team"
__license__ = "MIT"

from .core import BaseAgent, Config, Logger
from .utils import DataProcessor, ValidationUtils

__all__ = [
    "BaseAgent",
    "Config", 
    "Logger",
    "DataProcessor",
    "ValidationUtils"
]
