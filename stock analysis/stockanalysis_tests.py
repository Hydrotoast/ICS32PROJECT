import unittest
from stockanalysis_indicators import SimpleMovingAverageIndicator

class SimpleMovingAverageIndicatorTest(unittest.TestCase):
    def testEmpty(self):
        indicator = SimpleMovingAverageIndicator(3);
        self.assertEqual([], 
                          indicator.execute([]))
        self.assertEqual([], 
                          indicator.execute([(1, 0, 0), (2, 0, 0)]))

    def testBasic(self):
        indicator = SimpleMovingAverageIndicator(3);
        self.assertEqual([2], 
                          indicator.execute([(1, 0, 0), (2, 0, 0), (3, 0, 0)]))
        self.assertEqual(list(reversed([2, 3])), 
                          indicator.execute([(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0)]))

def main():
    unittest.main();

if __name__ == '__main__':
    main()
