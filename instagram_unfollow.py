import argparse
import zipfile
from json import load
from pathlib import Path
from typing import Any, Dict, List


def formatting(name: str, index: int) -> str:
    return f'{index} - {name} - https://www.instagram.com/{name}'


def get_list(raw_list: List[Dict[str, Any]]) -> List[str]:
    new_list = []
    for entry in raw_list:
        try:
            new_list.append(entry['string_list_data'][0]['value'])
        except KeyError or IndexError:
            print('Error while parsing:', entry)
    return new_list


def main(filepath: str):
    with zipfile.ZipFile(filepath) as z:
        with z.open('followers_and_following/followers.json') as f:
            raw_followers_list = load(f)['relationships_followers']
            followers_list = get_list(raw_list=raw_followers_list)
        with z.open('followers_and_following/following.json') as f:
            raw_following_list = load(f)['relationships_following']
            following_list = get_list(raw_list=raw_following_list)

    index = 0
    for following in following_list:
        if following not in followers_list:
            print(formatting(name=following, index=index))
            index += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="Path of the instagram zip file.")
    args = parser.parse_args()
    filepath = Path(args.filepath)

    if filepath.is_file():
        main(filepath=filepath)
    else:
        raise FileNotFoundError(f'"{args.filepath}" does not exist.')
