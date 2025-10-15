# conftest.py
#
# Pytest configuration and shared fixtures for ai-native-traditional-eng
# This file contains shared fixtures and configuration for all tests

import pytest
import os
import tempfile
from pathlib import Path
from typing import Generator, Any
from unittest.mock import Mock, patch

# Set testing environment
os.environ['TESTING'] = 'true'


# Basic fixtures
@pytest.fixture(scope="session")
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="function")
def mock_logger():
    """Mock logger for testing."""
    return Mock()


@pytest.fixture(scope="function")
def sample_data() -> dict[str, Any]:
    """Sample data for testing."""
    return {
        "id": 1,
        "name": "Test Item",
        "description": "A test item for testing purposes",
        "active": True,
        "metadata": {
            "created_at": "2025-01-01T00:00:00Z",
            "tags": ["test", "sample"]
        }
    }


# File system fixtures
@pytest.fixture(scope="function")
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing."""
    test_file = temp_dir / "test_file.txt"
    test_file.write_text("Test content")
    yield test_file


@pytest.fixture(scope="function")
def empty_temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create an empty temporary file for testing."""
    test_file = temp_dir / "empty_file.txt"
    test_file.touch()
    yield test_file


# Mock fixtures for web scraping and data processing
@pytest.fixture(scope="function")
def mock_requests():
    """Mock requests library for HTTP testing."""
    with patch('requests.Session') as mock_session:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success"}
        mock_response.text = '{"status": "success"}'
        mock_response.content = b'{"status": "success"}'
        mock_session.return_value.get.return_value = mock_response
        mock_session.return_value.post.return_value = mock_response
        yield mock_session


@pytest.fixture(scope="function")
def mock_selenium_driver():
    """Mock Selenium WebDriver for browser automation testing."""
    with patch('selenium.webdriver.Chrome') as mock_driver:
        mock_driver.return_value.get.return_value = None
        mock_driver.return_value.find_element.return_value = Mock()
        mock_driver.return_value.page_source = "<html><body>Test Page</body></html>"
        mock_driver.return_value.current_url = "http://example.com"
        yield mock_driver


@pytest.fixture(scope="function")
def mock_playwright():
    """Mock Playwright for browser automation testing."""
    with patch('playwright.sync_api.sync_playwright') as mock_playwright:
        mock_page = Mock()
        mock_page.goto.return_value = None
        mock_page.content.return_value = "<html><body>Test Page</body></html>"
        mock_page.url = "http://example.com"

        mock_browser = Mock()
        mock_browser.new_page.return_value = mock_page

        mock_context = Mock()
        mock_context.new_page.return_value = mock_page
        mock_context.browser = mock_browser

        mock_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
        yield mock_playwright


# Data processing fixtures
@pytest.fixture(scope="function")
def sample_excel_data():
    """Sample Excel data for testing."""
    import pandas as pd
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Tokyo']
    })


@pytest.fixture(scope="function")
def sample_pdf_content():
    """Sample PDF content for testing."""
    return "This is sample PDF content for testing purposes."


# Environment fixtures
@pytest.fixture(scope="function")
def test_env_vars():
    """Set test environment variables."""
    test_vars = {
        'TEST_MODE': 'true',
        'DEBUG': 'false',
        'SCRAPY_SETTINGS_MODULE': 'tests.fixtures.scrapy_settings'
    }

    # Store original values
    original_values = {}
    for key, value in test_vars.items():
        original_values[key] = os.environ.get(key)
        os.environ[key] = value

    yield test_vars

    # Restore original values
    for key, original_value in original_values.items():
        if original_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original_value


# Flask app fixture for web scraping projects
@pytest.fixture(scope="function")
def mock_flask_app():
    """Mock Flask application for testing."""
    with patch('flask.Flask') as mock_app:
        mock_app.return_value.run.return_value = None
        mock_app.return_value.route.return_value = lambda f: f
        yield mock_app


# Custom markers
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "e2e: mark test as an end-to-end test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "web: mark test as web scraping test")
    config.addinivalue_line("markers", "data: mark test as data processing test")
    config.addinivalue_line("markers", "selenium: mark test as requiring selenium")
    config.addinivalue_line("markers", "playwright: mark test as requiring playwright")


# Pytest hooks
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
            item.add_marker(pytest.mark.slow)


# Time mocking fixture
@pytest.fixture(scope="function")
def mock_time():
    """Mock time functions for consistent testing."""
    import time
    import datetime

    fixed_time = datetime.datetime(2025, 1, 1, 12, 0, 0)
    fixed_timestamp = fixed_time.timestamp()

    with patch('time.time', return_value=fixed_timestamp), \
         patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        mock_datetime.utcnow.return_value = fixed_time
        yield fixed_time


@pytest.fixture(scope="function")
def captured_logs(caplog):
    """Capture log messages for testing."""
    import logging
    caplog.set_level(logging.DEBUG)
    yield caplog