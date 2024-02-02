# test_readme_generator.py
import unittest
from app.readme import strip_ansi_sequences


class TestReadmeGenerator(unittest.TestCase):
    def test_strip_ansi_sequences(self):
        # Example ANSI escape sequence string
        ansi_string = "\x1b[31mThis is a test.\x1b[0m"
        expected_result = "This is a test."

        # Call the function and check if it returns the expected result
        result = strip_ansi_sequences(ansi_string)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
