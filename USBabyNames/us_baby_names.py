import pandas as pd
import matplotlib.pyplot as plt
from PandasFundamentals.USBabyNames.consts import *


# Goals:
# 1. Add a column that includes the proportion of each birth count
# 2. Extract a subset of the data with the top 10 names for each sex
# 3. Aggregate the names by first letter and plot the frequency distribution for males and females separately

def import_yob_dataset_pandas():
    # Each entry in the following dataset is a name, the sex of that name, and the number of children born in 2010
    # that were given that particular name
    return pd.read_csv(paths.year_dataset, names=["name", "sex", "births"])


# Adds a column that includes the proportion of each birth count
# Uses unaugmented .groupby followed by .apply
def augment_birth_prop(dataframe):
    g = dataframe.groupby('sex')

    def augment_prop(df):
        births = df.births
        prop = births / births.sum()
        df['prop'] = prop
        return df

    dataframe = g.apply(augment_prop)

    return dataframe


def extract_top_10(dataframe):
    males = dataframe[dataframe['sex'] == "M"]
    females = dataframe[dataframe['sex'] == "F"]

    top_males = males.sort_values(['births'], ascending=False).head(10)
    top_females = females.sort_values(['births'], ascending=False).head(10)

    return top_males, top_females


def plot_first_letter_frequency(dataframe):
    dataframe['first_letters'] = dataframe['name'].str[0]

    males = dataframe[dataframe['sex'] == "M"]
    females = dataframe[dataframe['sex'] == "F"]

    males = males.groupby(['first_letters'], as_index=False).agg('sum')
    females = females.groupby(['first_letters'], as_index=False).agg('sum')

    males.plot(kind='bar', x='first_letters', y='births', color='blue', title='Males Births by First Letter',
               xlabel='First Letters', ylabel="Births")
    plt.xticks(rotation=0)
    plt.savefig(paths.results_dir + "first_letters_male.png")
    females.plot(kind='bar', x='first_letters', y='births', color='blue', title='Females Births by First Letter',
                 xlabel='First Letters', ylabel="Births")
    plt.xticks(rotation=0)
    plt.savefig(paths.results_dir + "first_letters_female.png")
    return


if __name__ == "__main__":
    yob_dataset = import_yob_dataset_pandas()

    augmented_dataframe = augment_birth_prop(yob_dataset)

    top_males, top_females = extract_top_10(yob_dataset)

    plot_first_letter_frequency(yob_dataset)
