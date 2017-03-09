import pandas as pd
import numpy as np

# as discussed in the exploratory data analysis,
# we want to remove some data from our model because
# it looks like there has been some kind of mistake.

def clean_sales_dataframe(sales_df):

    # we had a couple values in the dataset that looked odd
    sales_df1 = sales_df[sales_df.QTY_ORDER < 200]

    return sales_df1

def clean_competitor_dataframe(comp_df):

    # all data on this day was unusually large
    comp_df1 = comp_df[comp_df.DATE_EXTRACTION < '2015-10-14 00:00:00']

    return comp_df1