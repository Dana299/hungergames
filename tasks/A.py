import re
from typing import List


class InvalidGithubURLError(ValueError):
    pass


def extract_project_name(url: str) -> str:
    """
    Extract repository name from a given github url. Raise InvalidGithubURLError if url is invalid.
    """
    regex = r"https://github.com/[\w\-]+/([\w\-]+)(\.git)?"
    match = re.fullmatch(regex, url)
    if not match:
        raise InvalidGithubURLError()
    return match.group(1)


def process_urls(urls_list: List[str]):
    """Print project name for each url in given list."""
    for url in urls_list:
        try:
            project_name = extract_project_name(url)
            print(url, ' -> ', project_name)
        except InvalidGithubURLError:
            print(url, ' -> invalid URL')
