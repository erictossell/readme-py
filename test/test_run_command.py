import unittest
from unittest.mock import patch, MagicMock
from app import run_command


class TestReadmeGenerator(unittest.TestCase):
    @patch("app.subprocess.run")
    @patch("app.strip_ansi_sequences")
    def test_run_command(self, mock_strip_ansi, mock_subprocess_run):
        # Set up the mock for subprocess.run
        mock_result = MagicMock()
        mock_result.stdout = "Test Output With ANSI\x1b[31m"
        mock_subprocess_run.return_value = mock_result

        # Set up the mock for strip_ansi_sequences
        mock_strip_ansi.return_value = "Test Output Without ANSI"

        # Call the function
        result = run_command("echo test")

        # Check that subprocess.run was called with the correct command
        mock_subprocess_run.assert_called_with(
            "echo test", shell=True, text=True, capture_output=True
        )

        # Check that strip_ansi_sequences was called with the subprocess output
        mock_strip_ansi.assert_called_with("Test Output With ANSI\x1b[31m")

        # Check the final result
        self.assertEqual(result, "Test Output Without ANSI")


if __name__ == "__main__":
    unittest.main()
