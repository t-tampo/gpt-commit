import random
from typing import List

class DummyAIModel:
    # このクラスは、ダミーのAIモデルを示しています。適切なAIモデルに置き換えてください。

    def generate_messages(self, diff: str) -> List[str]:
        dummy_messages = [
            "Update README.md",
            "Fix a bug in the main function",
            "Refactor code for better readability",
            "Add new feature to the application"
        ]
        return random.sample(dummy_messages, len(dummy_messages))

def generate_commit_messages(diff: str) -> List[str]:
    ai_model = DummyAIModel()
    try:
        commit_messages = ai_model.generate_messages(diff)
    except Exception as e:
        raise e
    return commit_messages

def handle_ai_exception(e: Exception) -> str:
    error_message = f"An error occurred while generating commit messages: {str(e)}"
    return error_message
