#!/usr/bin/python3
import test_matrix
import unittest

if __name__ == "__main__":
	runner = unittest.TextTestRunner(verbosity=3)
	runner.run(unittest.TestLoader().loadTestsFromModule(test_matrix))

