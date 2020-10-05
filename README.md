# PandasFundamentals
This repository includes a few examples of dataset manipulation using Pandas. The fundamentals delineated in this repository serve as a benchmark for future projects. This README includes a concatenation of all of the useful functions used in each sub-directory.

*TODO: Table of contents*

#### Data Importing:
- pd.read_csv(global_consts.year_dataset, names=["name", "sex", "births"]) - imports .csv file as DataFrame object

*More DataFrame construction examples are shown below*

#### Data Exploration:
- df.describe() - get summary stats for the data
- df.shape - returns shape of dataframe
- df.columns - returns columns of dataframe

#### Histogram Plotting:
- df[[column_name]].hist() - plots a histogram of the selected column
- df.hist() - plots a histogram of the entire dataset by plotting a histogram for each column

#### Series Objects:
- s = pd.Series(np.random.randn(5), index=['a','b','c','d','e']) - creates a Series from an ndarray
- Series objects are very similar to ndarrays
	- s[0], s[:3], s['a'], s.get('a') all possible

#### DataFrame Objects:
- df.index - returns useful info about the DataFrame
- df.columns - returns column information
- df.pivot(index, columns, values) - pivots the DataFrame by adding a new column for each unique value specified in the columns argument
- df.describe(percentiles, include, exclude) - generates various summary statistics, excluding NaN values


#### Creating Pandas DataFrames:
You can create a Pandas DataFrame in several different ways. A few simple methods of creating Pandas DataFrames are included in customer.py:

**Without indices from simple lists:**

```python
my_first_series = pd.Series([0, 2, 3, 4, 1])
my_second_series = pd.Series([1, 4, 3, 5, 5, 9])
custom_dataframe_dict = {"col_1": my_first_series, "col_2": my_second_series}
return pd.DataFrame(custom_dataframe_dict)
```

**Data indexed from lists**

```python
full_index_array = ["a", "b", "c", "d", "e", "f", "g"]
col_1 = pd.Series([48, 4, 1, 4, 5, 6, 4], index=full_index_array)
col_2 = pd.Series(np.random.randn(7), index=full_index_array)
col_3 = pd.Series(np.random.randn(6), index=full_index_array[:-1])

dataframe_dict = {"col_1": col_1, "col_2": col_2, "col_3":col_3}
return pd.DataFrame(dataframe_dict)
```

**From numpy 2-dimensional arrays**

```python
column_names = customer_column_names
return  pd.DataFrame(np_array, columns=column_names)
```

#### Data Indexing:
- df[:10], df.head(10) - selects the first 10 rows of the df
- df.tail(10) - selects the last 10 elements of the df
- df[column_name] - returns a df object with only the specified column
- df[[column_name_list]] - returns a df object with only the specified columns
- df.loc[[row_conditions_list]] - returns the rows of df with the row conditions
- df.loc[[row_conditions_list], [column_list]] - simultaneously selects the rows with the specified conditions and the columns specified in the column list

*df.loc example:*  
```python
selected_rows = df.loc[["Avery Bradley", "Jae Crowder"], ["Team", "Age"]]
```

- df.iloc[row_index] - returns the row with the specified row index
- df.iloc[[row_indices]] - returns the rows specified by the row indices list
- df.iloc[[row_indices], [col_indices]] - returns the rows specified by the row indices list and the columns specified by the column indices list



#### Conditional Indexing:
- df[condition] - returns the rows of df that satisfy the condition

*df[condition] example:*

```python
males = df[df['sex'] == "M"]
```

#### Sorting:
- df = df.sort_values([column_list], ascending=[True]) - sorts the df according to the columns in the column list

#### .groupby & Element-Wise Modification:
- df.groupby([column_name]) - groups the rows of the df according to the specified column name and returns a GroupBy object. An aggregation rule can then be specified on the un-aggregated GroupBy object

*simple .groupby summing example:*

```python
grouped_rows = df.groupby(['sex']).sum()
```

*un-aggregated .groupby example:*
```python
def modifier(dataframe):
    # We have access to the entire DataFrame object here
    ... 
    return dataframe
g = df.groupby(['sex'])
g = g.apply(modifier)
```

- Series.map - map values of Series according to input correspondence. 

*.map lambda example:*
```python
df['income_category'] = df['annual_income'].map(lambda x: 1 if x>30000 else 0)
```

*.map specified function example:*
```python
def modifier(value):
    if value > 3000:
        return 1
    else:
        return 0
df['income_category'] = df['annual_income'].map(modifier)
```

#### String Indexing:
- string_column.str - allows us to access and modify the string contents of the string column
 
 *string indexing example:*
 ```python
names = df.names
# The following will give us all a column of the first letters of the names
first_letters = names.str[0]
```

#### Plotting:
*Pandas plotting example:*
dataframe['first_letters'] = dataframe['name'].str[0]
```python
df.plot(kind='bar', x=x_column, y=y_column, color=desired_color, title=desired_title, xlabel=desired_xlabel, ylabel=desired_ylabel)
plt.savefig(save_location)
```