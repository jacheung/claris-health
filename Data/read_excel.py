import pandas as pd


def import_df():

    df = pd.read_excel('/Users/jonathancheung/Dropbox/Claris/Raw/KPI_Jan2020.xlsx', header=[0])
    df.set_index(list(df.columns[[0, 1]]), inplace=True)

    return df

