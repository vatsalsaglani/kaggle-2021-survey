import pandas as pd
from utils import flatten
from collections import Counter


def counts_from_parts(dataframe, columns: list, to_column_names: list = ['property', 'count']):

    property = flatten(dataframe[columns].values.tolist())
    property = [p for p in property if not pd.isna(p)]
    counts = dict(Counter(property))
    property_counts = [{to_column_names[0]: k, to_column_names[1]: v}
                       for k, v in counts.items()]

    return property_counts, counts


def counts_from_multiple_parts(dataframe, columns: list, condition_column, to_column_names: list = ['property', 'count']):

    unique_cols_df = dataframe[columns]
    unq_cols_set = [v.rstrip().lstrip() for v in list(
        set(flatten(unique_cols_df.values.tolist()))) if not pd.isna(v)]
    condition_unique_dict = {con: {unq: 0 for unq in unq_cols_set}
                             for con in pd.unique(dataframe[condition_column]).tolist()}

    for ix, row in dataframe.iterrows():

        for c in columns:

            if not pd.isna(row[c]):
                condition_unique_dict[row[condition_column]
                                      ][row[c].rstrip().lstrip()] += 1

    return condition_unique_dict
