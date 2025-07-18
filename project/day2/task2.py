# 用函数封装输出 1~9 的乘法表

def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{j} * {i} = {i*j}', end='\t')
        print()
# 测试代码
if __name__ == "__main__":
    multiplication_table()
    # 输出：
    # 1 * 1 = 1
    # 1 * 2 = 2
    # 2 * 2 = 4
    # ...
    # 9 * 9 = 81