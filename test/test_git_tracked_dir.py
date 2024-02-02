import unittest
from unittest.mock import patch, MagicMock
from app.readme import git_tracked_directories


class TestGitTrackedDirectories(unittest.TestCase):
    @patch("app.readme.subprocess.run")
    def test_git_tracked_directories_excludes_hidden(self, mock_subprocess_run):
        # Prepare the mock output to simulate the command's stdout
        mock_output = "folder1/file1.txt\nfolder2/.hidden/file2.txt\nfolder2/file3.txt"
        mock_subprocess_run.return_value = MagicMock(stdout=mock_output)

        # Execute the function with a mocked base path
        result = git_tracked_directories("/mock/base/path")

        # Assert subprocess.run was called with expected arguments
        mock_subprocess_run.assert_called_once_with(
            ["git", "ls-tree", "-r", "--name-only", "HEAD"],
            cwd="/mock/base/path",
            text=True,
            capture_output=True,
        )

        # Assert the function's output matches expected directories, excluding hidden ones
        expected_directories = sorted({"folder1", "folder2"})
        self.assertListEqual(result, expected_directories)


if __name__ == "__main__":
    unittest.main()
