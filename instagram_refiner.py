import argparse
import zipfile
from json import load
from pathlib import Path
from typing import Any, Dict, List


def format_output(name: str, index: int) -> str:
    return f'{index} - {name} - https://www.instagram.com/{name}'


def parse_raw_list(raw_list: List[Dict[str, Any]]) -> List[str]:
    new_list = []
    for entry in raw_list:
        try:
            new_list.append(entry['string_list_data'][0]['value'])
        except KeyError or IndexError:
            print(f'Error while parsing "{entry}"')
    return new_list


def analyze_zipfile(filepath: str) -> int:
    with zipfile.ZipFile(filepath) as z:
        with z.open('followers_and_following/followers.json') as f:
            raw_followers_list = load(f)['relationships_followers']
            followers_list = parse_raw_list(raw_list=raw_followers_list)
        with z.open('followers_and_following/following.json') as f:
            raw_following_list = load(f)['relationships_following']
            following_list = parse_raw_list(raw_list=raw_following_list)

    index = 0
    for following in following_list:
        if following not in followers_list:
            print(format_output(name=following, index=index))
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
