# -*- coding: utf-8 -*-
"""
Multiple Correlation Analysis and Linear Regression
Created on 6th Jan 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

# Load the dataset
Cars = pd.read_csv("C:/DataSet/Cars.csv")

# Exploratory Data Analysis (EDA)
# Descriptive statistics
print(Cars.describe())

# Graphical representation
plt.figure(figsize=(8, 5))
plt.bar(height=Cars.HP, x=np.arange(1, len(Cars.HP) + 1))
plt.title('Bar Plot of HP')
plt.show()

plt.hist(Cars.HP, bins=10, edgecolor='k', alpha=0.7)
plt.title('Histogram of HP')
plt.show()

plt.boxplot(Cars.HP)
plt.title('Boxplot of HP')
plt.show()

# Joint plot for HP vs MPG
sns.jointplot(x=Cars['HP'], y=Cars['MPG'])
plt.show()

# Count plot of HP
plt.figure(figsize=(16, 10))
sns.countplot(Cars['HP'])
plt.title('Count Plot of HP')
plt.show()

# QQ Plot for MPG
stats.probplot(Cars.MPG, dist="norm", plot=plt)
plt.title('QQ Plot of MPG')
plt.show()

# Pair Plot
sns.pairplot(Cars)
plt.show()

# Correlation matrix
print(Cars.corr())

# Linear Regression - Initial Model
ml1 = smf.ols('MPG ~ WT + VOL + SP + HP', data=Cars).fit()
print(ml1.summary())

# Influential data points
sm.graphics.influence_plot(ml1)
plt.show()

# Removing influential data point (76th row)
Cars_new = Cars.drop(Cars.index[[76]])

# Regression after removing the influential point
ml1_new = smf.ols('MPG ~ WT + VOL + HP + SP', data=Cars_new).fit()
print(ml1_new.summary())

# Variance Inflation Factor (VIF)
rsq_hp = smf.ols('HP ~ WT + VOL + SP', data=Cars).fit().rsquared
vif_hp = 1 / (1 - rsq_hp)

rsq_wt = smf.ols('WT ~ HP + VOL + SP', data=Cars).fit().rsquared
vif_wt = 1 / (1 - rsq_wt)

rsq_vol = smf.ols('VOL ~ HP + WT + SP', data=Cars).fit().rsquared
vif_vol = 1 / (1 - rsq_vol)

rsq_sp = smf.ols('SP ~ HP + WT + VOL', data=Cars).fit().rsquared
vif_sp = 1 / (1 - rsq_sp)

# VIF DataFrame
d1 = {'Variables': ['HP', 'WT', 'VOL', 'SP'], 'VIF': [vif_hp, vif_wt, vif_vol, vif_sp]}
vif_frame = pd.DataFrame(d1)
print(vif_frame)

# Final Model after removing WT
final_ml = smf.ols('MPG ~ VOL + SP + HP', data=Cars).fit()
print(final_ml.summary())

# Predictions
pred = final_ml.predict(Cars)

# Residual Analysis
res = final_ml.resid

# QQ Plot of Residuals
stats.probplot(res, dist="norm", plot=plt)
plt.title('QQ Plot of Residuals')
plt.show()

# Residual Plot
sns.residplot(x=pred, y=Cars.MPG, lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt.title('Fitted vs Residuals')
plt.show()

# Splitting the data into train and test sets
Cars_train, Cars_test = train_test_split(Cars, test_size=0.2, random_state=42)

# Model on Training Data
model_train = smf.ols('MPG ~ VOL + SP + HP', data=Cars_train).fit()
print(model_train.summary())

# Predictions on Test Data
test_pred = model_train.predict(Cars_test)

# Test Errors
test_error = Cars_test.MPG - test_pred
test_rmse = np.sqrt(np.mean(test_error ** 2))
print(f"Test RMSE: {test_rmse}")
