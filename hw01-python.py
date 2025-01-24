# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# load libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set wd
wd = r"C:\Users\cms549\Box\classwork\2025_Spring\BEE5850\hw\hw01-christinemswanson"

os.chdir(wd)

# load beer/mosquito bites data set
data = pd.read_csv("./data/bites.csv")

# problem 2 - shuffle data, compare to null distribution (non-parametric bootstrapping?)

# number of bootstrap samples
B = 50000
# non-parametric bootstrapping
mean_diff_vals = [] # store the mean difference values 

for i in np.arange(0,B):
    # resample n observations from original data, with replacement
    #boot_samp = data.sample(len(gages2), replace=True) # resample from entire df
    
    # shuffle the data
    np.random.shuffle(data["group"])
    
    # recalculate the differences in means 
    mean_diff_i = np.mean(data[data["group"] == "beer"]["bites"]) - np.mean(data[data["group"] == "water"]["bites"])

    # fit with ols() all the regressors using your boot samples
    #mdl_boot = ols(my_formula, data = boot_samp).fit()
    # append beta values to empty list, count how many less than zero outside the loop
    mean_diff_vals.append(mean_diff_i)

# plot the values
plt.hist(mean_diff_vals, color = "grey", bins=25)
plt.axvline(x=4.37777777777778, color = "red", linestyle="--") #4.3777...is original value

plt.title("Distribution of Differences in Means for Mosquito Bites (Beer vs. Water)")
plt.ylabel("Number of Shuffles")
plt.xlabel("Mean Difference in Mosquito Bites (Beer vs. Water)")

plt.show()

    
