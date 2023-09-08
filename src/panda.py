import os
import faker
import random
import numpy as np
import pandas as pd

term_size: int = os.get_terminal_size()

base_data = pd.DataFrame({
    'id': pd.Series([1, 2, 3, 4, 5]),
    'fname': pd.Series(['Gaurav', 'Tripti', 'Bhavil', 'Yashu', 'Mohit']),
    'lname': pd.Series(['J', 'K', 'L', 'M', 'N']),
    'email': pd.Series(['gaurav.j@email.com','tripti.k@email.com', 'bhavil.l@email.com', 'yashu.m@email.com', 'mohit.n@email.com']),
    'mobile': pd.Series([9167945576,9977942345,9834945876,9768943546,9146789086])
})

fake_data = faker.Faker()
data = {"id": [], "fname": [], "lname": [], "email": [], "mobile": []}
for _ in range(20): # increase the range to generate more records
    data["id"].append(fake_data.random_int(min=6)) # or simply use range(6, 106)
    data["fname"].append(fake_data.first_name())
    data["lname"].append(fake_data.last_name())
    data["email"].append(fake_data.email())
    data["mobile"].append(fake_data.phone_number()[:10])

data = pd.DataFrame(data)
data = pd.concat([base_data, data, data, data])

# Data Transformation - create sales data:
sales_data = {"year": [], "month": [], "sales": [], "expenses": []}
for _ in range(500): # increase the range to generate more records
    sales_data["year"].append(random.randint(1999, 2022)) # or simply use range(6, 106)
    sales_data["month"].append(random.choice(['Jan', 'Mar', 'Dec']))
    sales_data["sales"].append(fake_data.random_int())
    sales_data["expenses"].append(fake_data.random_int())
sales_data = pd.DataFrame(sales_data)


if '__main__' == __name__:
    # Read data from a CSV file
    data_dup = pd.read_csv('./data/data.csv')
    if not data.empty:
        console_half = int(term_size.columns/2)
        print('_' * term_size.columns)
        print(' ' * (console_half - 4), "OUTPUT", ' ' * (console_half - 4))
        print('-' * term_size.columns)
        data.columns = data.columns.str.strip()
        print("CSV Columns")
        print(data.columns)
        print('-' * term_size.columns)
        
        # Display the first few rows of the data
        print("First few rows of the data:")
        print(data.head())
        print('-' * term_size.columns)

        # Get basic information about the data
        print("Data information:")
        print(data.info())
        print('-' * term_size.columns)

        # Perform data filtering
        print("Perform data filtering: fname as Gaurav")
        filtered_data = data[data.fname == 'Gaurav']
        print(filtered_data)
        print('-' * term_size.columns)

        # Perform data aggregation
        print("Perform data aggregation: fname counts")
        fname_counts = data.fname.value_counts()
        print(fname_counts)
        print('-' * term_size.columns)
        
        # Perform data sorting
        print("Perform data sorting: fname descending")
        fname_sort = data.sort_values(by='fname', ascending=False)
        print(fname_sort)
        print('-' * term_size.columns)
        
        # Data Transformation - sales data:
        print("Data Transformation - sales data:")
        print("sales data columns")
        print(sales_data.columns)
        print('*' * term_size.columns)
        print("sales data describe:")
        print(sales_data.describe())
        print('*' * term_size.columns)
        print(sales_data)
        print('-' * term_size.columns)

        print("Data Transformation - new balance column from diff of sales & expenses:")
        sales_data['balance'] = sales_data.apply(lambda row: row.sales - row.expenses, axis=1)
        print(sales_data)
        print('-' * term_size.columns)

        print("Data Transformation - new is_profit column looking at balance > 0:")
        sales_data['is_profit'] = sales_data['balance'].map(lambda balance: True if balance > 0 else False)
        sales_data.iat[498, 4] =  202
        print(sales_data[sales_data.balance == 202])
        print('-' * term_size.columns)
        print(sales_data)
        print('-' * term_size.columns)

        print("Perform pivot_table on sales data for summing up year wise:")
        sales_data = pd.pivot_table(sales_data, values=['sales', 'expenses', 'balance'], index='year', fill_value=0, aggfunc='sum')
        sales_data['result'] = sales_data.apply(lambda row: 'Loss' if row.balance < 0 else 'Profit', axis=1)
        print(sales_data)
        print('-' * term_size.columns)

        print("Perform filtering on sales data: year 2005")
        print(sales_data[sales_data.index == 2005])
        print('-' * term_size.columns)

        print("Perform filtering on sales data: balance >= 15000")
        print(sales_data[sales_data.balance >= 15000])
        print('-' * term_size.columns)
        
        sales_group = sales_data.groupby('result')
        for group, group_df in sales_group:
            # print(sales_group.get_group(group))
            print(f"Perform grouping on sales data: {group}")
            group_df['severity'] = pd.cut(group_df['balance'], bins=[-75000, -50000, -25000, 0, 25000, 50000, 75000, 95000], labels=['Worst', 'Bad', 'Sick', 'Ok', 'Well', 'Good', 'Best'])
            print(group_df)
            print('-' * term_size.columns)

        print("Data Transformation - sales data:to binary")
        sales_data.loc[sales_data.balance > 0, "balance"] = 1
        sales_data.loc[sales_data.balance <= 0, "balance"] = 0
        sales_data.loc[sales_data.balance > 0, ["sales", "expenses"]] = 1
        sales_data.loc[sales_data.balance <= 0, ["sales", "expenses"]] = 0
        print(sales_data)
        # --------------------------------end--------------------------------
        print('_' * term_size.columns)
        # --------------------------------end--------------------------------
        # df['column_name'].fillna(0, inplace=True)
        # df.dropna(subset=['column_name'], inplace=True)
        # Data Transformation:
        # df['new_column'] = df['old_column'].apply(lambda x: x * 2)
        # df['category'] = df['code'].map(code_to_category)
        # df['binned_age'] = pd.cut(df['age'], bins=[0, 18, 30, 50, 100], labels=['Child', 'Young', 'Adult', 'Senior'])
        # Time Series Handling:
        # df.resample('D').mean()  # Resample to daily frequency
        # df['timestamp'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
        # Performance Optimization:
        # .astype(): Converting data types to reduce memory usage.
        # df['column_name'] = df['column_name'].astype('category')
        # .iterrows(): Iterating through rows efficiently.
        # for index, row in df.iterrows():
            # Process row
        # Handling Categorical Data:
        # .get_dummies(): Creating dummy variables for categorical data.
        # pd.get_dummies(df, columns=['category'])
        # Category Data Type: Converting columns with a limited number of unique values to the category data type to reduce memory usage.
        # df['category_column'] = df['category_column'].astype('category')

    """ if not data_dup.empty:
        data_dup.columns = data_dup.columns.str.strip()
        print("CSV Columns for duplicate data:")
        print(data_dup.columns)
        print('-' * term_size.columns)

    if not data.empty and not data_dup.empty:
        print("Merge and Join: Combining DataFrames based on common columns or indices:")
        merged_fname = pd.merge(data, data_dup, on='fname')
        print(merged_fname)
        print('-' * term_size.columns) """




   
    
