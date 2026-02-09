import numpy as np
import pandas as pd


def mixed_dtypes_detector(df):
    mixed_dtypes = {}
    for column in df.columns:
        types = df[column].apply(lambda x: type(x).__name__).value_counts()
        if len(types) > 1:
            mixed_dtypes[column] = types.to_dict()
            
    return mixed_dtypes
