import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from wordcloud import STOPWORDS, WordCloud
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


# 环境和参数的配置
def set_seaborn_properties(context='talk', font_scale=0.8):
    sns.set_theme(context=context, font='Helvetica', font_scale=font_scale,
                  rc={'axes.unicode_minus': False,
                      'figure.figsize': (12, 8),
                      'figure.dpi': 150})


# 获取2020年国家地区数据封装成的DataFrame
def get_2020_entities_dataframe():
    entity_group = global_users.groupby('Entity')
    entity_2020_df = pd.DataFrame()
    for entity, entity_df in entity_group:
        if entity == 'World':
            continue
        entity_2020 = entity_df[entity_df['Year'] == 2020]
        entity_2020_df = pd.concat([entity_2020_df, entity_2020], join='outer', axis=0)
    return entity_2020_df.set_index('Entity')


# 全球用户每年的各项数据的分析与可视化
def global_internet_users_analysis():
    set_seaborn_properties()
    # 全球每年的互联网用户总数分析与可视化：
    plt.subplots_adjust(hspace=1, wspace=0.7)
    year_groups = global_users.groupby('Year')
    internet_users_groups = year_groups['No. of Internet Users']
    column_mean = internet_users_groups.sum()
    internet_users_sum_data = pd.DataFrame({'Year': column_mean.index,
                                            'sum': column_mean.values})
    plt.subplot(2, 2, 1)
    plt.title('The total number of global internet users per year')
    plt.xlabel('Year')
    plt.ylabel('The total number of global internet users per year')
    sns.lineplot(data=internet_users_sum_data, x='Year', y='sum')
    plt.bar(column_mean.index, column_mean.values, color='cornflowerblue', width=0.6)

    # 全球每年每100人移动端互联网订阅数、互联网使用人数比例、每100人宽带订阅数的平均值分析与可视化：
    year_groups = global_users.groupby('Year')
    title_mapper = {'Cellular Subscription': 'Global annual mobile internet subscriptions per 100 people',
                    'Internet Users(%)': 'Global annual proportion of internet users',
                    'Broadband Subscription': 'Global average broadband subscriptions per 100 people per year'}
    i = 2
    for column in ['Cellular Subscription', 'Internet Users(%)', 'Broadband Subscription']:
        plt.subplot(2, 2, i)
        i += 1
        internet_users_groups = year_groups[column]
        column_mean = internet_users_groups.mean()
        column_max = internet_users_groups.max()
        max_data = pd.DataFrame({'Year': column_max.index, 'max': column_max.values})
        mean_data = pd.DataFrame({'Year': column_mean.index, 'mean': column_mean.values})
        plt.title(title_mapper[column])
        plt.xlabel('Year')
        plt.ylabel(title_mapper[column])
        sns.lineplot(data=max_data, x='Year', y='max', label=column + ' max', lw=2, linestyle=(0, (5, 1)))
        sns.lineplot(data=mean_data, x='Year', y='mean', label=column + ' mean', lw=3, linestyle=(0, (1, 1)))
        plt.legend(loc='upper left', prop={'size': 8.5})
    plt.savefig('../img/Analysis and visualization of annual data for global users.png')
    plt.show()


# 2020年各个国家地区的用户占比饼图和柱状图绘制
def entities_2020_internet_users_percentage_pie_bar():
    entity_2020_df = get_2020_entities_dataframe()
    entity_2020_df['No. of Internet Users'] /= entity_2020_df['No. of Internet Users'].sum()

    # 只筛选用户数量最多的10组数据，其他数据用`other`代替
    entity_2020_df.sort_values(by='No. of Internet Users', axis=0, ascending=False, inplace=True)
    other = entity_2020_df.iloc[10:].loc[:, 'No. of Internet Users'].sum()
    other_df = pd.DataFrame(data={'': {'Entity': 'Other', 'No. of Internet Users': other}}).T
    other_df.set_index('Entity', inplace=True)
    processed_data = pd.concat([entity_2020_df.head(10), other_df], axis=0, join='outer')

    # 绘制饼图
    set_seaborn_properties(context='notebook', font_scale=0.8)
    explode_arr = np.zeros(shape=(11))
    explode_arr[0] = 0.07
    plt.axes(aspect=1)
    plt.title('The proportion of internet users in various countries and regions in 2020')
    plt.pie(processed_data['No. of Internet Users'], labels=processed_data.index, explode=explode_arr,
            labeldistance=1.1, autopct='%2.1f%%', pctdistance=0.9, shadow=True)
    plt.legend(loc='lower right', bbox_to_anchor=(0.5, 0., 0.95, 0.5), ncols=2)
    plt.savefig('../img/Pie chart of the proportion of internet users in different countries and regions in 2020.png')
    plt.show()

    # 绘制柱状图
    set_seaborn_properties(font_scale=0.56)
    plt.rcParams['figure.dpi'] = 300
    data = pd.DataFrame({'Entity': processed_data.index, 'Percent': processed_data['No. of Internet Users']})
    plt.title('The proportion of internet users in various countries and regions in 2020')
    sns.barplot(data=data, x='Entity', y='Percent')
    plt.savefig('../img/Bar chart of the proportion of internet users in different countries and regions in 2020.png')
    plt.show()


# 2020年各国家地区互联网用户占比分布直方图
def entities_2020_internet_users_percentage_distribution_histogram():
    set_seaborn_properties(font_scale=0.8)
    entity_2020_df = get_2020_entities_dataframe()
    internet_users_percentage_sr = entity_2020_df['Internet Users(%)']
    plt.title('Histogram of the proportion of internet users in different countries and regions in 2020')
    plt.xlabel('The proportion of internet users')
    plt.ylabel('Number of countries and regions')
    data = pd.DataFrame({'Entity': internet_users_percentage_sr.index, 'Percent': internet_users_percentage_sr.values})
    sns.histplot(data, x='Percent')
    plt.savefig('../img/Histogram of the proportion of internet users in different countries and regions in 2020.png')
    plt.show()


# 2020年个国家地区互联网用户占比和移动互联网订阅量的散点图
def entities_2020_internet_users_percentage_distribution_scatter():
    set_seaborn_properties()
    entity_2020_df = get_2020_entities_dataframe()
    plt.title('Scatter plot of internet user proportion and mobile internet subscription volume by country and region in 2020')
    plt.xlabel('The proportion of internet users')
    plt.ylabel('Mobile internet subscription volume')
    sns.scatterplot(data=entity_2020_df, x='Internet Users(%)', y='Cellular Subscription',
                    palette='husl', hue='Entity', legend=None)

    # 利用线性回归分析两者关系
    x = entity_2020_df[['Internet Users(%)']]
    model_1 = linear_model.LinearRegression()
    model_1.fit(x, entity_2020_df[['Cellular Subscription']])
    data = pd.DataFrame({'x': x['Internet Users(%)'], 'pred_y': [x[0] for x in model_1.predict(x)]})
    sns.lineplot(data=data, x='x', y='pred_y')
    plt.savefig('../img/Scatter plot and linear regression fitting of the proportion of internet users and mobile internet subscriptions in different countries and regions in 2020.png')
    plt.show()


# 用每一年互联网用户的比例最大的三个国家地区名生成词云
def draw_internet_users_percentage_annual_top_3_wordcloud():
    text = ''
    year_groups = global_users.groupby('Year')
    # 获取每一年互联网用户的比例最大的三个国家地区名数据
    for year, year_df in year_groups:
        year_df.sort_values(by='Internet Users(%)', ascending=False, inplace=True)
        top_3 = year_df.head(3)
        entities = top_3['Entity']
        for entity in entities:
            if len(entity.split()) > 1:
                text += entity.replace(' ', '_') + ' '
                # 将名字中含有空格的国家地区名中的空格替换成下划线_，避免一个名字被拆分成多个单词
            else:
                text += entity + ' '
    wc = WordCloud(max_words=100, width=800, height=400, background_color='White',
                   max_font_size=150, stopwords=STOPWORDS, margin=5, scale=1.5)
    wc.generate(text)
    plt.title('The noun cloud of the country with the highest proportion of internet users each year')
    plt.imshow(wc)
    plt.axis("off")
    wc.to_file('../img/The noun cloud of the country with the highest proportion of internet users each year.png')
    plt.show()


# 对中国互联网用户数据的分析与可视化
def chinese_users_analysis():
    # 绘制各项指标的数值图
    set_seaborn_properties()
    pd.options.mode.chained_assignment = None
    plt.title('Number of internet users in China (in millions), proportion of population, proportion of mobile internet subscriptions per 100 people, proportion of broadband subscriptions per 100 people')
    plt.xlabel('Year')
    plt.ylabel('Numerical value')
    chinese_users.loc[:, 'No. of Internet Users'] /= 10000000
    sns.lineplot(data=chinese_users, x='Year', y='No. of Internet Users', label='Quantity (in millions of people)', lw=3)
    sns.lineplot(data=chinese_users, x='Year', y='Internet Users(%)', label='Proportion of population', lw=3)
    sns.lineplot(data=chinese_users, x='Year', y='Cellular Subscription', label='Mobile internet subscription ratio per 100 people', lw=3)
    sns.lineplot(data=chinese_users, x='Year', y='Broadband Subscription', label='Broadband subscription ratio per 100 people', lw=3)
    plt.legend(loc='upper left')
    plt.savefig('../img/Number of internet users in China (in millions), proportion of population, proportion of mobile internet subscriptions per 100 people, proportion of broadband subscriptions per 100 people.png')
    plt.show()

    # 绘制各项指标的增长率图
    set_seaborn_properties()
    chinese_users.loc[:, 'increase of No. of Internet Users'] = 0
    chinese_users.loc[:, 'increase of Internet Users(%)'] = 0
    chinese_users.loc[:, 'increase of Cellular Subscription'] = 0
    chinese_users.loc[:, 'increase of Broadband Subscription'] = 0
    rows = len(chinese_users.index)
    for i in range(rows - 1):
        chinese_users.loc[:, 'increase of No. of Internet Users'].iloc[i + 1] = int( 0 if chinese_users.iloc[i]['No. of Internet Users'] == 0 else (chinese_users.iloc[i + 1].loc['No. of Internet Users'] - chinese_users.iloc[i]['No. of Internet Users']) / chinese_users.iloc[i]['No. of Internet Users'])
        chinese_users.loc[:, 'increase of Internet Users(%)'].iloc[i + 1] = int ( 0 if chinese_users.iloc[i]['Internet Users(%)'] == 0 else (chinese_users.iloc[i + 1]['Internet Users(%)'] - chinese_users.iloc[i]['Internet Users(%)']) / chinese_users.iloc[i]['Internet Users(%)'])
        chinese_users.loc[:, 'increase of Cellular Subscription'].iloc[i + 1] = int ( 0 if chinese_users.iloc[i]['Cellular Subscription'] == 0 else (chinese_users.iloc[i + 1]['Cellular Subscription'] - chinese_users.iloc[i]['Cellular Subscription']) / chinese_users.iloc[i]['Cellular Subscription'])
        chinese_users.loc[:, 'increase of Broadband Subscription'].iloc[i + 1] = int ( 0 if chinese_users.iloc[i]['Broadband Subscription'] == 0 else (chinese_users.iloc[i + 1]['Broadband Subscription'] - chinese_users.iloc[i]['Broadband Subscription']) / chinese_users.iloc[i]['Broadband Subscription'])
    plt.title('The growth rate of the number of internet users in China (in millions), the proportion of population, the proportion of mobile internet subscriptions per 100 people, and the proportion of broadband subscriptions per 100 people')
    plt.xlabel('Year')
    plt.ylabel('Numerical value')
    sns.lineplot(data=chinese_users, x='Year', y='increase of No. of Internet Users', lw=4,
                 label='Growth rate of quantity (in millions of people)')
    sns.lineplot(data=chinese_users, x='Year', y='increase of Internet Users(%)', lw=4,
                 label='Proportion of population')
    sns.lineplot(data=chinese_users, x='Year', y='increase of Cellular Subscription', lw=4,
                 label='Growth rate of mobile internet subscription per 100 people')
    sns.lineplot(data=chinese_users, x='Year', y='increase of Broadband Subscription', lw=4,
                 label='Growth rate of broadband subscription per 100 people')
    plt.legend(loc='upper left')
    plt.savefig('../img/The growth rate of the number of internet users in China (in millions), the proportion of population, the proportion of mobile internet subscriptions per 100 people, and the proportion of broadband subscriptions per 100 people.png')
    plt.show()

    # 利用多元线性回归预测中国互联网到2050年的总用户数
    # 拟合：
    set_seaborn_properties()
    plt.title('Fitting the total number of internet users in China from 1980 to 2020')
    sns.scatterplot(data=chinese_users, x='Year', y='No. of Internet Users')
    poly_reg = PolynomialFeatures(degree=3)
    x = chinese_users[['Year']]
    x_m = poly_reg.fit_transform(x)

    model_2 = linear_model.LinearRegression()
    model_2.fit(x_m, chinese_users[['No. of Internet Users']])
    data = pd.DataFrame({'x': x['Year'], 'pred_y': [x[0] for x in model_2.predict(x_m)]})
    plt.xlabel('Year')
    plt.ylabel('Number of people (in millions)')
    sns.lineplot(data=data, x='x', y='pred_y')
    plt.savefig('../img/Fitting the total number of internet users in China from 1980 to 2020')
    plt.show()

    # 预测：
    set_seaborn_properties()
    plt.title('Prediction of the total number of internet users in China by 2030')
    plt.xlabel('Year')
    plt.ylabel('Number of people (in millions)')
    pred_x = pd.DataFrame(np.arange(1980, 2031), columns=['Year'])
    pred_x_m = poly_reg.fit_transform(pred_x)
    plt.plot(pred_x, model_2.predict(pred_x_m))
    plt.savefig('../img/Prediction of the total number of internet users in China by 2030')
    plt.show()


if __name__ == '__main__':
    # 读取文件，获取全球互联网用户信息
    global_users = pd.read_csv('../data/Final.csv', delimiter=',', usecols=range(1, 8))  # 由于第一列的列名未知，所以不使用第一列
    # 对全球用户进行分析：
    global_internet_users_analysis()
    entities_2020_internet_users_percentage_pie_bar()
    entities_2020_internet_users_percentage_distribution_histogram()
    entities_2020_internet_users_percentage_distribution_scatter()
    draw_internet_users_percentage_annual_top_3_wordcloud()

    # 通过切片获取中国互联网用户信息
    chinese_users = global_users.loc[global_users['Entity'] == 'China']
    chinese_users_analysis()
