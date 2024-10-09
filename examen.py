import logging
from typing import Callable, List, Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

from utils import get_random_number, verify_df_and_columns


def filter_dataframe(df: pd.DataFrame,
                     column: str | float,
                     threshold: float
                     ) -> pd.DataFrame:
    """Filter a dataframe where the values of the specified column are greater than the threshold
    
    Parameters
    ----------
    df : pd.DataFrame
        The data frame which will be filtered
    column : str
        The name of the column that will be use to filter
    threshold: float
        The minimum value of the data to be kept
        
    Returns
    -------
    pd.DataFrame
        The filtered dataframe
    """
    verify_df_and_columns(df, [column])
    return df[df[column] > threshold]

def generate_regression_data(n_samples: int) -> Tuple[pd.DataFrame, pd.Series]:
    """Generate random pandas dataframe and series
    
    Parameters
    ----------
    n_samples : int
        Number of samples to be generated
        
    Returns
    -------
    pd.DataFrame
        Data frame with the independant variables
    pd.Series
        Series with the dependant variables
    """
    a = [(get_random_number(), get_random_number(), get_random_number()) 
            for i in range(n_samples)]
    a = pd.DataFrame(a, columns=['var_a', 'var_b', 'var_c'])
    return a[['var_a', 'var_b']], a['var_c']
    
def train_multiple_linear_regression(X: pd.DataFrame, Y: pd.Series) -> LinearRegression:
    """Generate a linear regression model using the input data
    
    Parameters
    ----------
    X : pd.Dataframe
        Dependent variables
    Y : pd.Dataframe
        Independent variables
        
    Returns
    -------
    LinearRegression
        Trained model
    """
    verify_df_and_columns(X, [])
    X_train, X_test, y_train, y_test = train_test_split( 
        X, Y, test_size=0.2, random_state=0) 
    
    model = LinearRegression()
    model.fit(X_train,y_train)
    logging.info(f"Score on the test set: {model.score(X_test, y_test)}")
    return model

def flatten_list(x: List[List]) -> List:
    """Flatten a list of list into a single list
    
    Parameters
    ----------
    x: list
        The list of list which will be flattened. It can contain nested list but only
        the first level will be flattened
        
    Returns
    -------
    list
        Flattened list at first level
    """
    assert not sum([not isinstance(i, list) for i in x]), f'All the elements in the list must be of type list' 
    ### Without this assertion an string can be unpacked and could lead to unintended behaviour
    return [i for j in x for i in j]

def group_and_aggregate(df: pd.DataFrame, grouper_col: str,
                        aggregate_col: str) -> pd.DataFrame:
    """Group a pandas data frame by a single column and aggregate the values of another column
    
    Parameters
    ----------
    df: pd.DataFrame
        The dataframe to act on
    grouper_col
        The grouper column
    aggregate_col
        The column with values to be aggregated
        
    Returns
    -------
    pd.DataFrame
        The grouped and aggregated column
    """
    verify_df_and_columns(df, [grouper_col, aggregate_col])
    return df.groupby(by=grouper_col)[aggregate_col].aggregate("sum")

def train_logistic_regression(X: pd.DataFrame, Y: pd.Series) -> LogisticRegression:    
    """Generate a logistic regression model using the input data
    
    Parameters
    ----------
    X : pd.Dataframe
        Dependent variables
    Y : pd.Dataframe
        Independent variables
        
    Returns
    -------
    LinearRegression
        Trained model
    """
    verify_df_and_columns(X, [])
    X_train, X_test, y_train, y_test = train_test_split( 
        X, Y, test_size=0.2, random_state=0) 
    
    model = LogisticRegression()
    model.fit(X_train,y_train)
    logging.info(f"Score on the test set: {model.score(X_test, y_test)}")
    return model
    ...

def apply_function_to_column(df: pd.DataFrame, column: str,) -> pd.DataFrame:
    """Apply a custom function to a column of a pandas data frame
    
    Parameters
    ----------
    df: pd.DataFrame
        The dataframe to act on
    column
        The column to act on
        
    Returns
    -------
    pd.DataFrame
        The data frame with the modified column
    """
    verify_df_and_columns(df, [column])
    function = lambda x: 'A' if x < .5 else 'B'
    df[column] = df[column].apply(function)
    return df
    ...

def filter_and_square(numbers: List[float]) -> List[float]:
    """Filter all values less than 5 and square those greater
    
    Parameters
    ----------
    numbers: list
        List of values to be filtered and squared if case
        
    Returns
    -------
    list
        All values greater than 5 squared
    """
    return [i ** 2 for i in numbers if i > 5]
    ...