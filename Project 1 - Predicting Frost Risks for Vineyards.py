#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


from urllib.request import urlretrieve

url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/119/city_lat_long.csv"

urlretrieve(url, "city_lat_long_dataset.csv")
city_dataset = pd.read_csv("city_lat_long_dataset.csv")
city_dataset


# In[3]:


city_dataset["Alpha-2 code"].unique()


# In[4]:


alpha2_code = pd.read_html("https://www.iban.com/country-codes")
alpha2_code


# In[5]:


alpha2_code = alpha2_code[0]
alpha2_code


# In[6]:


inpPath = "C:/CarolineZiegler/Studium_DCU/8. Semester/Business Analytics Portfolio/Portfolio/02_Uni Projects/Kubicle Project 1/"
vineyards_Df = pd.read_csv(inpPath + "vineyards.csv", delimiter = ",")
vineyards_Df


# In[7]:


vineyards_alpha2 = vineyards_Df.merge(alpha2_code, on = "Country", how = "left")
vineyards_alpha2


# In[8]:


vineyards_alpha2['Alpha-2 code'].replace({np.nan: 'US'}, inplace=True)
vineyards_alpha2


# In[9]:


vineyards_alpha2['Alpha-3 code'].replace({np.nan: 'USA'}, inplace=True)
vineyards_alpha2


# In[10]:


vineyards_city_lat_long = vineyards_alpha2.merge(city_dataset, on =["City", 'Alpha-2 code'], how = "left")
vineyards_city_lat_long


# In[11]:


core_api = "http://api.weatherapi.com/v1/forecast.json?"
api_key = "bfb57ecc5a7e463ead3165422241201"


# In[12]:


from requests import get


# In[15]:


for index, row in vineyards_city_lat_long.iterrows():
    
    lat, long = map(float, row['lat,long'].split(','))
    country_code = row['Alpha-2 code']
    
    api_request = f"{core_api}key={api_key}&q={lat},{long}&days=3"

    response = get(api_request)
    
    if response.status_code == 200:
        weather_data = response.json()
        forecast = weather_data.get('forecast', {})
        forecastdays = forecast.get('forecastday', [])
        for day_index in range(3):
            min_temp_celsius = forecastdays[day_index]['day']['mintemp_c']
            vineyards_city_lat_long.at[index, f'Today+{day_index+1} Min Temp'] = min_temp_celsius
    else:
        print(f'Error for {row["City"]}, {row["Country"]}: {response.status_code}')


# In[16]:


for index, row in vineyards_city_lat_long.iterrows():
    lat_long = row['lat,long']
    api_request = f"{core_api}?key={api_key}&q={lat_long}&days=3"
    
    print(f"Processing {row['City']}, {row['Country']}")
    print(f"API Request: {api_request}")

    response = get(api_request)
    
    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)
        
        vineyards_city_lat_long.at[index, 'Today+1 Min Temp'] = data['forecast']['forecastday'][0]['day']['mintemp_c']
        vineyards_city_lat_long.at[index, 'Today+2 Min Temp'] = data['forecast']['forecastday'][1]['day']['mintemp_c']
        vineyards_city_lat_long.at[index, 'Today+3 Min Temp'] = data['forecast']['forecastday'][2]['day']['mintemp_c']
        
    else:
        print(f"Error for {row['City']}, {row['Country']}: {response.status_code}")


# In[17]:


vineyards_city_lat_long


# In[18]:


vineyards_city_lat_long.to_csv("C:/CarolineZiegler/Studium_DCU/8. Semester/Business Analytics Portfolio/Portfolio/02_Uni Projects/Kubicle Project 1/Vineyard_forecast", index = False)

