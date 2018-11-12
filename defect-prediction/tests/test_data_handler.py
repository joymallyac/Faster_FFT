import os
import sys
import unittest
import pandas as pd
from pathlib import Path
from pdb import set_trace

root = Path(os.path.abspath(os.path.join(
    os.getcwd().split("se4sci")[0], 'se4sci/se4sci')))

if root not in sys.path:
    sys.path.append(str(root))

from data.data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDataHandler, self).__init__(*args, **kwargs)
        self.dh = DataHandler(data_path=root.joinpath("data"))

    def test_get_data(self):
        all_data = self.dh.get_data()
        self.assertIsInstance(all_data, dict)
        for proj, datasets in all_data.items():
            self.assertIsInstance(proj, str)
            self.assertIsInstance(datasets, dict)
            for key, value in datasets.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(value, pd.core.frame.DataFrame)
