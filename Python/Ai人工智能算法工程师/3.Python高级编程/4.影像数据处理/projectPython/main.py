"""
import cv2

img_path = r'resources/food.png'

# 以彩色模式读取图片
image_color = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 以灰度模式读取图片
image_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# 显示图片
cv2.imshow('Color Image', image_color)
cv2.imshow('Grayscale Image', image_gray)

# 等待用户按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# 读取图片
image = cv2.imread('resources/food.png')

# 检查图片是否正确加载
if image is None:
    print("Error: Could not load image.")
    exit()

# 获取图片的原始尺寸
original_height, original_width = image.shape[:2]

# 计算新的尺寸
new_width = int(original_width / 2)
new_height = int(original_height / 2)

# 使用cv2.resize进行图片缩放
resized_image = cv2.resize(image, (new_width, new_height),
                           interpolation=cv2.INTER_AREA)

# 显示原始图片和缩放后的图片
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

# 等待用户按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

# 读取图片
image = cv2.imread('resources/food.png')

# 使用cv2.rotate()函数旋转图片
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 顺时针旋转90度
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)  # 顺时针旋转180度
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 顺时针旋转270度

cv2.imshow('original', image)
cv2.imshow('90 degree', rotated_90)
cv2.imshow('180 degree', rotated_180)
cv2.imshow('270 degree', rotated_270)
cv2.waitKey(0)

import cv2

def convert_and_show_image(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"无法加载图像: {image_path}")
        return

    # 显示原图
    cv2.imshow('Original Image', image)

    # 定义要转换的颜色空间和对应的标志
    color_spaces = {
        'Gray': cv2.COLOR_BGR2GRAY,
        'HSV': cv2.COLOR_BGR2HSV,
        'HLS': cv2.COLOR_BGR2HLS,
        'Lab': cv2.COLOR_BGR2Lab,
        'YCrCb': cv2.COLOR_BGR2YCrCb
    }

    # 遍历颜色空间并进行转换
    for color_space, flag in color_spaces.items():
        converted_image = cv2.cvtColor(image, flag)
        cv2.imshow(f'{color_space} Image', converted_image)

    # 等待用户按键，然后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 使用图像路径作为参数调用函数
convert_and_show_image('resources/food.png')



import cv2

# 读取图像
image = cv2.imread('input_image.png')

# 如果图像不为空，则保存图像
if image is not None:
    cv2.imwrite('output_image.png', image)
else:
    print("无法读取图像")


import cv2

# 创建一个 VideoCapture 对象，参数 0 表示使用默认的摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果读取成功，显示这一帧
    if ret:
        cv2.imshow('Frame', frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()


import cv2

# 定义视频捕获对象
cap = cv2.VideoCapture(0)

# 检查是否成功打开摄像头
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# 获取摄像头的帧宽度和帧高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定义视频编码器和输出文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 或者使用 'XVID'
out = cv2.VideoWriter('output.mp4', fourcc, 20.0,
                      (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # 将当前帧写入输出视频文件
    out.write(frame)
    # 显示当前帧
    cv2.imshow('frame', frame)
    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()



import cv2
import numpy as np


def add_gaussian_noise(image):
    row, col = image.shape
    mean = 0
    sigma = 15
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy = image + gauss
    noisy_img = np.clip(noisy, 0, 255)
    return noisy_img.astype(np.uint8)


# 输入和输出视频文件名
input_video = 'resources/outdoor.mp4'
output_video = 'resources/output.mp4'

# 打开输入视频
cap = cv2.VideoCapture(input_video)

# 获取视频的帧率和帧大小
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 计算新的帧大小 (540p)
new_height = 540
new_width = int((new_height / frame_height) * frame_width)

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, new_height), isColor=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 调整帧大小
    frame = cv2.resize(frame, (new_width, new_height))

    # 转换为灰度图像
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 垂直翻转画面
    frame = cv2.flip(frame, 1)

    # 添加高斯噪声
    frame = add_gaussian_noise(frame)

    # 写入输出视频
    out.write(frame)

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

"""



























































































