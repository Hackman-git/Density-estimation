'''
Name:   Olugbenga Abdulai
ID:     A20447331
'''

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the file
path = r"C:\Users\abdul\Desktop\CS 584\HW\HW 1\NormalSample.csv"
file = pd.read_csv(path)
col = file['x']
N = col.size

'''
This function calculates the density estimates of the histogram
   Inputs: a pandas series of numbers and a specified bin width
   Output: a list of density estimates
   The adjusted minimum and maximum values have been considered
   here
'''
def hist_density_estimator(values, width):
    N = values.size
    midpoints = []
    minim = values.min()
    real_min = math.floor(minim)
    maxim = values.max()
    real_max = math.ceil(maxim)

    # obtaining the first midpoint
    counter = real_min + (width / 2)

    # obtaining the subsequent midpoints
    while(counter < maxim):
        midpoints.append(counter)
        counter += width

    # converting the pandas series to a numpy array to ease calculations
    vals = np.array(values)
    estimates = []
    # bin edges for histogram
    bins = []

    # iterating through each midpoint and calculating deviations
    for mid in midpoints:
        bins.append(mid - (width / 2))
        weights = []
        dev = (vals - mid) / width

        # Obtaining weights
        for i in dev:
            if (i > -0.5 and i <= 0.5):
                weights.append(1)
            else: weights.append(0)

        estimates.append(sum(weights) / (N * width))
    bins.append(bins[-1] + width)

    print('midpoints: ',midpoints)

    # plotting the histogram
    sns.distplot(vals, bins=bins, kde=False, color='green',
                 hist_kws={'edgecolor':'black'})
    plt.title('Histogram for bin width '+ str(width))
    plt.show()

    return estimates

'''
Q 1(a): Suggested bin width by Izenman (1991)

'''
# obtaining the interquartile range
first_quart, third_quart = np.percentile(col, [25, 75])
iqr = third_quart - first_quart

# obtaining bin width
width_iz = 2 * iqr * (1 / np.cbrt(N))
print('suggested width: ', width_iz, end='\n\n')

'''
Q 1(b): minimum and maximum values of field x

'''
mini = col.min()
maxi = col.max()
print('min value in x: ', mini, end='\n\n')
print('max value in x: ', maxi, end='\n\n')

'''
Q 1(c): calculating a and b

'''
a = math.floor(mini)
b = math.ceil(maxi)
print('a is: ', a, end='\n\n')
print('b is: ', b, end='\n\n')

'''
Q 1(d): density estimator coordinates for width=0.25

'''
points = hist_density_estimator(values=col, width=0.25)
print('coordinates: ',points, end='\n\n')

'''
Q 1(e): density estimator coordinates for width=0.5

'''
points = hist_density_estimator(col, width=0.5)
print('coordinates: ', points, end='\n\n')

'''
Q 1(f): density estimator coordinates for width=1.0

'''
points = hist_density_estimator(col, width=1)
print('coordinates: ', points, end='\n\n')

'''
Q 1(g): density estimator coordinates for width=2.0

'''
points = hist_density_estimator(col, width=2)
print('coordinates: ', points, end='\n\n')