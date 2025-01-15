# IS THE TEMPERATURE RISING? LET'S PREDICT

## Overview
It involves predicting future temperatures based on historical data. You are provided with a dataset containing historical temperature data for India up to the year 1999. Your task is to develop models to predict both month-wise and average year-wise temperatures up to September 2013. Find out whether your model predicts increasing trend of temperatures!!.

**You are required to do the predictions for the cities "Delhi" and "Madras" among the many cities in the dataset.**

## Files
- `india_temperatures.csv`: Contains historical temperature data up to the year 1999 citywise for over 170 years timeline. 

## Instructions
1. **Data Preprocessing**: Perform any necessary preprocessing on the data, such as handling missing values, etc.


2. **Exploratory Data Analysis**: As you would have learnt over the previous few weeks, this is the most important step. Make plots of temperature vs time, analyse their time series properties, perform ADF tests, etc. and write your observations. Use this analyse to build the most suitable model.


3. **Model Development**:
    - **Split the Data**: Split the provided data into training and validation sets.
    - **Model Training**: Train different time series models (e.g., ARIMA, SARIMA, etc.) on the training data, whichever seems relevant accoridng to your analysis.
    - **Model Evaluation**: Evaluate the performance of each model on the validation set. Report the prediction time series plots and performance metrics (MSE, MASE, and all other metrics you stuided in the previous weeks) for each model.

4. **Prediction**:
    - **Best Model Selection**: Select the best-performing model based on your evaluation.
    - **Future Predictions**: Use the best model to predict:
        - Month-wise temperatures from January 2000 to September 2013.
        - Average year-wise temperatures from 2000 to 2013.

5. **Submission**: Your predictions will be evaluated on a hidden test set. Ensure your code is well-documented and your models are clearly presented. Submit four csv files for the predictions,"delhi_monthwise.csv", "delhi_yearwise.csv" and "madras_monthwise.csv", "madras_yearwise.csv". Each with two columns, "timeline" (year or month whichever ) and "temperature".

Good Luck!

