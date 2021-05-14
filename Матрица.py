# Input lines:
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15

matrix = list()
for i in range(1, 5):
    matrix.append(input())
for j in matrix:
    out_line = list()
    split_line = j.split()
    for k in split_line:
        out_line.append(int(k) ** 2)
    print(out_line)
