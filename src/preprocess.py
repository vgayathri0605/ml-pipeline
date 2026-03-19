def preprocess_data(df):
    # remove missing values
    df = df.dropna()

    # split features and target
    X = df.iloc[:, :-1]   # all columns except last
    y = df.iloc[:, -1]    # last column

    return X, y