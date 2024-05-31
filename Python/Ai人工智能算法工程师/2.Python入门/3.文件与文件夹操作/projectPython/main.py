"""
import shutil

file_1_loc = 'D:/桌面/文件与文件夹操作_yolo数据清洗_代码与数据集/resources/保存目录1/fire.jpg'
file_1_save_loc = 'D:/桌面/文件与文件夹操作_yolo数据清洗_代码与数据集/resources/保存目录2/fire_copy.jpg'
shutil.copyfile(file_1_loc, file_1_save_loc)


import shutil

# 源目录和目标目录
src = 'resources/fire_yolo_format'
dst = 'resources/fire_yolo_format_new_1'

# 使用copytree复制目录
shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.txt"))
#使用 shutil.ignore_patterns 函数创建一个忽略模式，
#该模式会忽略所有与给定模式（在本例中是 "*.txt"）匹配的文件。这样，所有 .txt 文件都不会被复制到目标目录

print(f"Directory copied from {src} to {dst}")


#移动文件
import shutil

file_1_loc = 'resources/保存目录1/fire_label.txt'
file_1_save_loc = 'resources/保存目录2/fire_label.txt'
shutil.move(file_1_loc, file_1_save_loc)



#删除文件
import os

file_loc = r'resources/保存目录1/fire.jpg'

os.remove(file_loc)


#创建一级目录
import os

dir_name = "resources/一级目录"
if os.path.exists(dir_name):
    print("文件夹已经存在！")
else:
    os.mkdir(dir_name)
    print("文件夹已经创建完毕！")



#创建多级目录
import os
os.makedirs(r"resources/多级目录1/多级目录2/多级目录3")


#遍历文件夹
import os

root_dir = "D:/桌面/文件与文件夹操作_yolo数据清洗_代码与数据集/"

file_full_path_list = []
for root, dirs, files in os.walk(root_dir):
#os.walk函数会生成一个三元组 (root, dirs, files)
#root 是当前正在遍历的目录路径
#dirs 是一个列表，包含当前目录中子目录的名字
#files 是一个列表，包含当前目录中文件的名字
    for file_i in files:
        #循环遍历当前目录 (root) 中的每个文件 (files 列表中的元素)
        file_i_full_path = os.path.join(root, file_i)
        #使用 os.path.join 函数将目录路径 (root) 和文件名 (file_i) 连接起来，得到文件的完整路径 (file_i_full_path)
        file_full_path_list.append(file_i_full_path)
        #将文件的完整路径添加到 file_full_path_list 列表中
print(file_full_path_list)

#删除空文件夹
import os

dir_path = r'resources/一级目录'

if os.path.exists(dir_path):
    print("删除文件夹"+dir_path)
    os.rmdir(dir_path)
    print("删除完成")
else:
    print("文件夹"+dir_path+"不存在")

#删除非空文件夹
import os
import shutil

dir_name = "resources/多级目录1"
if os.path.exists(dir_name):
    shutil.rmtree(dir_name) # 文件夹里有东西也一并删除
    print("文件夹已经删除！")
else:
    os.mkdir(dir_name)
    print("文件夹不存在！")

"""




# 训练一个人工智能算法需要一个庞大的数据集，这个数据集需要进行人为标注。
# 但由于出现意外，造成部分数据丢失，使得标注文件和图片文件的文件名前缀不能一一对应。
# 需要写一段代码，将可以文件名前缀一一对应的文件保存到一个新的文件夹中，以完成数据的清洗。

import os
import shutil
#例如这个文件的目录\\resources\\fire_yolo_format\\images\\test\\很多图片文件
#1、file_i遍历test目录下图片的文件名，然后与目录"\\resources\\fire_yolo_format\\images\\test\\"
#拼接到一起。最终形成例如：\\resources\\fire_yolo_format\\images\\test\\1.jpg
#2、使用\\将这个目录结构分隔开：['resources', 'fire_yolo_format', 'images', 'test', '1.jpg']
#3、列表的倒数第二个和最后一个元素拼接成一个新的路径。例如：\\test\\1.jpg
#4、"."是为了分割成：['test\\1', 'jpg']得到一个新的列表
#5、取这个列表的第一个元素 [0]，即 'test\\1'

def get_info(root_from):
    file_full_path_list = []
    for root, dir, files in os.walk(root_from):
        for file_i in files:
            file_i_full_path = os.path.join(root, file_i)

            file_i_full_path_list = file_i_full_path.split('\\')

            file_i_short_path = os.path.join(file_i_full_path_list[-2], file_i_full_path_list[-1])

            file_i_name = file_i_short_path.split('.')[0]

            file_full_path_list.append(file_i_name)


    return file_full_path_list

#清洗前的路径
root_path_from = r'resources/fire_yolo_format'
#清洗后的路径
root_path_save = r'resources/clean_data'

#拼接清洗前的路径+images=resources/fire_yolo_format/images
#拼接清洗前的标签+labels=resources/fire_yolo_format/labels
root_images_from = os.path.join(root_path_from, 'images')
root_labels_from = os.path.join(root_path_from, 'labels')

#拼接清洗后的路径+images=resources/fire_yolo_format/images
#拼接清洗后的标签+labels=resources/fire_yolo_format/labels
root_images_save = os.path.join(root_path_save, 'images')
root_labels_save = os.path.join(root_path_save, 'labels')

print(root_images_from)
print(root_labels_from)
print(root_images_save)
print(root_labels_save)

dir_list_1 = ['images', 'labels']
dir_name_list = ['train','test', 'val']


#创建新的目录/resources/clean_data/images/train
for dir_1_i in dir_list_1:
    for dir_2_i in dir_name_list:
        dir_i_full_path = os.path.join(root_path_save, dir_1_i, dir_2_i)
        if not os.path.exists(dir_i_full_path):
            os.makedirs(dir_i_full_path)


#调用get_info函数将拼接前的路径resources/fire_yolo_format/images
#取短路径。例如：'test\1'
image_full_path_list = get_info(root_images_from)
print(image_full_path_list)

#调用get_info函数将拼接前的路径resources/fire_yolo_format/labels
#取短路径。例如：'test\1'
label_full_path_list = get_info(root_labels_from)
print(label_full_path_list)




#取交集，图片名和文件名有一致性
#例如：'test\1'
image_set = set(image_full_path_list)
label_set = set(label_full_path_list)

intersection_set = image_set & label_set
print(len(image_set))
print(len(label_set))
print(len(intersection_set))

print(intersection_set)




for intersection_i in intersection_set:
    intersection_i_image_full_path_from = os.path.join(root_images_from, intersection_i) + '.jpg'
    # print(intersection_i_image_full_path)
    intersection_i_label_full_path_from = os.path.join(root_labels_from, intersection_i) + '.txt'
    # print(intersection_i_label_full_path)

    intersection_i_image_full_path_save = os.path.join(root_images_save, intersection_i) + '.jpg'

    intersection_i_label_full_path_save = os.path.join(root_labels_save, intersection_i) + '.txt'

    shutil.copy(intersection_i_image_full_path_from, intersection_i_image_full_path_save)
    shutil.copy(intersection_i_label_full_path_from, intersection_i_label_full_path_save)






















































































