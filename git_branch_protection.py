#!/usr/local/bin/python3

from github import Github
from github.GithubException import UnknownObjectException, GithubException
import sys
import json


class GitHubProtection():
    """
    Class for managing branch protection in GitHub repositories.
    """

    def __init__(self, url, organization, username, access_token):
        """
        Initialize the GitHubProtection instance.

        Args:
            url (str): The GitHub API URL.
            organization (str): The name of the organization.
            username (str): The GitHub username.
            access_token (str): The GitHub access token.
        """
        self.github = Github(base_url=url, login_or_token=access_token)
        self.username = username
        self.org = self._get_one_org(organization)

    def _get_one_org(self, organization):
        try:
            org = self.github.get_organization(organization)
            return org
        except UnknownObjectException:
            print("ERROR: Organization '{0}' not found".format(organization))
            sys.exit(1)

    def _get_all_repos(self):
        repo_paginator = self.org.get_repos(type="all")
        return repo_paginator

    def _get_branch_protection_status(self, repo_obj):
        branch = self._get_master_branch(repo_obj)
        if branch:
            try:
                branch.get_protection()
                return True
            except GithubException as exception:
                if exception.status == 404:
                    return False
                else:
                    return "ERROR: status: {0} message: {1}".format(
                        exception.status,
                        exception.data["message"]
                    )
                return (exception.data)
        return "ERROR: Unable to find master branch"

    def _get_master_branch(self, repo_obj):
        try:
            branch = repo_obj.get_branch("master")
            return branch
        except GithubException:
            # Branch wasn't found
            return

    def _return_result_dict_output(self, repo_name, protected):
        return {
            "repo": repo_name,
            "protected": str(protected)
        }

    def _print_repos(self, repo_list):
        print(json.dumps(repo_list, indent=4))

    def view_all_repos(self, excludes):
        result_list = []
        repo_paginator = self._get_all_repos()
        active_repos = [repo_obj for repo_obj in repo_paginator if not repo_obj.archived]
        for repo_obj in active_repos:
            if repo_obj.name not in excludes:
                protected = self._get_branch_protection_status(repo_obj)
                result_dict = self._return_result_dict_output(
                    repo_obj.name,
                    protected
                )
                result_list.append(result_dict)
        self._print_repos(result_list)


if __name__ == "__main__":
    import arg_parser_file
    parser = arg_parser_file.create_arg_parser()
    args = parser.parse_args()

    git_protection = GitHubProtection(args.url,
                                      args.organization,
                                      args.username,
                                      args.token)

    if args.all:
        if args.view:
            git_protection.view_all_repos(args.excludes)
    elif args.repos:
        if args.view:
            git_protection.view_list_repos(args.repos)
