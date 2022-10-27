
import matplotlib.ticker as tick
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#source: https://www.kaggle.com/code/dimitriirfan/eda-introduction-to-vtubers
def reformat_large_tick_values(tick_val, pos):
    """
    Turns large tick values (in the billions, millions and thousands) such as 4500 into 4.5K and also appropriately turns 4000 into 4K (no zero after the decimal).
    """
    if tick_val >= 1000000000:
        val = round(tick_val/1000000000, 1)
        new_tick_format = '{:}B'.format(val)
    elif tick_val >= 1000000:
        val = round(tick_val/1000000, 1)
        new_tick_format = '{:}M'.format(val)
    elif tick_val >= 1000:
        val = round(tick_val/1000, 1)
        new_tick_format = '{:}K'.format(val)
    elif tick_val < 1000:
        new_tick_format = round(tick_val, 1)
    else:
        new_tick_format = tick_val

    # make new_tick_format into a string value
    new_tick_format = str(new_tick_format)
    
    # code below will keep 4.5M as is but change values such as 4.0M to 4M since that zero after the decimal isn't needed
    index_of_decimal = new_tick_format.find(".")
    
    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal+1]
        if value_after_decimal == "0":
            # remove the 0 after the decimal point since it's not needed
            new_tick_format = new_tick_format[0:index_of_decimal] + new_tick_format[index_of_decimal+2:]
            
    return new_tick_format

def create_plot_bar(data, group):
    plt.figure(figsize=(20,9))
    ax = sns.barplot(data=data,
                x="englishName", 
                y="subscriptionCount",
                alpha=0.8)
    ax.yaxis.set_major_formatter(tick.FuncFormatter(reformat_large_tick_values))
    ax.set_axisbelow(True)
    plt.title(f'{group} Subscriber 2022')
    plt.ylabel('Subs', fontsize=12)
    plt.xlabel('Talent', fontsize=12)
    plt.show()
    
def create_scatter_plot(data):
    #source: https://stackoverflow.com/a/46028674
    ax = sns.lmplot('videoCount', # Horizontal axis
           'subscriptionCount', # Vertical axis
           data=data, # Data source
           fit_reg=False, # Don't fix a regression line
           size = 5,
           aspect = 3 ) # size and dimension

    plt.title('Korelasi antara Subscriber dan Video Upload')
    # Set x-axis label
    plt.xlabel('Video Upload')
    # Set y-axis label
    plt.ylabel('Subscriber')
    
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.02, point['y'], str(point['val']))
        