import pandas as pd


def data_wrangling(filename):
    json_file = filename
    df = pd.read_json(json_file)

    new_df = df.dropna()

    df = new_df.to_dict('records')

    return df
