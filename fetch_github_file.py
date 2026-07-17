import requests

def fetch_github_file(owner: str, repo: str, file_path: str, branch: str = "main") -> str:
    """
    Fetches the content of a specific file from a public GitHub repository.
    
    Args:
        owner: The GitHub username or organization (e.g., 'google').
        repo: The repository name (e.g., 'requests').
        file_path: The path to the file inside the repo (e.g., 'src/utils.py').
        branch: The branch name (defaults to 'main').
    """
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return f"Error fetching file: HTTP {response.status_code}. Please check the owner, repo, branch, and file path."