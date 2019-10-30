#绘制散点图
import matplotlib.pyplot as plt

#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]
x_values=list(range(1,1001)) #列表数字1~1000
y_values=[x**2 for x in x_values]
#绘点,s设置点的尺寸
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,edgecolor='none',s=40)
        #" c='red' "自定义颜色;c+cmap实现颜色映射,随y_values增大渐深
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14) #刻度标记的大小
plt.axis([0,1100,0,1100000])  #设置每个坐标轴的取值范围
#plt.show()
#自动保存图表时注释掉.show()方法,否则是空白png
# (参数1是存储文件名,默认地址是scatt..py所在目录,参数2指将多余空白区裁剪,若保留省略即可)
plt.savefig('squares_plot.png',bbox_inches='tight')
