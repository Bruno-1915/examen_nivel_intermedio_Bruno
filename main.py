import logging
import random

import pandas as pd

from config_logging import config_logging
from examen import (apply_function_to_column, filter_and_square,
                       filter_dataframe, flatten_list, generate_regression_data,
                       group_and_aggregate, train_logistic_regression, 
                       train_multiple_linear_regression)

if __name__ == "__main__":
    config_logging(logging.INFO)

    random.seed(0)

    ### Generate regression data
    logging.info(("-" * 20) + " Generate regression data " + ("-" * 20)) #logging header
    X, Y = generate_regression_data(40)
    logging.info(f"Output X:\n{X.tail()}")
    logging.info(f"Output Y:\n{Y.tail()}")

    ### Filter dataframe
    logging.info(("-" * 20) + " Filter dataframe " + ("-" * 20)) #logging header
    logging.info(f"Output:\n{filter_dataframe(X, 'var_a', .5)}")

    ### Train regression model
    logging.info(("-" * 20) + " Train regression model " + ("-" * 20)) #logging header
    model = train_multiple_linear_regression(X, Y)
    logging.info(f"Model: {model}")

    ### Flatten list
    test_a = [[1] * 5, [2] * 5, [3] * 5]
    logging.info(("-" * 20) + " Flatten list " + ("-" * 20)) #logging header
    logging.info(f"Input: {test_a}")
    logging.info(f"Output: {flatten_list(test_a)}")

    ### Group and aggregate
    X['var_c'] = [random.choice([0,1]) for i in range(len(X))] # Adding a categorical column to the data for the grouping
    logging.info(("-" * 20) + " Group and aggregate " + ("-" * 20)) #logging header
    logging.info(f"Output:\n{group_and_aggregate(X, 'var_c', 'var_b')}")
    
    ### Train regression model
    target = pd.Series([random.choice([0,1]) for i in range(len(Y))]) #Creating a binary target for the model
    logging.info(("-" * 20) + " Train logistic model " + ("-" * 20)) #logging header
    model = train_logistic_regression(X, target)
    logging.info(f"Model: {model}")

    ### Apply function to column
    logging.info(("-" * 20) + " Apply function to column  " + ("-" * 20)) #logging header
    logging.info(f"Output:\n{apply_function_to_column(X, 'var_a')}")

    ### Filter and square
    input_square = [random.choice(range(10)) for i in range(10)]
    logging.info(("-" * 20) + " Filter and square  " + ("-" * 20)) #logging header
    logging.info(f"Input: {input_square}")
    logging.info(f"Output: {filter_and_square(input_square)}")

