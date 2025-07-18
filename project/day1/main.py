'''
2. 编写程序，实现：

   - 输入若干学生姓名与分数
   - 计算总分，排序后打印成绩排名
'''

dict = {}
sign = 0
while not sign:
    name = input('请输入学生姓名:\n')
    point = input('请输入该学生分数:\n')
    stop = input('是否还要输入下一个[Y/N]')
    if stop == 'N':
        sign = 1
    dict[name] = int(point)

n = len(dict)
sum = sum(dict.values())
medium = sum / n
print('平均分数为:', medium)
sorted_students = sorted(dict.items(), key=lambda x: x[1], reverse=True)

print("\n学生成绩排名:")
for i, (name, score) in enumerate(sorted_students, 1):
    print(f"{i}. {name}: {score}分")

