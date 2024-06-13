#coding:utf-8
import os
import pikepdf

# 1 个用法
def unlock(document):
    pdf = pikepdf.open(document, allow_overwriting_input=True)
    pdf.save(document)

documents = os.listdir('.') # 当前目录下所有文件
for document in documents:
    if os.path.splitext(document)[1] == '.pdf': # 判断文件后缀名
        unlock(document)
        print(document, 'is unlocked')


