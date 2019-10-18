import requests


class Repository:

    _RELEASES_PATTERN = "https://api.github.com/repos/{owner}/{repo}/releases"

    def __init__(self, owner: str, name: str) -> None:
        self.owner = owner
        self.name = name

    @staticmethod
    def from_url(url: str) -> "Repository":
        splitted = url.split("/")
        repo = splitted[-1]
        owner = splitted[-2]
        return Repository(owner, repo)

    def list_releases(self):
        url = Repository._RELEASES_PATTERN.format(owner=self.owner, repo=self.name)
        resp = requests.get(url)
        return resp.json()

    def __str__(self) -> str:
        return f"{self.owner}/{self.name}"

    def __repr__(self) -> str:
        return str(self)
