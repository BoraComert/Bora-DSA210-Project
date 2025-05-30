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


Since economic is one of the factors in tourism inflation trends in Turkey has been analyzed.


![Figure_4](https://github.com/user-attachments/assets/24d0fd04-d055-459c-a54e-46686fb9dca0)


It appears to be there is a significant correlation between inflation of TL and tourists coming to Istanbul.


![Figure_3](https://github.com/user-attachments/assets/5376ea7e-cb74-46f1-a910-6af9983eabc6)


The USD/TL exchange rate has a moderate effect on the tourist preference while coming to Istanbul.

![Figure_8](https://github.com/user-attachments/assets/8fd4efed-1880-4e38-ad7d-914bd3942220)

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

## Machine Learning Techniques

Now that hypothesis testing is complete , we can develop machine learning models to predict the number of tourist is coming to istanbul based on Ethnicity, Istanbul's weather condition , other countries weather condition ,TL inflation and income classifcation of countries.

Since the data is continous models will be about regression.

Predicators will be the following columns on the filtered_merged_output.csv : Date,Country,Country_Temp,Country_Humidity,Country_Precipitation,Avg Temperature (C),Avg Humidity (%),Total Precipitation (mm) ,Income classification

Avg Temperature , Total precipitation and Avg Humidity are Istanbul's data

Target will be the Visitors column.

### Multicolinerity Analysis

Correlation between predicators might distort the results of machine learning algorithms so it is best to check before implementation. We will use Variance Inflation Factor (VIF) Scores to check if there is a high correlation between features.

![image](https://github.com/user-attachments/assets/a1ebbb37-bc45-4941-a72d-31d2ad503c87)

### Variance Inflation Factor (VIF) Scores

| Feature                  | VIF         |
|--------------------------|-------------|
| const                    | 1282.178385 |
| Avg Temperature (C)      | 4.411763    |
| Avg Humidity (%)         | 4.024948    |
| Country_Humidity         | 2.186522    |
| Country_Precipitation    | 2.005954    |
| Total Precipitation (mm) | 1.638862    |
| Country_Temp             | 1.607103    |
| YoY_Inflation (%)        | 1.123432    |

Slight Correlation between Temperature and Humidity is a known weather phenomenon. More weather evaporates when temperature is high and hence more humidity in the air.
Since any of the predicators are not over 5 we don't have to drop one.

### K Nearest Neighbours Model

K Nearest Neighbour Model using one hot encoding for country and label encoding for Income classification.
We have to first find the best number of K for the model.

![image](https://github.com/user-attachments/assets/818fa716-9ce5-4fa0-8904-fa99775ca747)


Best k: 4 with RMSE: 23505.06

![image](https://github.com/user-attachments/assets/b4da6021-db45-4b1d-8e34-7b18544a14ed)


RMSE: 23505.06
R^2 Score: 0.7296

Our model might be prone to overfitness.Let's check by using 5 fold  cross validation.

Cross-Validation RMSE Scores: [14740.78469004 55886.44534054 62113.35298067 93965.76169791 20713.97639702]

Mean RMSE: 49484.06
Std Deviation: 29030.76

### Random Forest Regression Model


![image](https://github.com/user-attachments/assets/b5978e7e-eeb9-49e3-8c73-004c182c4dfa)

![image](https://github.com/user-attachments/assets/6a3efaa1-bc4e-4d24-adf4-1e5f1b8f7082)

![image](https://github.com/user-attachments/assets/8803c754-080b-4d9e-8255-6b863927a9d0)



R^2 Score: 0.7224

RMSE: 23816.80

Our Model might be prone for overfitting. We have to check using 5 fold cross validation.

Cross Validation RMSE Scores: [24773.61223564 28022.95107626 30912.70925616 30524.94428591 27966.29144994]

| RMSE                     |Fold Index   |
|--------------------------|-------------|
| 24773.61223564           | 1           |
| 28022.95107626           | 2           |
| 30912.70925616           | 3           |
| 30524.94428591           | 4           |
| 27966.29144994           | 5           |


Mean RMSE: 28440.10
Standard Deviation: 2204.63



### Multilinear Regression Model 

![image](https://github.com/user-attachments/assets/fa90c939-8e0b-4165-9102-2a212d4e933c)

Multilinear Regression RMSE: 25949.98
Multilinear Regression R^2 Score: 0.6704

![image](https://github.com/user-attachments/assets/501c9ac9-a544-4989-bdc4-caf74643d2d0)

RMSE: 0.97
R^2 Score: 0.8654

After 5 Fold Cross Validation:
Average RMSE: 0.93
Average R^2 Score : 0.8806


### Comparison Between Models 




## Limitations




## Future Work 

There might be economic conditions in the background which might require further analysis.
Proximity might have an effect on tourisit decisions.

