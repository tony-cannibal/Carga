
def trim_auto(df):
    columns = [2, 8, 9, 21, 22]
    df.drop(df.columns[columns], axis=1, inplace=True)
    df = df.fillna('')
    return df
