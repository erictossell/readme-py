import unittest
from unittest.mock import patch, MagicMock
import subprocess
from app.readme import run_command


class TestRunCommand(unittest.TestCase):
    @patch("subprocess.run")
    @patch("app.readme.strip_ansi_sequences")
    def test_run_command_success(self, mock_strip_ansi, mock_subprocess_run):
        # Set up mocks
        mock_result = MagicMock(stdout="Test Output With ANSI\x1b[31m")
        mock_subprocess_run.return_value = mock_result
        mock_strip_ansi.return_value = "Test Output Without ANSI"

        # Test the successful execution path
        result = run_command(["echo", "test"])
        mock_subprocess_run.assert_called_with(
            ["echo", "test"], text=True, capture_output=True, check=True
        )
        mock_strip_ansi.assert_called_with("Test Output With ANSI\x1b[31m")
        self.assertEqual(result, "Test Output Without ANSI")

    @patch("subprocess.run")
    def test_run_command_failure(self, mock_subprocess_run):
        # Set up the mock to simulate a command failure
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(
            1, ["echo", "test"], "Error Message"
        )

        # Test the failure execution path
        result = run_command(["echo", "test"])
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
