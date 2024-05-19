# test_gcs_client.py
import pytest
from google.cloud import storage
from app.gcs_client import upload_to_gcs, GcsClientError
from unittest.mock import Mock, patch

def test_upload_to_gcs_success():
    """Test successful upload to GCS."""
    with patch.object(storage.Client, 'bucket') as mock_bucket:
        mock_bucket.return_value.blob.return_value.upload_from_string = Mock()
        assert upload_to_gcs("test_bucket", {"key": "value"}, "test_blob.json") is True

def test_upload_to_gcs_failure():
    """Test upload failure to GCS."""
    with patch.object(storage.Client, 'bucket', side_effect=Exception("Error")):
        with pytest.raises(GcsClientError):
            upload_to_gcs("test_bucket", {"key": "value"}, "test_blob.json")
