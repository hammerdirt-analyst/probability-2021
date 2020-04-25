import numpy as np
from utilities.utility_functions import get_data_by_date_range
import matplotlib.pyplot as plt
from utilities.utility_functions import save_the_figure as save_the_figure

def make_box_plot_stats(date_range, df_location, percentiles,whiskers, start_date, end_date):
    data_by_dates = get_data_by_date_range(df_location, date_range)
    locations = data_by_dates['location'].unique()
    num_samps = len(data_by_dates)
    num_locations = len(locations)
    label='{} - {}'.format(start_date, end_date)
    an_array = data_by_dates.total.values
    data_quantiles = np.percentile(an_array, percentiles)
    whislo = np.percentile(an_array, whiskers[0])
    whishi = np.percentile(an_array, whiskers[1])
    box_stats = {
        'label':label,
        'med':data_quantiles[1],
        'q1':data_quantiles[0],
        'q3':data_quantiles[2],
        'whislo':whislo ,
        'whishi':whishi,
        'fliers':[x for x in an_array if x > data_quantiles[2] or x < data_quantiles[0]],
        }

    return box_stats, data_quantiles, num_samps, num_locations

def single_boxplot(**kwargs):

    fig, ax = plt.subplots(figsize=(kwargs['figsize']))

    number_of_samples= kwargs['num_samps']
    if(kwargs['num_locations'] > 1):
        plural_or_not = 'locations'
    else:
        plural_or_not = 'location'

    kwargs['the_title']["label"] = "{}{} samples, {} {}.".format(
        kwargs['the_title']["label"],        
        kwargs['num_samps'],
        kwargs['num_locations'],
        plural_or_not
    )

    ax.bxp(kwargs["bxpstats"],
           showfliers=True,
           flierprops=kwargs['flierprops'],
           medianprops=kwargs['medianprops'],
           boxprops=kwargs['boxprops'],
           capprops=kwargs['capprops']
           )

    plt.ylabel(kwargs['y_axis']['label'],
               fontfamily=kwargs['y_axis']['fontfamily'],
               labelpad=kwargs['y_axis']['lablepad'],
               color=kwargs['y_axis']['color'],
               size=kwargs['y_axis']['size']
              )

    plt.xlabel(kwargs['x_axis']['label'],
               fontfamily=kwargs['x_axis']['fontfamily'],
               labelpad=kwargs['x_axis']['lablepad'],
               color=kwargs['x_axis']['color'],
               size=kwargs['x_axis']['size'],
              )

    plt.subplots_adjust(**kwargs['subplot_params'])
    plt.title(**kwargs['the_title'], fontdict=kwargs['title_style'], **kwargs['the_title_position'])
    plt.suptitle(kwargs['the_sup_title']['label'],
                 size=kwargs['sup_title_style']['fontsize'],
                 color=kwargs['sup_title_style']['color'],
                 fontfamily=kwargs['sup_title_style']['fontfamily'],
                 x=kwargs['sup_title_position']['x'],
                 y=kwargs['sup_title_position']['y'],
                 ha=kwargs['sup_title_position']['ha'],
                 va=kwargs['sup_title_position']['va'],

                )
    plt.grid(b=kwargs['grid_props']['b'],
             which=kwargs['grid_props']['which'],
             axis=kwargs['grid_props']['axis'],
             color=kwargs['grid_props']['color'],
             alpha=kwargs['grid_props']['alpha']
            )

    save_the_figure(folder=kwargs['save_this']['folder'], file_name=kwargs['save_this']['file_name'], file_suffix=kwargs['save_this']['file_suffix'])

    plt.show()
    plt.close()
