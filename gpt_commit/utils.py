import os
import subprocess
from typing import Tuple

def get_git_diff() -> str:
    try:
        diff = subprocess.check_output(['git', 'diff']).decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise e
    return diff

def commit_with_message(commit_message: str) -> Tuple[bool, str]:
    try:
        subprocess.check_output(['git', 'commit', '-am', commit_message])
    except subprocess.CalledProcessError as e:
        return False, str(e)
    return True, "Commit successful."

def notify_commit_result(result: Tuple[bool, str]) -> None:
    success, message = result
    if success:
        print("Commit successful.")
    else:
        print("Commit failed:")
        print(message)
