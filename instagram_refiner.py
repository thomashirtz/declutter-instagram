import argparse
import zipfile
from json import load
from pathlib import Path
from typing import Any, Dict, List


def get_account_name(raw_entry: Dict[str, Any]) -> str:
    """Function that can process a raw JSON instagram account entry.
    
    Args:
        raw_entry: Raw JSON instagram account entry 

    Returns:
        The name of the instagram account.
    """
    return raw_entry['string_list_data'][0]['value']


def analyze_zipfile(filepath: str) -> int:
    with zipfile.ZipFile(filepath) as z:
        with z.open('followers_and_following/followers.json') as f:
            raw_followers_list = load(f)['relationships_followers']
            followers_list = list(map(get_account_name, raw_followers_list))
        with z.open('followers_and_following/following.json') as f:
            raw_following_list = load(f)['relationships_following']
            following_list = list(map(get_account_name, raw_following_list))

    index = 0
    for following in following_list:
        if following not in followers_list:
            print(f'{index} - {following} - https://www.instagram.com/{following}')
            index += 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="Path of the instagram zip file.")
    args = parser.parse_args()
    filepath = Path(args.filepath)

    if filepath.is_file():
        return analyze_zipfile(filepath=filepath)
    else:
        raise FileNotFoundError(f'"{args.filepath}" does not exist.')


if __name__ == '__main__':
    raise SystemExit(main())
