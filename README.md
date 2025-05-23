# Tourism in Istanbul: Influence of  Climates 

## Objective

Istanbul is one of the most touristic cities in the world. In this project i will be analyzing the effects of the weather conditions on the number of foreign visitors in Istanbul. 
My goal is to understand how weather patterns such as precipitation ,temperature and wind speed interact with foreign visitor numbers and if there is a correlation exists.

Additionally i will explore the role of climate in the visitor's home countries. By analyzing whether tourists from warmer regions prefer visiting Istanbul in cooler months, or if those from colder regions are more likely to visit during summer, this study will provide deeper insights into seasonal variations in tourism.

Tourism is highly influenced by economic conditions. Therefore in addition to weather patterns ,economic factors such as median income,GDP per capita and inflation will be analyzed as well. This will help determine whether fluctuations in foreign visitor numbers are primarily driven by weather patterns or if economic conditions play a more significant role.

## Data

**Weather Data(2019-2024)**

 Source: https://www.worldweatheronline.com
 
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

**Inflation Of Consumer Prices**

Source: https://www.worldbank.org/en/research/brief/inflation-database

**Past Dolar/Try exchange rate**

Source: https://finance.yahoo.com/quote/USDTRY%3DX/history/?period1=1546300800&period2=1704067200&frequency=1mo&guccounter=1

## Data Analysis Plan

**Weather Conditions Analysis**

1.  Daily Weather data of Istanbul  from 2019 to 2024 is requested from worldweatheronline.com via weather api and arranged into a dataset.
   
2.  A seasonal weather data is generated from daily weather data for Istanbul.
   Winter: January,February,March
   Spring: April,May,June
   Summer: July,August,Septembre
   Fall:   October,November,December

3.  Monthly foreign visitor numbers will be compared to see if a pattern exists.

4.  The time foreign visitors come to Istanbul will be compared against income classification to analyze if a pattern exists.

5.  Climate of the Countries tourists come from are  analyzed and seperated into cold or hot weather categories.

**Economic Conditions Analysis**

1. Country Income Classification is taken from worldbank and used to analyze if income levels affect seasonality.
   
2. Core Costumer Inflation trends in Turkey is analyzed.

3. Inflation and USD/TRY exchange rate data is merged and used to analyze if total visitor number has a correlation with them.

## Processing Data

![Figure_2](https://github.com/user-attachments/assets/d2ace642-b61e-4ead-b47a-7d14a14a135a)

The plot is created by Seasonalityplot.py

Since economic is one of the factors in tourism inflation trends in Turkey has been analyzed.


![Figure_4](https://github.com/user-attachments/assets/24d0fd04-d055-459c-a54e-46686fb9dca0)
The plot is created with inflationanalysis.py

It appears to be there is a significant correlation between inflation of TL and tourists coming to Istanbul.


![Figure_3](https://github.com/user-attachments/assets/5376ea7e-cb74-46f1-a910-6af9983eabc6)
The plot is created with inflationanalysis.py

The USD/TL exchange rate has a moderate effect on the tourist preference while coming to Istanbul.

![Figure_8](https://github.com/user-attachments/assets/8fd4efed-1880-4e38-ad7d-914bd3942220)
the plot is created by humidityandprecipitationanalysis.py

After Inspecting the plot there is clearly a relationship between humidity of the tourists origin countries and Istanbul's season.

![Figure_10](https://github.com/user-attachments/assets/28081003-b937-4559-b5f5-1e59bdaa2210)
the plot is created by precipitationanalysis.py

After inspecting this graph it can be concluded that people tend to not come to istanbul during times of high precipitation.

![Figure_1](https://github.com/user-attachments/assets/d1cb9b33-7286-4575-9242-156f845ea3f0)
the plot is created by IncomeClassification.py

This plot is to analyze if the income group of countries have an effect on when the tourist come to Istanbul. From the the plot i can be interpreted that income groups are not significant at the time of decision.

## Hypothesis Testing

A table containing Season of Istanbul and total tourist numbers from cold,moderate and warm countries is formed. By doing so we can actually analyze the preference of people from different climates.

Chi-Square Test of Independence Results:
Chi2 statistic: 26093420.685
P-value < 0.001
Degrees of freedom: 6

A table containing humidity classification of Istanbul and other countries were made to analyze the humidity of the peoples origin country on their preference to the time they visit Istanbul.

Chi2 statistic: 240070.010
p-value < 0.001
degrees of freedom: 2

Since both tests p-values are (p-value=0.001 < 0.05) we reject Null Hypothesis.

Null Hypothesis: There is no significant relationship between the climate of tourists' home countries and the season during which they choose to visit Istanbul.

Alternative Hypothesis: There is a significant relationship between the climate of tourists' home countries and the season during which they choose to visit Istanbul.

There is a relationship between climate of the tourists origin country and their preference for Istanbul. People tend to choose the time when climate conditions of Istanbul is similar to their countries.

However when analyzing tourist numbers and Istanbul precipitation levels , the findings indicate that the number of tourists drop in the times of high precipitation on Istanbul regardless of their countries precipitation levels. This suggests that while tourist might prefer similar humidity and temperature levels to their countries they avoid unfavorable weather conditions like heavy rain. 

## Future Work 

There might be economic conditions in the background which might require further analysis.
Proximity might have an effect on tourisit decisions.

