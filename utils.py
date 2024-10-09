from typing import Tuple

from faker import Faker
from pandas import DataFrame

Faker.seed(0)
fake = Faker()

def get_random_number() -> float:
    """Get a random number using the flake package
    
    Parameters
    ----------
        
    Returns
    -------
    float
        A random number greater than zero and almost lower to 1
    """
    return fake.random_number(digits=10) / 9e9

def verify_df_and_columns(df: DataFrame, columns: Tuple[str]) -> None:
    """Verify that the df parameter is really a pd.DataFrame and the columns passed are in it
    
    Parameters
    ----------
    df: pd.DataFrame
        The object to be evaluated as data frame
    columns: list
        The columns to check that are in the data frame
    Returns
    -------
    None
        If all is correct it returns None otherwise it raise an assertion error
    """
    
    assert isinstance(df, DataFrame), f'The df argument must be a pandas dataframe but is {type(df)}'
    for column in columns:
        assert column in df.columns, f'The column specified ({column}) is not in df columns {df.columns.to_list()}'