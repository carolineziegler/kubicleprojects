#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


from urllib.request import urlretrieve

madden_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/112/Madden_s_Dairy.csv"

urlretrieve(madden_url, "Madden_s_Dairy.csv")
madden_dataset = pd.read_csv("Madden_s_Dairy.csv")
madden_dataset


# In[3]:


nell_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/113/Nell_s_Soups_and_Stocks.csv"
clerkin_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/114/Clerkin_Nuts_and_Grains.csv"
mahon_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/115/Mahon_Produce.csv"
nutley_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/116/Nutley_Fish_and_Seafood.csv"
foley_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/117/Foley_s_Butchers.csv"
tolsco_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/118/Tolsco_Foods.csv"


# In[4]:


urlretrieve(nell_url, "Nell_s_Soups_and_Stocks.csv")
nell_dataset = pd.read_csv("Nell_s_Soups_and_Stocks.csv")
nell_dataset


# In[5]:


urlretrieve(clerkin_url, "Clerkin_Nuts_and_Grains.csv")
clerkin_dataset = pd.read_csv("Clerkin_Nuts_and_Grains.csv")
clerkin_dataset


# In[6]:


urlretrieve(mahon_url, "Mahon_Produce.csv")
mahon_dataset = pd.read_csv("Mahon_Produce.csv")
mahon_dataset


# In[7]:


urlretrieve(nutley_url, "Nutley_Fish_and_Seafood.csv")
nutley_dataset = pd.read_csv("Nutley_Fish_and_Seafood.csv")
nutley_dataset


# In[8]:


urlretrieve(foley_url, "Foley_s_Butchers.csv")
foley_dataset = pd.read_csv("Foley_s_Butchers.csv")
foley_dataset


# In[9]:


urlretrieve(tolsco_url, "Tolsco_Foods.csv")
tolsco_dataset = pd.read_csv("Tolsco_Foods.csv")
tolsco_dataset


# In[10]:


urlretrieve(tolsco_url, "Tolsco_Foods.csv")
tolsco_dataset = pd.read_csv("Tolsco_Foods.csv")
tolsco_dataset


# In[11]:


nutritional_data = pd.concat([madden_dataset, nell_dataset, mahon_dataset, clerkin_dataset, nutley_dataset, foley_dataset, tolsco_dataset], )
nutritional_data.reset_index(drop=True, inplace=True)
nutritional_data


# In[12]:


nutritional_data["Protein"].sum()


# In[13]:


nutritional_data["Calories"].unique()


# In[14]:


nutritional_data["Grams"].unique()


# In[15]:


import re


# In[16]:


def clean_column(column):
    return column.apply(lambda x: re.sub(r'[^0-9.]', '', x))


nutritional_data["Grams"] = pd.to_numeric(clean_column(nutritional_data["Grams"]), errors='coerce')
nutritional_data["Calories"] = pd.to_numeric(clean_column(nutritional_data["Calories"]), errors='coerce') 


# In[17]:


nutritional_data


# In[18]:


nutritional_data["Grams"].sum()


# In[19]:


nutritional_data["Calories"].sum()


# In[20]:


nutritional_data[nutritional_data["Calories"] < 0]


# In[21]:


nutritional_data[nutritional_data["Grams"] < 0]


# In[22]:


nutritional_data[nutritional_data["Protein"] < 0]


# In[23]:


nutritional_data["Protein"].unique()


# In[24]:


nutritional_data["Protein"].replace(-30.0, 30.0, inplace = True)
nutritional_data[nutritional_data["Protein"] < 0]


# In[25]:


nutritional_data["Protein"].replace(-1.0, 1.0, inplace = True)
nutritional_data[nutritional_data["Protein"] < 0]


# In[26]:


nutritional_data[nutritional_data["Fat"] < 0]


# In[27]:


nutritional_data["Fat"].replace(-7.0, 7.0, inplace = True)
nutritional_data[nutritional_data["Fat"] < 0]


# In[28]:


nutritional_data[nutritional_data["Fiber"] < 0]


# In[29]:


nutritional_data[nutritional_data["Carbs"] < 0]


# In[30]:


nutritional_data["Carbs"].replace(-8.0, 8.0, inplace = True)
nutritional_data["Carbs"].replace(-22.0, 22.0, inplace = True)
nutritional_data[nutritional_data["Carbs"] < 0]


# In[31]:


nutritional_data[nutritional_data["Grams"] > 1000]


# In[32]:


nutritional_data["Grams"].replace(1100.0, 110.0, inplace = True)
nutritional_data[nutritional_data["Grams"] > 1000]


# In[33]:


nutritional_data[nutritional_data["Calories"] > 1500]


# In[34]:


nutritional_data[nutritional_data["Protein"] > 250]


# In[35]:


nutritional_data[nutritional_data["Fat"] > 250]


# In[36]:


nutritional_data["Fat"].replace(470.0, 6.0, inplace = True)
nutritional_data["Fat"].replace(360.0, 36.0, inplace = True)
nutritional_data[nutritional_data["Fat"] > 250]


# In[37]:


nutritional_data[nutritional_data["Food"] == "Cheddar"]


# In[38]:


nutritional_data[nutritional_data["Fiber"] > 250]


# In[39]:


nutritional_data[nutritional_data["Carbs"] > 250]


# In[40]:


null_values_breakdown = nutritional_data.isnull().sum()
null_values_breakdown


# In[41]:


nutritional_data[nutritional_data["Protein"].isnull()]


# In[42]:


nutritional_data.at[6, "Protein"] = 30.0
nutritional_data.at[79, "Protein"] = 19.0
nutritional_data[nutritional_data["Protein"].isnull()]


# In[43]:


nutritional_data[nutritional_data["Fat"].isnull()]


# In[44]:


nutritional_data.at[52, 'Fat'] = 0.0
nutritional_data.at[193, 'Fat'] = 8.0
nutritional_data.at[215, 'Fat'] = 10.0
nutritional_data[nutritional_data["Fat"].isnull()]


# In[45]:


nutritional_data[nutritional_data["Food"] == "Flounder"]


# In[46]:


nutritional_data[nutritional_data["Fiber"].isnull()]


# In[47]:


nutritional_data["Fiber"].replace(np.nan, 2.5, inplace = True)
nutritional_data[nutritional_data["Fiber"].isnull()]


# In[48]:


nutritional_data[nutritional_data["Carbs"].isnull()]


# In[49]:


nutritional_data[nutritional_data["Carbs"].isnull()]


# In[50]:


nutritional_data["Carbs"].replace(np.nan, 9.0, inplace = True)
nutritional_data[nutritional_data["Carbs"].isnull()]


# In[51]:


nutritional_data[nutritional_data.duplicated()]


# In[52]:


nutritional_data.drop_duplicates(inplace=True)
nutritional_data


# In[53]:


nutritional_data.reset_index(drop=True, inplace=True)
nutritional_data


# In[54]:


nutritional_data["Food Type"].value_counts()


# In[55]:


nutritional_data["Food Type"].replace("Drairy", "Dairy", inplace = True)
nutritional_data["Food Type"].replace("Fruit", "Fruits", inplace = True)
nutritional_data["Food Type"].replace("Mreat & Poultry", "Meat & Poultry", inplace = True)
nutritional_data["Food Type"].replace("Oil & Fats", "Oils & Fats", inplace = True)
nutritional_data["Food Type"].value_counts()


# In[56]:


nutritional_data[nutritional_data["Food Type"] == "insert_category_here"]


# In[57]:


nutritional_data["Food Type"].replace("insert_category_here", "Seafood", inplace = True)
nutritional_data["Food Type"].value_counts()


# In[58]:


nutritional_data['Incorrect_calories'] = (nutritional_data['Calories'] != (nutritional_data['Fat'] * 9 + (nutritional_data['Protein'] + nutritional_data['Fiber'] + nutritional_data['Carbs']) * 4)).astype(int)
nutritional_data


# In[59]:


nutritional_data['True Calories'] = nutritional_data['Fat'] * 9 + (nutritional_data['Protein'] + nutritional_data['Fiber'] + nutritional_data['Carbs']) * 4
nutritional_data


# In[60]:


rows_with_incorrect_calories = nutritional_data[nutritional_data['Incorrect_calories'] == 1]

print("Rows with Incorrect 'Calories' Values:")
rows_with_incorrect_calories


# In[61]:


nutritional_data['Calories'] = nutritional_data['Fat'] * 9 + (nutritional_data['Protein'] + nutritional_data['Fiber'] + nutritional_data['Carbs']) * 4

print("\nDataFrame with Corrected 'Calories' Values:")
print(nutritional_data[['Food', 'Food Type', 'Calories']])


# In[62]:


nutritional_data


# In[63]:


rows_with_incorrect_calories


# In[64]:


nutritional_data[nutritional_data["Food"]== "French-fried"]


# In[65]:


nutritional_data.to_csv("C:/CarolineZiegler/Studium_DCU/8. Semester/Business Analytics Portfolio/Portfolio/02_Uni Projects/Kubicle Project 2/Nutritional Data Output File", index = False)

