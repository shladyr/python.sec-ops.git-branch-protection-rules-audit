from argparse import ArgumentParser

def create_arg_parser():
    parser = ArgumentParser(description="Branch Protection")

    parser.add_argument( "--url",      dest="url",          required=True, help="Github API URL" )
    parser.add_argument( "--org",      dest="organization", required=True, help="Github organization" )
    parser.add_argument( "--username", dest="username",     required=True, help="Github username" )
    parser.add_argument( "--token",    dest="token",        required=True, help="Github Access Token" )

    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument( "--protect",  dest="protect",      action="store_true", help="Set protection on master branch" )
    action.add_argument( "--view",     dest="view",         action="store_true", help="View branch protection settings" )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument( "--repo",     dest="repos",        action="append",             help="Repos you wish to target" )
    target.add_argument( "--all",      dest="all",          action="store_true",         help="Target all repos" )
    parser.add_argument( "--exclude",  dest="excludes",     action="append", default=[], help="Repos to exclude when using --all" )

    args = parser.parse_args()

    if args.excludes and not args.all:
        print("--exclude should only be used when using --all")
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser
