import argparse

from gpt_commit.ai_model import generate_commit_message, handle_ai_exception
from gpt_commit.utils import get_git_diff, commit_with_message, notify_commit_result

def display_commit_message(commit_message: str) -> None:
    print(f"Generated commit message: {commit_message}")

def get_user_choice(commit_message: str, allow_edit: bool) -> str:
    user_input = input(f"Enter 'c' to use the generated commit message, or 'e' to edit it: ").lower()
    if allow_edit and user_input == 'e':
        return input("Enter your edited commit message: ")
    elif user_input == 'c':
        return commit_message
    else:
        raise ValueError("Invalid choice.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a commit message with AI.")
    parser.add_argument('--edit', action='store_true', help="Allow editing of the generated commit message.")
    args = parser.parse_args()

    try:
        diff = get_git_diff()
        commit_message = generate_commit_message(diff)
    except Exception as e:
        print("An error occurred while generating the commit message:")
        print(handle_ai_exception(e))
        commit_message = input("Please enter a commit message manually: ")
    else:
        display_commit_message(commit_message)
        if args.edit:
            commit_message = get_user_choice(commit_message, True)

    result = commit_with_message(commit_message)
    notify_commit_result(result)

if __name__ == '__main__':
    main()
