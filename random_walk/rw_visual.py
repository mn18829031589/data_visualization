import matplotlib.pyplot as plt
from random_walk import RandomWalk

#模拟多次随机漫步:只要程序处于活动状态,就不断的模拟随机漫步
while True:
    # 创建一个随机漫步的实例,并将所有点绘制出来
    rw = RandomWalk(50000) #可传值增加点数
    rw.fill_walk()
    #调整屏幕尺寸(figure()用于指定图标的高宽,分辨率和背景色)
    plt.figure(dpi=140,figsize=(10,6))
    #给点着色(按先后顺序)
    points_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #重绘起点和终点(颜色,尺寸区别)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #plt.savefig('rw_plot.png',bbox_inches='tight')
    plt.show()
    keep_runing=input("Make another walk？（y/n）:")
    if keep_runing=='n':
        break