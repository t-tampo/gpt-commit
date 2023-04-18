import io
import unittest
from unittest.mock import patch
from typing import List
from gpt_commit.main import display_commit_messages, get_user_choice

class TestMain(unittest.TestCase):

    def test_display_commit_messages(self):
        commit_messages = [
            "Update README.md",
            "Fix a bug in the main function",
            "Refactor code for better readability",
            "Add new feature to the application"
        ]
        expected_output = "1: Update README.md\n2: Fix a bug in the main function\n3: Refactor code for better readability\n4: Add new feature to the application\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            display_commit_messages(commit_messages)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_get_user_choice(self):
        commit_messages = [
            "Update README.md",
            "Fix a bug in the main function",
            "Refactor code for better readability",
            "Add new feature to the application"
        ]
        user_input = '2'

        with patch('builtins.input', return_value=user_input):
            chosen_message = get_user_choice(commit_messages, allow_edit=False)
            self.assertEqual(chosen_message, commit_messages[int(user_input) - 1])

if __name__ == '__main__':
    unittest.main()
