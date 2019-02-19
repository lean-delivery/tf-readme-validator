#!/usr/bin/env python

import unittest

import sys
sys.path.append('../..')

target = __import__('tf_readme_validator')
main = target.main


class Test1(unittest.TestCase):
    def test(self):
        result = main()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
