import numpy as np
import random
sum = []
n = 10
for r in range(n):
    sum.append([])
    for c in range(n):
        sum[r].append(random.randint(0, n))
        # 'r'+str(r)+'c' + str(c) = sheets.cell(r, c).value

matrix = np.array(sum)

result = np.linalg.eig(matrix)

print("本征值为：\n", result[0], "\n本征向量为：\n", result[1])

