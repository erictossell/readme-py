import unittest

if __name__ == "__main__":
    unittest.main(
        argv=["first-arg-is-ignored"],
        exit=False,
        module=None,
        testRunner=unittest.TextTestRunner(verbosity=2),
        start_dir="test",
        pattern="test*.py",
    )
