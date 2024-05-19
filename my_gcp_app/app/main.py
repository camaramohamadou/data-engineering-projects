import logging
from app.api_client import fetch_repo_details, ApiClientError
from app.gcs_client import upload_to_gcs, GcsClientError

def main():
    repo_name = "octocat/Hello-World"  # GitHub repository to fetch
    bucket_name = "chouet-bidule"  # GCS bucket name
    destination_blob_name = "github_repo_data.json"  # File name in GCS

    try:
        # Fetch data from GitHub
        github_data = fetch_repo_details(repo_name)
        if github_data is not None:
            # Upload data to GCS
            upload_to_gcs(bucket_name, github_data, destination_blob_name)
        else:
            logging.error("No data received from GitHub API.")
    except ApiClientError as api_err:
        logging.error(f"Error fetching data from GitHub: {api_err}")
    except GcsClientError as gcs_err:
        logging.error(f"Error uploading data to GCS: {gcs_err}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
