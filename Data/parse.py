import pandas as pd


def filter_categories(df):
    categories = df.index.get_level_values(0).unique()
    filtered_df = {}
    for i in categories:
        filtered_df[i] = df.iloc[df.index.get_level_values(0) == i, :]
        filtered_df[i].index = filtered_df[i].index.droplevel(0)

    return filtered_df

def filter_years(df):
    years_to_eval = ['18', '19']
    years_filter = {}
    for b in years_to_eval:
        years_filter[b] = df.columns.str.contains(b, regex=False)

    return years_filter


