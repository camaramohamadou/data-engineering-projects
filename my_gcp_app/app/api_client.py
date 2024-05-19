import requests
import logging

class ApiClientError(Exception):
    """Custom exception for API client errors."""
    pass

def fetch_repo_details(repo_name):
    """
    Fetches details of a GitHub repository.
    
    Parameters:
    repo_name (str): Full name of the repository (e.g., 'octocat/Hello-World')

    Returns:
    dict: JSON response containing repository details.
    """
    if not repo_name:
        raise ValueError("Repository name must be provided.")

    try:
        GITHUB_API_BASE_URL = "https://api.github.com"
        url = f"{GITHUB_API_BASE_URL}/repos/{repo_name}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        raise ApiClientError(http_err)
    except Exception as err:
        logging.error(f"An error occurred: {err}")
        raise ApiClientError(err)

# Example usage:
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     try:
#         repo_details = fetch_repo_details("octocat/Hello-World")
#         logging.info(f"Repository details: {repo_details}")
#     except ApiClientError as e:
#         logging.error("Failed to fetch repository details.")
