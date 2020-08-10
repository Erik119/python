import unittest
import ams.ams


class MyTestCase(unittest.TestCase):

    def test_time_to_collect(self):
        self.collect_interval = 15
        self.assertEqual(time_to_collect(15), True)


if __name__ == '__main__':
    unittest.main()
