# test_api_client.py
import pytest
from app.api_client import fetch_repo_details, ApiClientError

def test_fetch_repo_details_success():
    """Test fetching repository details successfully."""
    # Assuming 'octocat/Hello-World' will always exist
    result = fetch_repo_details("octocat/Hello-World")
    assert result is not None
    assert "full_name" in result

def test_fetch_repo_details_failure():
    """Test fetching repository details with invalid repo name."""
    with pytest.raises(ApiClientError):
        fetch_repo_details("nonexistent/repo")
