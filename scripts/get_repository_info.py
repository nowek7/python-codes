from datetime import datetime
import json
import subprocess

if __name__ == '__main__':
    repository_info = {
        'buildDate': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'gitBranch': subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode("utf8")[0:-1],
        'gitDate': subprocess.check_output(['git', 'log', '-1', '--date=iso8601-strict', "--pretty=format:%cd"]).decode("utf8")[0:-1],
        'gitHash': subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode("utf8")[0:-1],
        'gitTag': subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode('utf8')[0:-1]
    }

    with open('../generated/repoInfo.json', 'w', encoding='utf-8') as file:
        json.dump(repository_info, file, ensure_ascii=False, indent=2)