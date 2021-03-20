# Authors: Arthur SICARD, Théo DUPONT, Carl BOYER
# Groupe 5 - Video games sales

import MatPlotFunction as mpf
import PandasFunction as pf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_csv(path):
    if isinstance(path, str):
        return pd.read_csv(path)
    if isinstance(path, list):
        for file_path in path:
            yield pd.read_csv(file_path)


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df_ps4, df_sales, df_xbox = import_csv(["dataset/PS4_GamesSales.csv",
                        "dataset/Video_Games_Sales_as_at_22_Dec_2016.csv",
                        "dataset/XboxOne_GameSales.csv"
                        ])

# Get mean value for missing columns
# 'Critic_Score','Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'
    Critic_Score = df_sales['Critic_Score'].mean()
    Critic_Count = df_sales['Critic_Count'].mean()
    User_Score = df_sales['User_Score'].mean()
    User_Count = df_sales['User_Count'].mean()
    # Rating = df_sales['Rating'].mean()

# Rename columns for PS4 & Xbox to follow Sales columns
    df_ps4 = df_ps4.rename(columns = { 'Game' : 'Name', 'Year' : 'Year_of_Release', 'Genre': 'Genre', 'Publisher' : 'Publisher', 'North America' : 'NA_Sales', 'Europe' : 'EU_Sales','Japan' : 'JP_Sales', 'Rest of World' : 'Other_Sales', 'Global' :'Global_Sales' })
    del df_xbox['Pos']
    df_xbox = df_xbox.rename(columns={'Game':'Name','Year':'Year_of_Release','Genre':'Genre','Publisher':'Publisher','North America':'NA_Sales','Europe':'EU_Sales','Japan':'JP_Sales','Rest of World':'Other_Sales','Global':'Global_Sales'})

# Add missing columns to Xbox & PS4
    df_xbox['Platform'] = 'XBOX'
    df_xbox['Critic_Score'] = Critic_Score
    df_xbox['Critic_Count'] = Critic_Count
    df_xbox['User_Score'] = User_Score
    df_xbox['User_Count'] = User_Count
    df_ps4['Platform'] = 'PS4'
    df_ps4['Critic_Score'] = Critic_Score
    df_ps4['Critic_Count'] = Critic_Count
    df_ps4['User_Score'] = User_Score
    df_ps4['User_Count'] = User_Count

# Concate df
    frames = [df_sales, df_xbox, df_ps4]
    df_global = pd.concat(frames)

# Set pivot table

# Fusion des doublons et conservation des valeurs max
#     table = df_global[df_global.Platform == "PS4"].pivot_table(
    table = df_global.pivot_table(
        index=['Platform','Name'],
        values=['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales','Global_Sales',
                 'Critic_Score','Critic_Count', 'User_Score', 'User_Count'],
        aggfunc=[np.max],
        fill_value=0 )
    # exit()
# Calculate sum sales for each zone for each plateform
#     table_sum_sales = df_global[df_global.Platform == "PS4"].pivot_table(
    table_sum_sales = df_global.pivot_table(
        index=['Platform'],
        values=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
        aggfunc=[np.sum],
        fill_value=0)

# Display graph sales by plateform by localisation
    table_sum_sales.plot(
        kind="bar",
        subplots=False,
        title="Video games sales by platefome around the world",
        ylabel="Sales by localisation",
        sharex=False,
        figsize=(6,6)
    )

# Flatten Pivot table to Dataframe to simplify then locate desired line
    flatten_table_sales = pd.DataFrame(table_sum_sales)
    # print(flatten_table_sales.loc["PS4"])

    dataSalesPs4 = flatten_table_sales.loc["PS4"]

    sum_NA_Sales = dataSalesPs4['sum']['NA_Sales']
    sum_EU_Sales = dataSalesPs4['sum']['EU_Sales']
    sum_JP_Sales = dataSalesPs4['sum']['JP_Sales']
    sum_Other_Sales = dataSalesPs4['sum']['Other_Sales']

# Display pie chart about Ps4 sales
    labels = 'NA_Sales', 'EU_Sales','JP_Sales','Other_Sales'
    sizes = [sum_NA_Sales, sum_EU_Sales, sum_JP_Sales, sum_Other_Sales]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()




#PS4 Index(['Game', 'Year', 'Genre', 'Publisher', 'North America', 'Europe','Japan', 'Rest of World', 'Global'],
#Xbox Sales(['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score','Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating'],
#Sales Xbox(['Pos', 'Game', 'Year', 'Genre', 'Publisher', 'North America', 'Europe','Japan', 'Rest of World', 'Global'],

