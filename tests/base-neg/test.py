#!/usr/bin/env python

import unittest

import sys
sys.path.append('../..')

target = __import__('tf_readme_validator')
main = target.main
readme = target.structure['readme']


class Test1(unittest.TestCase):
    def test(self):
        result = main()
        self.assertEqual(result, 1)
        self.assertEqual('ok' in readme['Description'], False)
        self.assertEqual('ok' in readme['Conditional creation'], False)
        self.assertEqual(readme['Terraform versions']['ok'], False)
        self.assertEqual(readme['inputs table']['ok'], False)
        self.assertEqual(readme['outputs table']['ok'], False)


if __name__ == '__main__':
    unittest.main()
