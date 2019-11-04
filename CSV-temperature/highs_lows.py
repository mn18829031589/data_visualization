import csv #用于分析CSV(以逗号分隔的值)文件中的数据行,能够快速提取感兴趣的数据
import matplotlib.pyplot as plt
from datetime import datetime
filename='sitka_weather_2018_simple.csv'
with open(filename) as f: #f存储文件对象
    reader=csv.reader(f)  #与文件相关联的阅读器对象
    header_row=next(reader) #reader处理数据时将每项数据作为一个元素存储在一个列表中
    #打印文件头及其位置
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    #提取并读取数据(最高/低气温TMAX/TMIN日期DATE)
    highs,lows,dates=[],[],[]
    for row in reader:
    #错误检查(如:缺失数据时无法将空字符串转换为整数)
        try:
            date = datetime.strptime(row[2], "%Y-%m-%d")  # 将字符串转换为表示相应日期的对象
            high = int(row[5])  # 将字符串转换为数字让matplotlib能够读取它
            low = int(row[6])
        except ValueError:
            print(date,'missing data')
        else:
             dates.append(date)
             highs.append(high)
             lows.append(low)
    #根据数据绘制图像
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)  #设置alpha后颜色变浅
    plt.plot(dates,lows,c='blue',alpha=0.5)
    #图标区域着色了解每天的气温范围,参数alpha指定颜色透明度(0全透1全不透)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    #设置图形的格式
    plt.title("Daily high and low temperature-2018",fontsize=26)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate() #绘制斜的日期标签以免重叠
    plt.ylabel('Temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()