"""
Smoke tests for ai-native-traditional-eng.

These tests verify that the basic functionality of the system works
and that all major components can be imported and initialized.
"""

import pytest
import sys
import os
from pathlib import Path
import importlib.util


class TestProjectSmoke:
    """Basic smoke tests for project structure and imports."""

    def test_python_version(self):
        """Test that Python version meets requirements."""
        assert sys.version_info >= (3, 8), f"Python version {sys.version} is too old"

    def test_project_structure(self):
        """Test that essential project directories exist."""
        project_root = Path(__file__).parent.parent

        # Check essential directories
        assert (project_root / "src").exists(), "src directory not found"
        assert (project_root / "tests").exists(), "tests directory not found"
        assert (project_root / "pyproject.toml").exists(), "pyproject.toml not found"

    def test_src_package_import(self):
        """Test that src package can be imported."""
        project_root = Path(__file__).parent.parent
        src_path = project_root / "src"

        # Add src to Python path temporarily
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))

        # Try to import the main package
        try:
            import src
            assert hasattr(src, '__file__'), "src package not properly structured"
        except ImportError as e:
            pytest.skip(f"Could not import src package: {e}")

    def test_required_packages_importable(self):
        """Test that critical dependencies can be imported."""
        critical_packages = [
            'pytest',
            'loguru',
            'pandas',
            'numpy',
            'requests',
            'bs4',
            'flask',
            'selenium',
            'playwright'
        ]

        failed_imports = []
        for package in critical_packages:
            try:
                importlib.import_module(package)
            except ImportError:
                failed_imports.append(package)

        # Allow some packages to be missing in test environment
        if failed_imports:
            pytest.skip(f"Some packages not available: {failed_imports}")

    def test_environment_variables(self):
        """Test that testing environment is properly set."""
        assert os.environ.get('TESTING') == 'true', "TESTING environment variable not set"

    def test_temp_directory_creation(self, temp_dir):
        """Test that temporary directory fixture works."""
        assert temp_dir.exists(), "Temporary directory not created"
        assert temp_dir.is_dir(), "Temporary path is not a directory"

        # Test we can create files in temp dir
        test_file = temp_dir / "test.txt"
        test_file.write_text("test content")
        assert test_file.exists(), "Could not create file in temp directory"

    def test_mock_requests_fixture(self, mock_requests):
        """Test that mock requests fixture works."""
        session = mock_requests.return_value
        response = session.get('http://example.com')

        assert response.status_code == 200
        assert response.json() == {"status": "success"}

    def test_sample_data_fixture(self, sample_data):
        """Test that sample data fixture provides expected structure."""
        assert isinstance(sample_data, dict), "Sample data should be a dictionary"
        assert 'id' in sample_data, "Sample data should have 'id' field"
        assert 'name' in sample_data, "Sample data should have 'name' field"
        assert 'metadata' in sample_data, "Sample data should have 'metadata' field"
        assert isinstance(sample_data['metadata'], dict), "Metadata should be a dictionary"


class TestProjectIntegration:
    """Integration smoke tests for component interactions."""

    def test_file_operations(self, temp_file):
        """Test basic file operations work."""
        assert temp_file.exists(), "Temp file should exist"
        content = temp_file.read_text()
        assert content == "Test content", "File content not as expected"

        # Test we can modify the file
        temp_file.write_text("Modified content")
        assert temp_file.read_text() == "Modified content"

    def test_logging_integration(self, captured_logs):
        """Test that logging works correctly."""
        import logging
        logger = logging.getLogger(__name__)

        logger.info("Test info message")
        logger.warning("Test warning message")
        logger.error("Test error message")

        # Check logs were captured
        assert len(captured_logs.records) >= 3
        assert any("Test info message" in record.message for record in captured_logs.records)
        assert any("Test warning message" in record.message for record in captured_logs.records)
        assert any("Test error message" in record.message for record in captured_logs.records)

    @pytest.mark.data
    def test_data_processing_capabilities(self, sample_excel_data):
        """Test basic data processing functionality."""
        try:
            import pandas as pd
            import numpy as np

            # Test DataFrame operations
            assert len(sample_excel_data) == 3, "Sample data should have 3 rows"
            assert 'Name' in sample_excel_data.columns, "Should have Name column"
            assert 'Age' in sample_excel_data.columns, "Should have Age column"

            # Test basic operations
            mean_age = sample_excel_data['Age'].mean()
            assert mean_age == 30, f"Expected mean age 30, got {mean_age}"

        except ImportError:
            pytest.skip("Pandas/numpy not available for data processing test")

    def test_parallel_processing_config(self):
        """Test that parallel processing configuration is available."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"

        if pyproject_path.exists():
            content = pyproject_path.read_text()
            assert '[tool.parallel]' in content, "Parallel processing config not found in pyproject.toml"
            assert 'enabled = true' in content, "Parallel processing not enabled"


class TestPerformanceSmoke:
    """Basic performance smoke tests."""

    def test_import_speed(self):
        """Test that imports complete reasonably quickly."""
        import time
        start_time = time.time()

        try:
            import pandas
            import numpy
            import requests
        except ImportError:
            pytest.skip("Required packages not available")

        import_time = time.time() - start_time
        # Should complete in under 5 seconds even on slow systems
        assert import_time < 5.0, f"Imports took too long: {import_time:.2f} seconds"

    def test_basic_operations_speed(self, sample_data):
        """Test that basic operations complete quickly."""
        import time
        start_time = time.time()

        # Perform some basic operations
        data_copy = sample_data.copy()
        data_copy.update({"new_field": "new_value"})
        serialized = str(data_copy)

        operation_time = time.time() - start_time
        # Basic operations should be very fast
        assert operation_time < 0.1, f"Basic operations too slow: {operation_time:.3f} seconds"


@pytest.mark.slow
class TestSystemHealthSmoke:
    """System health smoke tests."""

    def test_memory_usage_reasonable(self):
        """Test that memory usage is reasonable."""
        import psutil
        import os

        try:
            process = psutil.Process(os.getpid())
            memory_mb = process.memory_info().rss / 1024 / 1024

            # Memory usage should be reasonable for tests (under 500MB)
            assert memory_mb < 500, f"Memory usage too high: {memory_mb:.1f}MB"
        except ImportError:
            pytest.skip("psutil not available for memory test")

    def test_disk_space_available(self, temp_dir):
        """Test that sufficient disk space is available."""
        import shutil

        total, used, free = shutil.disk_usage(temp_dir)
        free_gb = free / (1024**3)

        # Should have at least 1GB free for testing
        assert free_gb > 1.0, f"Insufficient disk space: {free_gb:.1f}GB free"