import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from unittest.mock import MagicMock, patch
from gpt_commit.ai_model import generate_commit_messages, handle_ai_exception, DummyAIModel

class TestAIModel(unittest.TestCase):

    def test_generate_commit_messages(self):
        dummy_diff = "This is a dummy git diff."
        dummy_messages = [
            "Update README.md",
            "Fix a bug in the main function",
            "Refactor code for better readability",
            "Add new feature to the application"
        ]

        with patch('gpt_commit.ai_model.DummyAIModel.generate_messages', return_value=dummy_messages):

            result = generate_commit_messages(dummy_diff)
            self.assertEqual(result, dummy_messages)

    def test_handle_ai_exception(self):
        error_msg = "An error occurred while generating commit messages: AI model failed."
        exception = RuntimeError("AI model failed.")
        result = handle_ai_exception(exception)
        self.assertEqual(result, error_msg)

if __name__ == '__main__':
    unittest.main()
