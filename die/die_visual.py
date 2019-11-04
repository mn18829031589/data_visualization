from die import Die
import pygal

#创建一个D6
die=Die()

#掷骰子多次，并将结果保存在一个列表中
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

#分析结果
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#对结果进行可视化(绘制直方图)
hist=pygal.Bar()  #pygal让图表有交互性,鼠标指向任一条形均可看到与之关联的数据
hist.title="Results of rolling one D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add('D6',frequencies) #将一系列值添加到图表中,参数1是添加值指定的标签
hist.render_to_file('die_visual.svg') #将图表渲染成一个SVG文件
