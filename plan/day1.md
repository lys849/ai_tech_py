# 第 1 天任务 — Python 基础语法与学生成绩统计

## 目标

- 熟悉 Python 基础语法（变量、数据类型、输入输出）
- 编写第一个小程序：学生成绩录入与总分排名

## 任务内容

1. 复习基础语法（变量、字符串、数字、input 函数）  
   推荐资料：B 站 Python 入门视频前 30 分钟或书籍对应章节

2. 编写程序，实现：

   - 输入若干学生姓名与分数
   - 计算总分，排序后打印成绩排名

3. 运行测试，调试程序，输出结果截图

## 练习目标

- 掌握数据类型和输入输出
- 学会使用字典存储和排序数据

## 代码示例参考（可自由修改）

```python
# 学生成绩统计器示例
students = {}
n = int(input("请输入学生人数: "))
for _ in range(n):
    name = input("请输入学生姓名: ")
    score = int(input("请输入学生分数: "))
    students[name] = score

# 按分数排序
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("\n学生成绩排名：")
for i, (name, score) in enumerate(sorted_students, 1):
    print(f"{i}. {name}: {score}分")
```
