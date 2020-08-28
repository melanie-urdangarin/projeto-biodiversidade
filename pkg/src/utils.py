
import pandas as pd
import re

def select_columns(data, columns_list):
    clean = data[columns_list].astype(str)

    result = [clean.columns.tolist()]
    [result.append(clean.iloc[i].values.tolist()) for i in range(clean.shape[0])]

    return result


def filter_rows(data, column, value):
    clean = data[data[column] == value].astype(str)

    result = [data.columns.tolist()]
    [result.append(clean.iloc[i].tolist()) for i in range(clean.shape[0])]

    return result


# def filter_rows_pattern(data, column, pattern):
#     clean = data.astype(str)
#     result = [clean.columns.tolist()]

#     for i in range(len(clean)):
#         if bool(re.search(pattern, clean[column][i])):
#             result.append(clean.iloc[i].tolist())

#     return result
