import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load CSV data from `path`."""
    return pd.read_csv(path)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for cleaning, encoding, scaling."""
    # TODO: implement preprocessing steps
    return df
