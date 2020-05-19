import matplotlib.pyplot as plt
import pandas as pd
from Data import read_excel
from Data import parse

df = read_excel.import_df()
years_filter = parse.filter_years(df)
categorized_df = parse.filter_categories(df)




fig_directory = '/Users/jonathancheung/Dropbox/Claris/Figures/'

## Year difference plots
all_18 = categorized_df['Service Items'].iloc[:, years_filter['18']]
all_19 = categorized_df['Service Items'].iloc[:, years_filter['19']]
diff_df = pd.DataFrame(all_19.values - all_18.values)
diff_df.set_index(all_18.index, inplace=True)
raw_strings = all_18.columns
diff_df.columns = raw_strings.str.strip("'18")
all_19.columns = raw_strings.str.strip("'18")
all_18.columns = raw_strings.str.strip("'18")


data = diff_df.iloc[diff_df.index == 'Total Services Offered*',0:12].transpose()

fig_name = 'total_service_diff'
value = 9
data = diff_df.iloc[value, 0:12].transpose()
data.plot(kind = 'bar')
plt.ylabel('Difference from 2019 minus 2018 in ' + diff_df.index[value])
plt.savefig(fig_directory + fig_name + '.png', bbox_inches='tight')

fig_name = 'breakdown_service_diff'
data = diff_df.iloc[0:8, 0:12].transpose()
data.plot(kind = 'line')
plt.ylabel('Difference in number of services offered from 2019 to 2018 (2019 minus 2018)')

plt.rcParams.update({'font.size': 8})
data = pd.concat([all_18[' Total'], all_19[' Total']], axis=1)
data.iloc[0:9, :].plot(kind='bar')
plt.gcf().subplots_adjust(bottom=0.15)
plt.legend(["'18 total", "'19 Total"])
plt.tight_layout()