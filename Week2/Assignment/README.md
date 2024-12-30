# Week 2 Assignment
Hey, its time to apply some time-series skills. You have been given a dataset "stores_sales_forecasting2.csv" . Create a "week2.ipynb" and do the following:

**Task 1:**

First of all, preprocess the data. That is check for missing values in the data, ensure correct datatype of each feature, no duplicates, etc.
And handle them accordingly. For example, rows with missing values can be imputed with preceding/succeeding rows data, filled with the average value of that feature, etc. Read about such techniques more here - https://medium.com/@aaabulkhair/data-imputation-demystified-time-series-data-69bc9c798cb7 and apply the suitable ones.

**The data is provided daywise (by order date) in a random order. Group the sales monthwise using order dates then proceed further.**

**Task 2:**

This task is seemingly easy but often the most important one. Plot and Visualise the time series, and observe for the things you have studied....seasonality, cycles, trends, etc. Write down your observations (use Markdown cells).

**Task 3:**

Now that you have observed, use "statsmodels" Python library to break the series into trends, seasonality, residual components and write your observations.

**Task 4:**

In any data, there can be too much of noise. To ignore those outliers(find out how are outliers detected), implement "Simple Moving Average(SMA)" and "Exponential Moving Average(EMA)" of the Time series and visualise all the three plots (original and two averages together). Write down the observed difference between EMA and SMA.

**Task 5:**

This will be our first predicitve model.

If you are not familiar with linear regression, first checkout this link- https://www.youtube.com/watch?v=owI7zxCqNY0 and https://www.youtube.com/watch?v=8jazNUpO3lQ . (Ask for resources if you want to go more deep into regression.)

Then go through this notebook - https://www.kaggle.com/code/ryanholbrook/linear-regression-with-time-series .

And finally create your own regression prediction model on given dataset by splitting it into train(80%) and test(20%) sets. Plot the prediction line along with actual data. Report your results including MAE, MASE, RMSE on the test set in the notebook. (Read about the metrics and find out which one is best for time series.)


Happy learning !