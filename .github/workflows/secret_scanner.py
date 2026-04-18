import requests
import re
import time
import os
import base64

# MISSION: Scan all repositories for potential secret leaks
# REQUIREMENTS: pip install requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") # Run with: $env:GITHUB_TOKEN="your_token"; python script.py
USERNAME = "NickiMash17"

# Common patterns for secrets
PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "GitHub Token": r"(ghp|gho|ghu|ghs|ghr)_[a-zA-Z0-9]{36}",
    "Generic Secret": r"(?i)(password|secret|key|api_key|passwd)\s*[:=]\s*['\"]([^'\"]+)['\"]"
}

def get_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch repositories: {response.status_code}")
            try:
                print(f"   Message: {response.json().get('message')}")
            except:
                print(f"   Raw Response: {response.text}")
            break

        data = response.json()
        if not isinstance(data, list) or not data: break
        repos.extend([(r['name'], r['private']) for r in data])
        page += 1
    return repos

def verify_secret_in_content(repo_name, file_path, patterns):
    """Fetches file content and verifies if it actually matches the regex."""
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/contents/{file_path}"
    res = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    
    if res.status_code == 200:
        content_data = res.json()
        if content_data.get('encoding') == 'base64':
            try:
                # Decode base64 content
                decoded_content = base64.b64decode(content_data['content']).decode('utf-8')
                found_matches = []
                for label, pattern in patterns.items():
                    if re.search(pattern, decoded_content):
                        found_matches.append(label)
                return found_matches
            except:
                return []
    return []

def scan_repo(repo_name, is_private):
    print(f"⚓ Scanning {'[PRIVATE] ' if is_private else ''}{repo_name}...")
    for label, pattern in PATTERNS.items():
        exclude_query = "-path:node_modules -path:package-lock.json -path:vendor -path:.venv"
        term = label.split()[0].lower()
        query = f"repo:{USERNAME}/{repo_name} \"{term}\" {exclude_query}"
        
        url = f"https://api.github.com/search/code?q={query}"
        res = requests.get(url, headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        })
        
        if res.status_code == 200:
            results = res.json()
            items = results.get('items', [])
            
            for item in items:
                file_path = item.get('path')
                # Double-check the file content with the actual Regex
                matches = verify_secret_in_content(repo_name, file_path, {label: pattern})
                if matches:
                    print(f"  [!] CONFIRMED {label} found in {repo_name}!")
                    print(f"      - Location: {file_path}")

        elif res.status_code == 403:
            print("  [!] Rate limit hit. Waiting 30 seconds...")
            time.sleep(30)
        
        # Respect rate limits
        time.sleep(3)

if __name__ == "__main__":
    if not GITHUB_TOKEN or GITHUB_TOKEN == "YOUR_PERSONAL_ACCESS_TOKEN":
        print("❌ Please provide a GitHub Personal Access Token.")
    else:
        all_repos = get_repos()
        print(f"🚢 Found {len(all_repos)} repositories. Starting inspection...")
        for repo in all_repos:
            repo_name, is_private = repo
            try:
                scan_repo(repo_name, is_private)
            except Exception as e:
                print(f"Error scanning {repo_name}: {e}")