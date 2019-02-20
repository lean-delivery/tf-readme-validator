#!/usr/bin/env python

import unittest

import sys
sys.path.append('../../bin')

target = __import__('tf_readme_validator')
main = target.main
structure = target.structure


class Test1(unittest.TestCase):
    def test(self):
        result = main()
        self.assertEqual(result, 1)
        self.assertEqual('ok' in structure['readme']['License'], False)
        self.assertEqual('ok' in structure['readme']['Tests'], False)
        self.assertEqual('ok' in structure['readme']['Authors'], False)


if __name__ == '__main__':
    unittest.main()
