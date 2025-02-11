import requests

def fetch_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    return commits

def generate_markdown(commits):
    markdown = "# Recent Commits\n\n"
    for commit in commits[:10]:  # 只取最近10次提交
        markdown += f"- {commit['commit']['message']} by {commit['commit']['author']['name']} on {commit['commit']['author']['date']}\n"
    return markdown

if __name__ == "__main__":
    repo = "github-commit-logger"  # 你的仓库名
    owner = "your-username"  # 你的GitHub用户名
    commits = fetch_commits(repo, owner)
    markdown = generate_markdown(commits)
    with open("commits.md", "w") as f:
        f.write(markdown)
