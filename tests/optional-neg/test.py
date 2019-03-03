#!/usr/bin/env python

import unittest

import sys
sys.path.append('../../bin')

target = __import__('tf_readme_validator')
main = target.main
readme = target.cfg['readme']


class Test1(unittest.TestCase):
    def test(self):
        result = main()
        self.assertEqual(result, 1)
        self.assertEqual('ok' in readme['Conditional creation'], False)
        self.assertEqual('ok' in readme['Code included in this module'], False)
        self.assertEqual('ok' in readme['Known issues / Limitations'], False)
        self.assertEqual('ok' in readme['Tests'], False)
        self.assertEqual('ok' in readme['Examples'], False)


if __name__ == '__main__':
    unittest.main()
