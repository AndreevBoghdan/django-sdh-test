import pandas as pd

dateparser = lambda x: pd.datetime.strptime(x, "%d.%m.%Y %H:%M")
weather_df = pd.read_csv('weather.csv',
	error_bad_lines=False, comment='#', delimiter=';',
	index_col=False,
	parse_dates=['Местное время в Харькове (аэропорт)'],
	date_parser=dateparser,
	)


weather_df.rename(columns={'Местное время в Харькове (аэропорт)':'datetime'}, inplace=True)

weather_df['RRR'] = pd.to_numeric(weather_df['RRR'], errors='coerce').fillna(0)
weather_df['Ff'] = pd.to_numeric(weather_df['Ff'], errors='coerce').fillna(0)

mounth_wind_test = weather_df.groupby([pd.Grouper(key='datetime', freq='M')])['Ff'].mean()

print ('1) the most windy month is {}, average wind is {}'.format(
	mounth_wind_test.idxmax().strftime('%Y-%m'),
	round(mounth_wind_test.max(),2)))

month_coldest_test = weather_df.groupby([pd.Grouper(key='datetime', freq='M')])['T'].mean()

print ('2) the coldest month is {}, average temperature is {}'.format(
	month_coldest_test.idxmin().strftime('%Y-%m'),
	round(month_coldest_test.min(),2) ))

day_coldest_test = weather_df.groupby([pd.Grouper(key='datetime', freq='D')])['T'].mean()

print ('3) the coldest day is {}, average temperature is {}'.format(
	day_coldest_test.idxmin().strftime('%d.%m.%Y'),
	round(day_coldest_test.min(),2) ))

month_hotest_test = weather_df.groupby([pd.Grouper(key='datetime', freq='M')])['T'].mean()

print ('4) the hotest month is {}, average temperature is {}'.format(
	month_hotest_test.idxmax().strftime('%Y-%m'),
	round(month_hotest_test.max(),2) ))

day_hotest_test = weather_df.groupby([pd.Grouper(key='datetime', freq='D')])['T'].mean()

print ('5) the hotest day is {}, average temperature is {}'.format(
	day_hotest_test.idxmax().strftime('%d.%m.%Y'),
	round(day_hotest_test.max(),2)))

week_rainy_test = weather_df.groupby([pd.Grouper(key='datetime', freq='W')])['RRR'].sum()

the_rainiest_week_value = round(week_rainy_test.max(),2)
the_rainiest_week_sunday = week_rainy_test.idxmax()
the_rainiest_week_monday = the_rainiest_week_sunday - pd.Timedelta("6 days")

print('6) the most rainy week is {} - {}, rain value is {}'.format(
	the_rainiest_week_monday.strftime('%d.%m.%Y'),
	the_rainiest_week_sunday.strftime('%d.%m.%Y'),
	the_rainiest_week_value ))