import subprocess
from typing import Tuple

class GitUtils:
    @staticmethod
    def get_git_diff() -> str:
        """現在の作業ディレクトリのGit diffを取得する

        :return: Git diff 文字列
        """
        try:
            diff = subprocess.check_output(['git', 'diff']).decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise e
        return diff

    @staticmethod
    def commit_with_message(commit_message: str) -> Tuple[bool, str]:
        """指定されたコミットメッセージでGitコミットを実行する

        :param commit_message: コミットメッセージ
        :return: 成功したかどうかの真偽値と、結果メッセージのタプル
        """
        try:
            subprocess.check_output(['git', 'commit', '-am', commit_message])
        except subprocess.CalledProcessError as e:
            return False, str(e)
        return True, "Commit successful."

    @staticmethod
    def notify_commit_result(result: Tuple[bool, str]) -> None:
        """コミット結果を表示する

        :param result: コミット結果のタプル (成功したかどうかの真偽値, 結果メッセージ)
        """
        success, message = result
        if success:
            print("Commit successful.")
        else:
            print("Commit failed:")
            print(message)
