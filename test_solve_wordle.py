import unittest
from solve_wordle import passes_constraints

class TestConstraintValidation(unittest.TestCase):

    def test_validation(self):
        simple_example = passes_constraints("magic", ["mNoGoGoGrG"])
        self.assertTrue(simple_example)

        # Word is awful, we guessed magic and money and are checking ALPHA
        self.assertTrue(passes_constraints("alpha", ["mGaYgGiGcG", "mGoGnGeGyG"]))
        self.assertFalse(passes_constraints("eerie", ['mGaYgGiGrG']))


if __name__ == "__main__":
    unittest.main()
