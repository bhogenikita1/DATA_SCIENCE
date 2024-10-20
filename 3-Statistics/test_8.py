# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:17:24 2024

@author: HP
"""
'''
1. Given a dataset of integers or floating-point numbers, calculate the 
following descriptive statistics:
 Mean
 Median
 Mode
 Variance
 Standard Deviation
Sample Dataset: [20, 40, 40, 40, 30, 50, 60]
'''

import pandas as pd
import numpy as np
Sample_Dataset=[20, 40, 40, 40, 30, 50, 60]

np.mean(Sample_Dataset)
np.median(Sample_Dataset)
np.mode(Sample_Dataset)
np.var(Sample_Dataset)
np.std(Sample_Dataset)



'''
2. Generate a dataset of 1,000 random values generated from a lognormal 
distribution with a mean of 0 and a standard deviation of 1 in the log-space, 
perform the following tasks:
 Plot the histogram of the dataset.
 Calculate the mean and median of the dataset.
 Fit a lognormal distribution to the data and overlay the probability density 
function (PDF) on the histogram.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(42)

lognormal_data = np.random.lognormal(mean=0, sigma=1, size=1000)

# Step 2: Plot the histogram of the dataset
plt.figure(figsize=(8, 6))
plt.hist(lognormal_data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')

# Step 3: Calculate the mean and median of the dataset
mean_lognormal = np.mean(lognormal_data)
median_lognormal = np.median(lognormal_data)

# Step 4: Fit a lognormal distribution to the data and overlay the PDF
shape, loc, scale = stats.lognorm.fit(lognormal_data, floc=0)  # Fit lognormal to the data
x = np.linspace(min(lognormal_data), max(lognormal_data), 1000)
pdf_fitted = stats.lognorm.pdf(x, shape, loc, scale)

# Overlay the PDF on the histogram
plt.plot(x, pdf_fitted, 'r-', lw=2, label='Lognormal PDF')
plt.title('Histogram with Lognormal PDF overlay')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Display the plot
plt.show()



'''
3. Generate 1,000 random values following a logarithmic distribution with 
a probability parameter p = 0.3. Perform the following tasks:
 Plot the histogram of the dataset.
 Calculate the mean of the dataset.
 Overlay the probability mass function (PMF) of the logarithmic 
distribution on the histogram.
'''

# Step 1: Generate 1,000 random values following a logarithmic distribution with p = 0.3
p = 0.3
logarithmic_data = np.random.logseries(p, size=1000)

# Step 2: Plot the histogram of the dataset
plt.figure(figsize=(8, 6))
plt.hist(logarithmic_data, bins=np.arange(1, 10), density=True, alpha=0.6, color='g', label='Histogram')

# Step 3: Calculate the mean of the dataset
mean_logarithmic = np.mean(logarithmic_data)

# Step 4: Overlay the probability mass function (PMF) of the logarithmic distribution
x = np.arange(1, 10)
pmf = stats.logser.pmf(x, p)

# Overlay the PMF on the histogram
plt.plot(x, pmf, 'r-', lw=2, label='Logarithmic PMF')
plt.title('Histogram with Logarithmic PMF overlay')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Display the plot
plt.show()


'''
4. Given a dataset containing various types of data, categorize each 
variable into the appropriate statistical data type: Nominal, Ordinal, 
Interval, or Ratio. Then, write code to demonstrate how you would work 
with each type of data.
Example Dataset:
ID  Name    Age     Education   Salary  Joining Year
1   Sophie  22      Bachelor's  60000   2022
2   Aryan   25      Master's    75000   2020
3   Amit    28      PhD         78000   2018
4   Charu   26      Bachelor's  45000   2015
5   Piyush  37      Master's    92000   2010
'''


import pandas as pd
import numpy as np
Dataset = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Sophie', 'Aryan', 'Amit', 'Charu', 'Piyush'],
    'Age': [22, 25, 28, 26, 37],
    'Education': ['Bachelor\'s', 'Master\'s', 'PhD', 'Bachelor\'s', 'Master\'s'],
    'Salary': [60000, 75000, 78000, 45000, 92000],
    'Joining Year': [2022, 2020, 2018, 2015, 2010]
}
# Convert to DataFrame
df = pd.DataFrame(Dataset)
df

set(df['Name'])
set(df['ID'])
set(df['Age'])
set(df['Education'])
set(df['Salary'])
set(df['Joining Year'])

meaan_age=df['Age'].mean()
mean_salary=df['Salary'].mean()
year_difference=df['Joining Year']-2000



'''
5. Given a data of house prices [200000, 250000, 150000, 350000, 300000, 
400000, 450000, 600000, 650000, 500000, 550000]. Calculate the following:
 The median of the dataset.
 The 25th percentile (1st quantile), 50th percentile (2nd quantile, also the 
median), and 75th percentile (3rd quantile).
 Visualize the data using a box plot.
'''
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
house_prices= [200000, 250000, 150000, 350000, 300000, 400000, 450000, 600000, 650000, 500000, 550000]
#df=pd.read_excel("C:/3-Statistics/data.xlsx")
df = np.median(house_prices)
df

percentiles = np.percentile(house_prices, [25, 50, 75])
percentiles

plt.boxplot(house_prices)
plt.show()









