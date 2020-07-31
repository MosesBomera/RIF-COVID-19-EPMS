"""
    This script generates synthetic data based on this paper,
    the Makerere COVID-19 survey released on 22/05/2020.

    features    lower_bound upper_bound units
    'age'       16          90          years
    weight      40          200         kgs
    height      110         300         cm
    temperature 34          43          C

    categorical data -> Yes ['1'] or No ['0']
    runny_nose
    fever
    cough
    headache
    muscle_ache
    fatigue

    target -> +/-
"""
import os

import pandas as pd
import numpy as np

def main():
    dg = DataGenerator(rows=10000, seed=42)
    df = pd.DataFrame(dg.generator())
    df.to_csv('covid19.csv', index=False)

class DataGenerator:
    """
        Generates data based on a given distribution.
    """
    def __init__(self, rows, seed):
        self.rows = rows
        self.seed = seed

    def generator(self):
        """
            Return a column of values.
        """
        np.random.seed(self.seed)
        data = [
            {
                'gender': np.random.choice(['M', 'F'], p=[0.68, 0.32]),
                'age': np.random.choice(np.arange(16, 90)),
                'weight': np.random.choice(np.arange(40, 200)),
                'temperature': np.random.choice(np.arange(34, 43)),
                'runny_nose': np.random.choice(['1', '0'], p=[0.161, 0.839]),
                'fever': np.random.choice(['1', '0'], p=[0.214, 0.786]),
                'cough': np.random.choice(['1', '0'], p=[0.196, 0.804]),
                'headache': np.random.choice(['1', '0'], p=[0.125, 0.875]),
                'muscle_ache':np.random.choice(['1', '0'], p=[0.071, 0.929]),
                'fatigue': np.random.choice(['1', '0'], p=[0.071, 0.929]),
                'test': np.random.choice(['1', '0'])
            }
            for _ in range(self.rows)
        ]
        return data


if __name__ == '__main__':
    main()
