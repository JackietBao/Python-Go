"""
import numpy as np
import matplotlib.pyplot as plt

# 创建一个x值的数组，从-2π到2π，步长为0.01
x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)

# 计算每个x值对应的sin(x)值
y = np.sin(x)

# 使用matplotlib来绘制图像
plt.figure()  # 创建一个新的图像窗口
plt.plot(x, y)  # 绘制折线图
plt.title('sin(x)')  # 设置图像的标题
plt.xlabel('x')  # 设置x轴的标签
plt.ylabel('sin(x)')  # 设置y轴的标签
plt.grid(True)  # 显示网格
plt.show()  # 显示图像


import matplotlib.pyplot as plt
import numpy as np

# 创建数据生成的点的数量，这里是50
num_points = 50
#生成50个在[0,1)之间均匀分布的随机数，作为x坐标
x = np.random.rand(num_points)  # x坐标
#生成50个在[0,1)之间均匀分布的随机数，作为y坐标
y = np.random.rand(num_points)  # y坐标
#生成50个在[0,1)之间均匀分布的随机数，用作每个点的颜色
colors = np.random.rand(num_points)  # 每个点的颜色
#生成50个在[0,1)之间均匀分布的随机数，并乘以1000，作为每个点的大小
sizes = 1000 * np.random.rand(num_points)  # 每个点的大小
#生成50个在[0,1)之间均匀分布的随机数，作为每个点的透明度
alphas = np.random.rand(num_points)  # 每个点的透明度

# 创建散点图
#所有点的透明度设为0.5  使用'viridis'颜色映射来显示颜色条
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

# 显示颜色条
plt.colorbar()

# 显示图像
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

# 设置标签的位置
x = np.arange(len(labels))

# 绘制柱状图
plt.bar(x, values, color='blue', align='center', alpha=0.7)

# 设置图表的标题和轴标签
plt.title('Simple Bar Chart')
plt.xlabel('Labels')
plt.ylabel('Values')

# 设置x轴的标签
plt.xticks(x, labels)

# 显示图像
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 正常显示负号

file_loc = 'resources/销售数据.xlsx'

data = pd.read_excel(file_loc)

print(data)


#使用groupby方法按照'大类名称'列对数据进行分组，并对每个分组的'销售金额'列进行求和
#再次使用reset_index方法，并且drop=True，这一次是为了删除排序后的旧索引并生成新的连续索引
data_extract = data.groupby('大类名称')['销售金额'].sum().reset_index().sort_values('销售金额',ascending=True).reset_index(drop=True)
print(data_extract)

# 使用大类名称作为x轴的标签
x_labels = data_extract['大类名称']
bars = plt.bar(x_labels, data_extract['销售金额'], tick_label=x_labels)
plt.xticks(rotation=45)  # 如果标签文字太长，可以旋转标签以便更好地显示

# 在每一根柱上显示对应的高度值
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')  # ha: horizontal alignment, va: vertical alignment

plt.show()



import matplotlib.pyplot as plt

# 数据
sizes = [15, 30, 45, 10]  # 各部分的大小
labels = ['A', 'B', 'C', 'D']  # 各部分的标签
colors = ['yellow', 'red', 'green', 'orange']  # 各部分的颜色
explode = (0.1, 0, 0, 0)  # 突出显示第一个部分

# 绘制扇形图
plt.pie(sizes, explode=explode, labels=labels,
        colors=colors, autopct='%1.1f%%', shadow=True,
        startangle=140)

# 设置为等比例，这样扇形图就是一个圆
plt.axis('equal')

# 显示图像
plt.show()
"""



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

file_loc = 'resources/销售数据.xlsx'

data = pd.read_excel(file_loc)

print(data)

data_extract = data.groupby('商品类型')['销售金额'].sum()
data_extract = data_extract.reset_index()


# 提取销售金额和大类名称
sales_amounts = data_extract['销售金额']
category_names = data_extract['商品类型']

# 计算每个类别的占比
sales_proportions = sales_amounts / sales_amounts.sum()

# 画饼状图
fig1, ax1 = plt.subplots()
ax1.pie(sales_proportions, labels=category_names, autopct='%1.1f%%', startangle=90)


plt.show()


























































































