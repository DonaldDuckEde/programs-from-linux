import unittest
import pandas as pd
import os
import matplotlib.pyplot as plt

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Create a copy of the test data file
        shutil.copyfile('./data/test.csv', './data/data.csv')

    def tearDown(self):
        # Remove the test data file copy
        os.remove('./data/data.csv')

    def test_changeData(self):
        # Call the function to be tested
        changeData()

        # Check if the expected output file exists
        self.assertTrue(os.path.isfile('./data/data.csv'))

        # Read the output file and check its contents
        df = pd.read_csv('./data/data.csv')
        self.assertEqual(df['id'][0], '1234')
        self.assertEqual(df['Time'][0], '2022-01-01 00:00:00')
        self.assertEqual(df['pm1'][0], 1.23)
        self.assertEqual(df['pm2.5'][0], 2.34)
        self.assertEqual(df['pm4'][0], 3.45)
        self.assertEqual(df['pm10'][0], 4.56)

    def test_getId(self):
        # Capture the console output of the function
        from io import StringIO
        import sys
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        getId()
        sys.stdout = sys.__stdout__

        # Check if the expected console output was produced
        self.assertIn("loading data...", capturedOutput.getvalue())

    def test_main(self):
        # Simulate user input
        from unittest.mock import patch
        with patch('builtins.input', return_value='1234'):
            # Call the function to be tested
            main()

            # Check if the expected plot was produced
            self.assertTrue(plt.gcf().axes)
            self.assertEqual(len(plt.gcf().axes), 1)
            self.assertEqual(len(plt.gcf().axes[0].lines), 4)

if __name__ == '__main__':
    unittest.main()
