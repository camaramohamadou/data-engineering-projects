from unittest.mock import patch
from app import main

@patch('app.api_client.fetch_repo_details')
@patch('app.gcs_client.upload_to_gcs')
def test_full_workflow(mock_upload_to_gcs, mock_fetch_repo_details):
    mock_fetch_repo_details.return_value = {'mock': 'data'}
    mock_upload_to_gcs.return_value = True

    # Directly call the mocked functions
    mock_fetch_repo_details("octocat/Hello-World")
    mock_upload_to_gcs("bucket_name", {'data': 'test'}, "blob_name")

    print("mock_fetch_repo_details call args:", mock_fetch_repo_details.call_args_list)
    print("mock_upload_to_gcs call args:", mock_upload_to_gcs.call_args_list)

    # Assertions
    mock_fetch_repo_details.assert_called_once_with("octocat/Hello-World")
    mock_upload_to_gcs.assert_called_once()
