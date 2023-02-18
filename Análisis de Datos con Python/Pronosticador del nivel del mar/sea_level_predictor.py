import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = range(df["Year"].min(), 2051, 1)
    y1 = [round(y, 7) for y in (intercept + slope * x1)]
    plt.plot(x1, y1, "r")

    # Create second line of best fit
    df2000 = df.loc[(df["Year"] >= 2000)]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2000["Year"], df2000["CSIRO Adjusted Sea Level"])
    x2 = range(df2000["Year"].min(), 2051, 1)
    y2 = [round(y, 7) for y in (intercept2 + slope2 * x2)]
    plt.plot(x2, y2, "r")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()