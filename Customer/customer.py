import pandas as pd
import numpy as np
from global_consts import global_consts
from PandasFundamentals.Customer.consts import paths

customer_column_names = ["custid", "gender", "age", "age_cat",	"debtinc", "card", "carditems", "cardspent", "cardtype","creddebt", "commute", "commutetime", "card2", "card2items", "card2spent", "card2type", "marital", "homeown", "hometype", "cars", "carown", "region",	"ed_cat", "ed_years", "job_cat", "employ_years", "emp_cat", "retire", "annual_income", "inc_cat"]

def import_customer_dataset():
    # Each entry in the following dataset is a name, the sex of that name, and the number of children born in 2010
    # that were given that particular name
    return pd.read_csv(global_consts.customer_dataset, names=customer_column_names)

def import_customer_dataset_numpy():
    return np.array(import_customer_dataset())

def create_no_index_custom_dataframe():
    # The series that you use to create the columns of the dataframe need not be equal in size. Size mismatches just result in NaN occurring in places where certain entries were expected

    # Creating your own dataframe example (no indices):
    my_first_series = pd.Series([0, 2, 3, 4, 1])
    my_second_series = pd.Series([1, 4, 3, 5, 5, 9])
    custom_dataframe_dict = {"col_1": my_first_series, "col_2": my_second_series}
    return pd.DataFrame(custom_dataframe_dict)

def create_indexed_custom_dataframe():
    full_index_array = ["a", "b", "c", "d", "e", "f", "g"]
    col_1 = pd.Series([48, 4, 1, 4, 5, 6, 4], index=full_index_array)
    col_2 = pd.Series(np.random.randn(7), index=full_index_array)
    col_3 = pd.Series(np.random.randn(6), index=full_index_array[:-1])

    dataframe_dict = {"col_1": col_1, "col_2": col_2, "col_3":col_3}
    return pd.DataFrame(dataframe_dict)

def create_dataframe_from_np(np_array):
    column_names = customer_column_names
    return pd.DataFrame(np_array, columns=column_names)

if __name__ == "__main__":
    df = import_customer_dataset()

    # Customer Categorization:
    # Create a column that categorizes customers according to 5 income brackets
    print(df.columns)
    print(df["annual_income"].describe())
    print(df["inc_cat"].describe())

    print(df[["annual_income", "inc_cat"]][:10])
    df["annual_income"] = pd.Series(df["annual_income"], dtype=float)

    min = float(df["annual_income"][1:].min())
    max = float(df["annual_income"][1:].max())
    mean = pd.Series(df["annual_income"][1:], dtype=float).mean()

    categories = ["lowest", "low", "mid", "high", "highest"]
    tier_range = (max - min) / len(categories)

    for element in df["annual_income"][1:]:
        if element is not float:
            print("WOAH")
            #PROBLEM: Can't remove string values from annual_income column. Not sure why but pd.Series( , dtype=float) doesn't work.

    def rule(df):
        annual_income = df["annual_income"]
        df["new_cat"] = pd.Series(np.zeros((df.shape[0], )), dtype=float)

        df[df["annual_income"] < 40000]["new_cat"] = 1
        return df

    g = df.groupby([customer_column_names[1]])
    df = g.apply(rule)

    # Histogram Plotting:
    # Plot a histogram of the income brackets of the customers


    print("Program End")