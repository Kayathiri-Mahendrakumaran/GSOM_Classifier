import pandas as pd
import numpy as np

class InputParser:

    @staticmethod
    def parse_input_zoo_data(filename):
        df = pd.read_csv(filename)
        X = np.asarray(df.iloc[:, :-1].values)
        y = np.asarray(df.iloc[:, -1].values)
        classes = y.tolist()
        return X, classes
