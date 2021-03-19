import pandas as pd

def HelloPandas():
    df = pd.DataFrame(
         {
             "Name": [
                 "Braund, Mr. Owen Harris",
                 "Allen, Mr. William Henry",
                 "Bonnell, Miss. Elizabeth",
             ],
             "Age": [22, 35, 58],
             "Sex": ["male", "male", "female"],
         }
     )
    print(df)