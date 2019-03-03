#!/usr/bin/env python

import unittest

import sys
sys.path.append('../../bin')

target = __import__('tf_readme_validator')
main = target.main
cfg = target.cfg


class Test1(unittest.TestCase):
    def test(self):
        result = main()
        self.assertEqual(result, 1)
        self.assertEqual('ok' in cfg['readme']['License'], False)
        self.assertEqual('ok' in cfg['readme']['Authors'], False)


if __name__ == '__main__':
    unittest.main()
