from google.cloud import storage
import json
import logging

class GcsClientError(Exception):
    """Custom exception for GCS client errors."""
    pass

def prepare_data_for_upload(data):
    """
    Prepares data for upload to GCS by converting it to a JSON string.

    Parameters:
    data (dict): Data to be converted into JSON.

    Returns:
    str: JSON string representation of the data.
    """
    if not data:
        raise ValueError("Data to upload cannot be empty.")
    return json.dumps(data)

def upload_to_gcs(bucket_name, data, destination_blob_name):
    """
    Uploads data to a specified Google Cloud Storage bucket.

    Parameters:
    bucket_name (str): Name of the GCS bucket.
    data (dict): Data to be uploaded.
    destination_blob_name (str): Name of the blob in GCS.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        json_data = prepare_data_for_upload(data)
        blob.upload_from_string(json_data, content_type='application/json')
        logging.info(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}")
        return True        
    except Exception as err:
        logging.error(f"Error uploading to {bucket_name}/{destination_blob_name}: {err}")
        raise GcsClientError(err)

# Example usage:
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     try:
#         test_data = {"key": "value"}  # Replace with actual data
#         upload_to_gcs("your_bucket_name", test_data, "test_blob.json")
#     except GcsClientError:
#         logging.error("Failed to upload data to GCS.")
