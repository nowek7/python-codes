#!/bin/python3

import os
import sys
from typing import Iterable, Iterator
import re

SKIPPED_DIRS = frozenset(('.git', '.vscode'))


def skipped_dir(dir: list) -> bool:
    for skip_dir in SKIPPED_DIRS:
        if skip_dir in dir:
            return True

    return False


def skip_files(paths: Iterable) -> bool:
    return filter(lambda name: name.endswith('.tex'), paths)


def find_tex_files() -> Iterator[str]:
    for root, dirs, files in os.walk('.'):
        if skipped_dir(root):
            continue

        filtered_names = skip_files(files)
        for name in filtered_names:
            yield os.path.join(root, name)


def replace_double_dollars(path: str) -> None:
    with open(path, 'r+', encoding='utf-8') as tex_file:
        content = tex_file.read()

        # Trailing whitespaces.
        content = content.strip()

        tex_file.seek(0)

        # Find and replace double dollars.
        regex = r'(\$\$)([^\$]*)(\$\$)'
        content = re.sub(regex, r'\[ \2 \]', content)

        tex_file.write(content)
        tex_file.truncate()


if __name__ == '__main__':
    for tex_file in find_tex_files():
        print(f'Replaced double dollars in {tex_file}')
        try:
            replace_double_dollars(tex_file)
            print(f'Replaced double dollars in {tex_file}')
        except UnicodeDecodeError as error:
            print(f'{tex_file} -> {str(error)}')
