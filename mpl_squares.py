#绘制简单折线图
import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=4) #绘线,可以设置输入,输出,线条粗细

plt.title("Square Numbers",fontsize=24)  #设置标题
plt.xlabel("Value",fontsize=14) #设置坐标轴标签
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14) #设置刻度标记的大小
plt.show() #显示生成的图像