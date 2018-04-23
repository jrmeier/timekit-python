import unittest
import sys
from . import suite

result = unittest.TextTestRunner(verbosity=2).run(suite())

if result.errors or result.failures:
    sys.exit(1)
