import numpy as np
import xlrd

book = xlrd.open_workbook(r'numpy.xlsx')

sheets = book.sheet_by_index(0)
nrows = sheets.nrows
ncols = sheets.ncols

sum = []

for r in range(nrows):
    sum.append([])
    for c in range(ncols):
        sum[r].append(sheets.cell(r, c).value)
        # 'r'+str(r)+'c' + str(c) = sheets.cell(r, c).value

matrix = np.array(sum)

result = np.linalg.eig(matrix)

print("本征值为：\n", result[0], "\n本征向量为：\n", result[1])

