
import pandas as pd

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    df = df.asfreq('D')
    df['sales'] = df['sales'].fillna(method='ffill')
    return df
