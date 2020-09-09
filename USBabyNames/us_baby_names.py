import pandas as pd
import numpy as np
from PandasFundamentals.USBabyNames.consts import *

def import_yob_dataset_pandas():
    return pd.read_csv(paths.year_dataset, names=["name", "sex", "births"])

if __name__ == "__main__":
    print("__main__")

    yob_dataset = import_yob_dataset_pandas()
    