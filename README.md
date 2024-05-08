# Audit of Git Branch Protection Rules

This script is used to view or set the master branch protection for supplied repos or all repos in an org.

# Requirements
$ pip3 install PyGithub

# Examples

# QA examples
$  python3 git_branch_protection.py --url https://github.company.com/api/v3 --org devops-team --username ACC --token *** --view --all
$  python3 git_branch_protection.py --url https://github.company.com/api/v3 --org devops-team --username ACC --token *** --view --repo app-microservice-abc


## View chosen repos

```
python3 git_protection.py --url https://github.company.com/api/v3 --org <org> --username <username> --token <token> --view --repo microservice-123 --repo app-microservice-abc
```

## View all repos

```
python3 git_protection.py --url https://github.company.com/api/v3 --org <org> --username <username> --token <token> --view --all
```

## Protect chosen repos

```
python3 git_protection.py --url https://github.company.com/api/v3 --org <org> --username <username> --token <token> --protect --repo microservice-123 --repo app-microservice-abc
```

## Protect all repos

```
python3 git_protection.py --url https://github.company.com/api/v3 --org <org> --username <username> --token <token> --protect --all
```