import unittest
from unittest.mock import patch, MagicMock
from app import git_tracked_directories


class TestReadmeGenerator(unittest.TestCase):
    @patch("app.subprocess.run")
    def test_git_tracked_directories(self, mock_subprocess_run):
        # Mock subprocess.run to simulate Git command output
        mock_output = "folder1/file1.txt\nfolder2/.hidden/file2.txt\nfolder2/file3.txt"
        mock_result = MagicMock()
        mock_result.stdout = mock_output
        mock_subprocess_run.return_value = mock_result

        # Call the function with a mock base path
        result = git_tracked_directories("/mock/base/path")

        # Verify that subprocess.run was called correctly
        mock_subprocess_run.assert_called_with(
            ["git", "ls-tree", "-r", "--name-only", "HEAD"],
            cwd="/mock/base/path",
            text=True,
            capture_output=True,
        )

        # Verify the result
        expected_directories = ["folder1", "folder2"]
        self.assertEqual(result, expected_directories)


if __name__ == "__main__":
    unittest.main()
