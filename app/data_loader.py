import pandas as pd


def load_supplier_data(file_path: str) -> pd.DataFrame:
    """
    Load supplier performance data from CSV.
    """
    return pd.read_csv(file_path)
