# -*- coding: UTF-8 -*-
import os
import xlwt
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
fp = book.add_sheet('test', cell_overwrite_ok=True)
path = 'C:/Users/24643/Desktop/测试'
n = 0
for root, dirs, files in os.walk(path, True):
    # print('root: %s' % root)
    # print('dirs: %s' % dirs)
    # print('files: %s' % files)
    # print('')
    # for name in dirs:
    #     # print(os.path.join(root, name))
    #     if os.path.split(name)[1] == "Numpy练习":
    #         fp.write(n, 0, name)   # 行 列 数值
    #         n += 1

    for name in files:
        # print(os.path.join(root, name))
        if os.path.splitext(name)[1] == ".pdf":
            fp.write(n, 0, name)   # 行 列 数值
            n += 1
book.save('index.xls')

