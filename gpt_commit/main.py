import argparse
from typing import List

from ai_model import generate_commit_messages, handle_ai_exception
from utils import get_git_diff, commit_with_message, notify_commit_result

def display_commit_messages(commit_messages: List[str]) -> None:
    for idx, msg in enumerate(commit_messages, start=1):
        print(f"{idx}: {msg}")

def get_user_choice(commit_messages: List[str], allow_edit: bool) -> str:
    user_input = input(f"Enter the number of your preferred commit message{( ', or e to edit' if allow_edit else '')}: ")
    if allow_edit and user_input.lower() == 'e':
        return input("Enter your edited commit message: ")

    choice = int(user_input) - 1
    if 0 <= choice < len(commit_messages):
        return commit_messages[choice]
    else:
        raise ValueError("Invalid choice.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate commit messages with AI.")
    parser.add_argument('--edit', action='store_true', help="Allow editing of generated commit messages.")
    args = parser.parse_args()

    try:
        diff = get_git_diff()
        commit_messages = generate_commit_messages(diff)
    except Exception as e:
        print("An error occurred while generating commit messages:")
        print(handle_ai_exception(e))
        commit_message = input("Please enter a commit message manually: ")
    else:
        print("Generated commit messages:")
        display_commit_messages(commit_messages)
        commit_message = get_user_choice(commit_messages, args.edit)

    result = commit_with_message(commit_message)
    notify_commit_result(result)

if __name__ == '__main__':
    main()
