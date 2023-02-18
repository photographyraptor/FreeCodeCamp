import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])

# Clean data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] < df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(
        legend=False,
        figsize=(20, 7),
        xlabel="Date",
        ylabel="Page Views",
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019").figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot    
    df_bar = df.copy()
    df_bar["month"] = df_bar["date"].dt.month
    df_bar["year"] = df_bar["date"].dt.year    
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    
    # Draw bar plot
    ax = df_bar.plot.bar()
    ax.legend([
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"], title='Months')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
