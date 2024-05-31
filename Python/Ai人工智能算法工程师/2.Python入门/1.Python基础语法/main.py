"""
#当你不关心某个值时，可以使用下划线 (_) 作为“丢弃”变量。
x,_ = 1,2
print(x)

#建议命名规则1_下划线法
user_name = "Jackietbao"
print(user_name)
account_blance = 1000.50
print(account_blance)


#建议命名规则2_驼峰法
userName = "LiuHui"
print(userName)
accountBlance = 1000.50
print(accountBlance)



#可以打印一个对象
print("AI")
#需要打印的对象，可以是多个
print("Hello","World")
#用于分隔多个对象的字符，默认是空格
print("Hello","World",sep="-")
print("Hello",end="!")


result = input("请输入结果")
print(result)

#使用type()可以查看数据类型
a = 1
b = 3.14
c = '123'
d = "这也是字符串"
e = '''这也可以是字符串'''

print("a的数据类型是：", type(a))
print("b的数据类型是：", type(b))
print("c的数据类型是：", type(c))
print("d的数据类型是：", type(d))
print("e的数据类型是：", type(e))


#转为浮点型 使用float()转为小数
num_str = input("请输入小数:")
print("num_str = ", num_str, " 格式是：", type(num_str))
num_float = float(num_str)
print("num_float = ", num_float, " 格式是：", type(num_float))

#转为字符串 使用str()转为字符串
name = "Alice"
age = 30

print("My name is %s and I'm %d years old." % (name, age))
print("My name is {} and I'm {} years old.".format(name, age))
print(f"My name is {name} and I'm {age} years old.")


#输出时控制精度
number = 12.3456

print("%.2f" % number)
print("{:.2f}".format(number))
print(f"{number:.2f}")


#if语句
x = 10
if x > 5:
    print("x大于5")

#if..else语句
x = 10
if x > 5:
    print("x > 5")
else:
    print("x <= 5")


#if..elif..else语句
x = 5
if x > 10:
    print("x大于10")
elif x == 5:
    print("x是5")
else:
    print("x小于10, 但不是5")


#综合案例
a = 10
b = 20
result = a + b
answer = int(input(f"请输入{a}+{b}的结果"))
if result == answer:
    print("回答正确！")
else:
    print("回答错误")


#for循环 可指定循环次数
epoch = 5
for epoch_i in range(epoch):
    print("---------------")
    print(f"正在处理第{epoch_i}个epoch的数据")
    print(f"第{epoch_i}个数据处理完毕")


#for循环  可指定迭代对象
optimizers = ["SGD", "Adam", "Momentum", "Adagrad"]
for optimizer_i in optimizers:
    print("正在使用", optimizer_i, "进行优化")

#for循环  可对数据进行枚举
img_list = ["img_1.png", "img_2.png", "img_3.png"]
for index, img_i in enumerate(img_list):
    print(f"索引 {index} 对应的数据是 {img_i}")

#while循环 当不清楚循环多少次时，使用while
command = ""
while command != "end":
    command = input("请输入命令: ")
    print("正在执行命令: ", command)

#使用break可以停止循环，跳出当前的循环
# 这是一个数字列表，机器人将在这个列表中搜索数字“5”
numbers = [1, 3, 4, 2, 5, 6, 8, 7, 9]

# 这是一个标志，用来表示机器人是否找到了数字“5”
found = False

# 机器人开始搜索数字“5”
for number in numbers:
    print(f"正在查看数字{number}")
    if number == 5:
        found = True
        print(f"机器人找到了数字{number}！")
        break  # 一旦找到数字“5”，就退出循环

# 检查机器人是否找到了数字“5”
if not found:
    print("机器人没有找到数字5。")


#continue跳出当前的回合，仍在循环中
# 这是一个数字列表，机器人将在这个列表中搜索不是“5”的数字
numbers = [1, 3, 4, 2, 5, 6, 8, 7, 9]

# 机器人开始搜索不是“5”的数字
for number in numbers:
    print(f"正在查看数字{number}")
    if number == 5:
        continue  # 如果数字是“5”，跳过当前迭代，继续下一次循环
    print(f"机器人找到了数字{number}！")




#综合案例
a = 10
b = 20
result = a + b
while True:
    answer = int(input(f"请输入{a}+{b}的结果"))
    if result == answer:
        print("回答正确！")
        break
    else:
        print("回答错误")

#序列索引
numbers = [10, 11, 12, 13, 14]
print(numbers[0])
print(numbers[-1])

#序列切片
numbers = [10, 11, 12, 13, 14]
print(numbers[1:3])
print(numbers[2:])
print(numbers[:2])
print(numbers[:-2])
print(numbers[0:4:2])

#序列相加
numbers = [1, 2, 3, 4, 5]
data = ["a", "b", 3, 4.0, 5]
result = numbers + data
print(result)

#序列乘法
numbers = [1, 2, 3]
result = numbers * 3
print(result)


#序列是否包含元素
numbers = [1, 2, 3]
if 1 in numbers:
    print("1 在 numbers 里面")
else:
    print("1 不在 numbers 里面")


#序列长度，最大值，最小值
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print(max(numbers))
print(min(numbers))

#创建列表
list_empty = []
list_a = [1, 2, 3]
list_b = list(range(10))

print(list_empty)
print(list_a)
print(list_b)

#访问列表元素
list_a = [1, 2, 3]
print(list_a[1])

#遍历列表1
data_list = ['a', 'b', 'c', 'd', 'e']
for data_i in data_list:
    print(data_i)


#遍历列表2
data_list = ['a', 'b', 'c', 'd', 'e']
for index, data_i in enumerate(data_list):
    print(index, data_i)


#添加、修改、删除列表元素
list_a = [1, 2, 3, 4, 5]
print(list_a)
list_a.append(6)
print(list_a)
list_a[0] = 0
print(list_a)
list_a.remove(4)
print(list_a)

#列表元素统计计算
list_a = [1, 2, 3, 4, 5]
result = sum(list_a)
print(result)


#列表排序
score = [50, 60, 20, 40, 30, 80, 90, 55, 100]
print("原列表: ", score)
score.sort()
print("升序后: ", score)
score.sort(reverse=True)
print("降序后: ", score)

#列表推导式
x_list = [i for i in range(10)]
print(x_list)



#列表案例
# 初始的模型准确率
accuracies = [0.85, 0.90, 0.88, 0.92]

# 添加新的准确率
accuracies.append(0.95)

# 计算平均准确率
average_accuracy = sum(accuracies) / len(accuracies)
print(f"Average Accuracy: {average_accuracy:.2f}")


#创建元组
tuple_1 = ()
tuple_2 = tuple(range(10, 20, 2))

print(tuple_1)
print(tuple_2)


#访问元组元素
tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1[2])
print(tuple_1[-1])

#元组推导式
tuple_a = tuple(i for i in range(10))
print(tuple_a)


#元组案例
# 模型的配置（层数，每层的单元数，激活函数）
model_config = (3, 128, "relu")

# 解包元组
layers, units, activation = model_config
print(f"Layers: {layers}, Units: {units}, Activation: {activation}")

#创建字典  字典存放的信息以键值的形式出现
info_xiaoming = {'name': '小明', 'age': 14, 'score': 60}
info_zhangsan = {'name': '张三', 'age': 15, 'score': 79}

print(info_xiaoming)
print(info_xiaoming['age'])
print(info_zhangsan['score'])

#创建字典  字典存放的信息以键值的形式出现
# 创建一个字典来存储神经网络的配置参数
neural_network_config = {
    "layer_1": {"units": 64, "activation": "relu"},
    "layer_2": {"units": 128, "activation": "relu"},
    "output_layer": {"units": 10, "activation": "softmax"}
}

print(neural_network_config)

#通过键值对访问字典
# 创建一个字典来存储神经网络的配置参数
neural_network_config = {
    "layer_1": {"units": 64, "activation": "relu"},
    "layer_2": {"units": 128, "activation": "relu"},
    "output_layer": {"units": 10, "activation": "softmax"}
}

# 访问字典中的特定键值对
layer_1_units = neural_network_config["layer_1"]["units"]
print(f"Number of units in layer 1: {layer_1_units}")


#遍历字典
info_xiaoming = {'name': '小明', 'age': 14, 'score': 60}

# 遍历字典
print("以下为 xiaoming 的信息：")
for key, value in info_xiaoming.items():
    print(f"{key} 为 {value}")


#遍历字典
neural_network_config = {
    "layer_1": {"units": 64, "activation": "relu"},
    "layer_2": {"units": 128, "activation": "relu"},
    "output_layer": {"units": 10, "activation": "softmax"}
}

# 遍历字典，打印每一层的配置信息
for layer, config in neural_network_config.items():
    print(f"{layer}: {config['units']} units, activation = {config['activation']}")



#添加、修改、删除字典元素
neural_network_config = {
    "layer_1": {"units": 64, "activation": "relu"},
    "layer_2": {"units": 128, "activation": "relu"},
    "output_layer": {"units": 10, "activation": "softmax"}
}

# 添加一个新的层到字典
neural_network_config["layer_3"] = {"units": 256, "activation": "relu"}

# 修改第一层的单元数
neural_network_config["layer_1"]["units"] = 128

# 删除输出层的激活函数键值对
del neural_network_config["output_layer"]["activation"]

# 输出修改后的字典
print(neural_network_config)



#字典案例
# 不同模型的信息
models_info = {
    "CNN": {"layers": 3, "units": 128, "activation": "relu"},
    "RNN": {"layers": 2, "units": 64, "activation": "tanh"}
}

# 访问特定模型的信息
cnn_info = models_info["CNN"]
print(f"CNN - Layers: {cnn_info['layers']}, Units: {cnn_info['units']}, Activation: {cnn_info['activation']}")


#创建集合
set_1 = set()
set_2 = {}
set_3 = {1, 2, 3, 3, 4, 5}

print(set_1)
print(set_2)
print(set_3)


#元素添加与删除
# 初始化一个空集合
my_set = set()

# 添加元素
my_set.add(1)  # {1}
my_set.add(2)  # {1, 2}
my_set.add(3)  # {1, 2, 3}

# 删除元素
my_set.remove(2)  # {1, 3}

print(my_set)

#集合的交集、并集与差集
# 定义两个集合
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 交集运算
intersection = set1.intersection(set2)
# 或者
# intersection = set1 & set2
print(f"交集: {intersection}")

# 并集运算
union = set1.union(set2)
# 或者
# union = set1 | set2
print(f"并集: {union}")

# 差集运算
difference1 = set1.difference(set2)
# 或者
# difference1 = set1 - set2
print(f"set1 和 set2 的差集: {difference1}")

difference2 = set2.difference(set1)
# 或者
# difference2 = set2 - set1
print(f"set2 和 set1 的差集: {difference2}")

#集合案例
# 两个实验中使用的激活函数
experiment1 = {"relu", "sigmoid", "tanh"}
experiment2 = {"relu", "softmax"}

# 找出两个实验中都使用过的激活函数
common_activations = experiment1.intersection(experiment2)
print(f"Common Activations: {common_activations}")

#字符串索引
# 示例字符串
string = "this_is_a_file.jpg"

# 获取字符串的第2到第5个字符（索引从0开始）
substring = string[1:5]  # 结果："his_"
print(substring)

# 获取字符串的第2到最后一个字符
substring = string[1:]  # 结果："his_is_a_file.jpg"
print(substring)

# 获取字符串的开始到第5个字符
substring = string[:5]  # 结果："this_"
print(substring)

# 获取整个字符串
substring = string[:]  # 结果："this_is_a_file.jpg"
print(substring)

# 获取字符串的最后3个字符
substring = string[-3:]  # 结果："jpg"
print(substring)

# 获取字符串的第2到倒数第3个字符
substring = string[1:-2]  # 结果："his_is_a_file.j"
print(substring)

# 获取字符串的第2到第3个字符，每隔2个字符取一个
substring = string[1:3:2]  # 结果："h"
print(substring)

# 反转字符串
substring = string[::-1]  # 结果："gpj.elif_a_si_sihT"
print(substring)


#字符串比较
# 定义两个字符串
string1 = "hello"
string2 = "hello"
string3 = "Hello"

# 使用 == 操作符比较字符串
is_equal = string1 == string2  # 结果：True
print(f"string1 is equal to string2: {is_equal}")

is_equal = string1 == string3  # 结果：False
print(f"string1 is equal to string3: {is_equal}")

# 使用 != 操作符比较字符串
is_not_equal = string1 != string2  # 结果：False
print(f"string1 is not equal to string2: {is_not_equal}")

# 使用 <, > 操作符比较字符串（基于字典顺序）
is_less_than = string1 < string2  # 结果：False
print(f"string1 is less than string2: {is_less_than}")

# 不区分大小写的字符串比较
is_equal_ignore_case = string1.lower() == string2.lower()  # 结果：True
print(f"string1 is equal to string2 (ignore case): {is_equal_ignore_case}")


#参数传递
# 形参是函数定义时的参数，实参是函数调用时的参数
def create_model(layers, units):  # layers和units是形参
    print(f"Creating a model with {layers} layers and {units} units in each layer.")

# 调用函数
create_model(3, 128)  # 3和128是实参


#位置参数
# 位置参数的顺序很重要
def create_model(layers, units):
    print(f"Creating a model with {layers} layers and {units} units in each layer.")

# 调用函数
create_model(3, 128)
create_model(128, 3)


#关键字参数
# 使用关键字参数调用函数
def create_model(layers, units):
    print(f"Creating a model with {layers} layers and {units} units in each layer.")

# 调用函数
create_model(units=128, layers=3)  # 使用关键字参数，顺序不重要
create_model(layers=3, units=128)

#默认参数
# 使用默认参数值
def create_model(layers=3, units=128):
    print(f"Creating a model with {layers} layers and {units} units in each layer.")

# 调用函数
create_model()  # 使用默认值

#可变参数
# 使用可变参数接收多个参数值
def add_layers(model, *layers):
    for layer in layers:
        print(f"Adding layer {layer} to model {model}.")

# 调用函数
add_layers("Model1", "conv", "relu", "softmax")

#函数返回值，通过return返回
# 函数返回模型的信息
def create_model(layers, units):
    info = f"Creating a model with {layers} layers and {units} units in each layer."
    return info

# 调用函数
model_info = create_model(3, 128)
print(model_info)

#变量作用域  全局变量
# 全局变量
MODEL_NAME = "CNN"

def print_model_name():
    print(f"The model name is {MODEL_NAME}.")

# 调用函数
print_model_name()



#变量作用域  局部变量
# 局部变量
def create_model():
    model_name = "RNN"  # 局部变量
    print(f"Creating a model named {model_name}.")

# 调用函数
create_model()

#print(model_name)  # 此行代码会报错

#匿名函数
# 使用lambda创建匿名函数
calculate_units = lambda layers: layers * 128

# 调用函数
units = calculate_units(3)
print(f"Total units: {units}")


#综合案例
def create_model(layers=3,units=128,activation="relu"):
    print(f"Creating a model with {layers} layers,each with {units} units and {activation} activation.")

# 调用函数
create_model()
create_model(4,256,"sigmoid")






"""







def create_cnn(input_size, kernel=3, padding=0, stride=1):
    """
    创建一个卷积神经网络层

    参数:
    - input_size: 输入图像的尺寸，形式为 (channels, height, width)
    - kernel: 卷积核的大小，默认为 3
    - padding: 填充大小，默认为 0
    - stride: 步长，默认为 1

    返回:
    - output_size: 卷积操作后输出图像的尺寸，形式为 (channels, height, width)
    """

    # 从输入尺寸中获取通道数和图像大小
    channels, height, width = input_size

    # 计算卷积操作后的输出图像尺寸
    new_height = ((height + 2 * padding - kernel) // stride) + 1
    new_width = ((width + 2 * padding - kernel) // stride) + 1

    # 输出图像的尺寸
    output_size = (channels, new_height, new_width)

    return output_size


# 示例用法:
input_size = (3, 64, 64)  # 3通道, 64x64的图像
output_size = create_cnn(input_size, kernel=3, padding=1, stride=2)
print(output_size)


































































































