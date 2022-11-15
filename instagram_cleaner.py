import argparse
import zipfile
from json import load
from pathlib import Path


def analyze_zipfile(filepath: str) -> int:
    """Function that analyse an Instagram data dump in order to print the
    account that are not following back.

    Args:
        filepath: path to the instagram archive.
    """

    # Open the archive and read the file needed.
    with zipfile.ZipFile(filepath) as z:
        with z.open('followers_and_following/followers.json') as f:
            raw_follower_list = load(f)['relationships_followers']
        with z.open('followers_and_following/following.json') as f:
            raw_following_list = load(f)['relationships_following']

    # Preprocess the accounts information.
    def get_account_name(entry):
        return entry['string_list_data'][0]['value']

    follower_list = [get_account_name(follower) for follower in raw_follower_list]
    following_list = [get_account_name(following) for following in raw_following_list]

    # Take the set difference, in order to find the account that are not following back.
    account_list = list(set(following_list) - set(follower_list))
    for index, account in enumerate(account_list):
        print(f'{index} - {account} - https://www.instagram.com/{account}')
    return 0


def main() -> int:
    """Main function acting as the entry point. It contains the parser as
    well as the code to execute the `analyze_zipfile` function.
    """

    # Create a parser to give the user an interface to interact with.
    parser = argparse.ArgumentParser(
        description='instagram-cleaner',
        usage='Use "instagram-cleaner filepath" in order to analyze the '
              'instagram zipfile and print the account names that do not '
              'follow you back',
    )
    parser.add_argument('filepath', help='Path of the instagram zip file.')

    # Parse arguments.
    args = parser.parse_args()
    filepath = Path(args.filepath)

    # Execute the main function if the file exists.
    if filepath.is_file():
        return analyze_zipfile(filepath=filepath)
    else:
        raise FileNotFoundError(f'"{args.filepath}" does not exist.')


if __name__ == '__main__':
    raise SystemExit(main())
