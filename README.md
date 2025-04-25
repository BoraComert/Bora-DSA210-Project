# Tourism in Istanbul: Influence of  Climates 

## Objective

Istanbul is one of the most touristic cities in the world. In this project i will be analyzing the effects of the weather conditions on the number of foreign visitors in Istanbul. 
My goal is to understand how weather patterns such as precipitation ,temperature and wind speed interact with foreign visitor numbers and if there is a correlation exists.

Additionally i will explore the role of climate in the visitor's home countries. By analyzing whether tourists from warmer regions prefer visiting Istanbul in cooler months, or if those from colder regions are more likely to visit during summer, this study will provide deeper insights into seasonal variations in tourism.

Tourism is highly influenced by economic conditions. Therefore in addition to weather patterns ,economic factors such as median income,GDP per capita and inflation will be analyzed as well. This will help determine whether fluctuations in foreign visitor numbers are primarily driven by weather patterns or if economic conditions play a more significant role.

## Data

**Weather Data(2019-2024)**

 Source: Past Observations will be taken from Weather Api
 
- Average Wind Speed
- Weather Condition(sunny,cloudy etc.) 
- Precipitation 
- Maximum temperature
- Minimum temperature
- Average Humidity

**Seasonal weather data**

source: https://climateknowledgeportal.worldbank.org

**Monthly Foreign Visitor Data(2019-2024)** 
 
 Source: https://data.ibb.gov.tr/dataset/turkiye-ve-istanbul-olceginde-gelen-yabanci-ziyaretci-sayisi

- Place(Turkey or Istanbul)
- Monthly Foreign Visitor Number

**Country Classifications by Income Level**

    Source: https://www.worldbank.org/en/search?q=income+groups

**Nationalities of Foreign Tourists Coming to Istanbul(2019-2024)**

Source: https://data.ibb.gov.tr/dataset/milliyetlerine-gore-istanbul-a-gelen-yabanci-turist-sayisi

- Nationality Of The Visitor
- Monthly Visitor Count By Nationality

**Median Income Of The World**

Source: https://ourworldindata.org/grapher/daily-median-income?tab=chart&country=TUR~OWID_WRL~AUT

**Gdp Per Capita Of Countries**

Source: https://ourworldindata.org/grapher/gdp-per-capita-worldbank

**Inflation Of Consumer Prices**

Source: https://www.worldbank.org/en/research/brief/inflation-database

## Data Analysis Plan

**Weather Conditions Analysis**

1.  Weather data of Istanbul will be requested from weather api and arranged into a dataset.
   
2.  A daily weather quality score will be generated from weather data for Istanbul.

3.  Monthly foreign visitor numbers will be compared to see if a pattern exists.

4.  Nationalities of the the foreign visitors will be compared if a pattern exists.

5.  Climate of the Countries with the most tourists come from will be analyzed and seperated into cold or hot weather categories.

**Economic Conditions Analysis**

1. Median income of citizens of foreign countries will be compared against Turkish Citizens.
   
2. Inflation trends in Turkey and the rest of the world will be analyzed.
 
## Processing Data



