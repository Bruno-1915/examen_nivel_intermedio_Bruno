# examen_nivel_intermedio_Bruno

All the functions are covered in the main.py script.

Before run ensure you have the requirements installed, you can do so with the following command.

```
pip install -r requirements.txt
```

Once this has done the script can be run with the following command.

```
python3 main.py
```

The main.py script runs the following functions:

- filter_dataframe:
    This function filter a data frame using the ability of a pandas series to compare a series with a value returning a bool series which then will be passed to the data frame selector to get only the truth values of the previous comparison.

- generate_regression_data:
    Using list comprehension a data frame with 3 columns and n_samples rows is created.
    After that the first two are selected as the independant variables and the third one as the dependant varialble.

- train_multiple_linear_regression:
    First the X and Y variables are splitted on train and test sets by a proportion of 80% - 20%.
    Then a linear regression is trained with the train set and a score is calculated on the test set.

- flatten_list:
    Here a list of lists is unpacked using double list comprehension.

- group_and_aggregate:
    With this function a data frame column is summed using another (or same) column as criteria to group the values.

- train_logistic_regression:
    Same as in train multiple_linear_regression but with a logistic regression.

- apply_function_to_column:
    Using this function a column of a data frame is modified with a fixed function.

- filter_and_square:
    With list comprehension the values of a list are discarded by a condition and the remaining are returned squared.