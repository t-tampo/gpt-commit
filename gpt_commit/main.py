import argparse

from gpt_commit.ai_model import generate_commit_message, handle_ai_exception
from gpt_commit.utils import GitUtils
from termcolor import colored

def display_commit_message(commit_message: str) -> None:
    colored_message = colored(f"\nGenerated commit message: {commit_message}", 'green')
    print(colored_message)

def get_user_choice(commit_message: str, allow_edit: bool) -> str:
    print("Review the generated commit message...")
    user_input = input("Enter 'c' to confirm and use the generated commit message, 'e' to edit the message, or 'q' to quit the program: ").lower()

    if allow_edit and user_input == 'e':
        return input("Enter your edited commit message: ")
    elif user_input == 'c':
        return commit_message
    elif user_input == 'q':
        print("Exiting the program...")
        exit(0)
    else:
        raise ValueError("Invalid choice.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a commit message with AI.")
    parser.add_argument('--no-edit', action='store_true', help="Disable editing of the generated commit message.")
    args = parser.parse_args()

    try:
        print("Getting git diff...")
        diff = GitUtils.get_git_diff()
        
        if not diff:
            print("No changes to commit.")
            exit(0)

        print("Generating commit message using AI...")
        commit_message = generate_commit_message(diff)

    except Exception as e:
        print("An error occurred while generating the commit message:")
        print(handle_ai_exception(e))
        commit_message = input("Please enter a commit message manually: ")

    else:
        display_commit_message(commit_message)

        if not args.no_edit:
            commit_message = get_user_choice(commit_message, True)

    print("Committing with the chosen message...")
    result = GitUtils.commit_with_message(commit_message)
    print("Notifying the commit result...")
    GitUtils.notify_commit_result(result)

if __name__ == '__main__':
    main()
