import requests
def get_user_stats(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
def get_top_repos(username, limit=5):
    url = f"https://api.github.com/users/{username}/repos"
    params = {"sort": "stars", "direction": "desc", "per_page": limit}
    response = requests.get(url, params=params)
    return response.json()
def main():
    username = input("GitHub username: ")
    user = get_user_stats(username)
    if not user:
        print("User not found")
        return
    print(f"Name: {user.get('name') or username}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Following: {user['following']}")
    repos = get_top_repos(username)
    print("Top repos:")
    for repo in repos:
        print(f"{repo['name']} - {repo['stargazers_count']} stars")
if __name__ == "__main__":
    main()
