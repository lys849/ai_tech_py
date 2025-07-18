以下是更新后的 **Day 3 完整版 `.md` 文件内容**，已经集成了当日的 Python 内置函数 mini 训练系列内容 ✅

---

````markdown
# 🚀 Python 提升计划 · Day 3

## 🎯 今日目标

- 掌握文件读写基础（打开、读取、写入、追加）
- 学会封装功能到模块中并导入使用
- 实战构建“代办事项管理器”程序
- 熟练掌握 5 个常用 Python 内置函数的语法与应用场景

---

## 📘 学习内容总结

### ✅ 文件操作

| 操作类型 | 示例代码                                                    |
| -------- | ----------------------------------------------------------- |
| 读取文件 | `with open('file.txt', 'r') as f:`<br>`content = f.read()`  |
| 按行读取 | `f.readlines()`                                             |
| 写入文件 | `with open('file.txt', 'w') as f:`<br>`f.write("内容")`     |
| 追加写入 | `with open('file.txt', 'a') as f:`<br>`f.write("追加内容")` |

### ✅ 模块导入与组织

```python
# todo_core.py
def add_item(item): ...
def show_items(): ...
def delete_item(index): ...

# main.py
from todo_core import add_item, show_items
```
````

---

## 🛠 实战任务记录

### ✅ 任务 1：代办事项管理器

```text
功能：
- 添加待办事项
- 查看事项
- 删除事项
- 数据保存在本地文件 todo.txt
```

#### 我的实现代码（函数划分）：

- `add_item()`:
- `show_items()`:
- `delete_item()`:

#### 测试样例输出：

```
1. 学 Python
2. 完成 Day 3 计划
```

---

### ✅ 任务 2：模块拆分练习

```text
todo_core.py 与 main.py 分离代码，封装逻辑
```

- 是否成功导入模块：✅/❌
- 出现的问题及解决方案：

---

### ✅ 任务 3（选做）：歌词逐行打印

```text
- 读取文件，每行加 🎵 输出
- 可去除空行 / 空格 / 行号标注
```

#### 我的代码实现：

...

---

## 🧠 学习反思与总结

- 遇到的问题（如：编码问题、路径不正确、模块导入失败）：
- 最有成就感的部分：
- 是否尝试封装复用代码？
- 是否尝试使用 try/except 捕获错误？

---

## 🔧 Python 内置函数 mini 训练 · Day 3 配套练习

### 📘 今日函数学习清单（5 个）

| 函数          | 功能简介                                     |
| ------------- | -------------------------------------------- |
| `open()`      | 打开文件进行读写                             |
| `strip()`     | 去除字符串前后空白符                         |
| `split()`     | 拆分字符串成列表                             |
| `join()`      | 将列表拼接为字符串                           |
| `enumerate()` | 获取元素及索引（常用于打印带编号的待办事项） |

---

### ⚡ 使用示例

```python
# 1. open()
with open('todo.txt', 'r') as f:
    content = f.read()

# 2. strip() + split()
line = "   Learn Python  "
line.strip()  # "Learn Python"
sentence = "a,b,c"
sentence.split(',')  # ['a', 'b', 'c']

# 3. join()
items = ['a', 'b', 'c']
",".join(items)  # 'a,b,c'

# 4. enumerate()
todos = ['study', 'eat']
for idx, item in enumerate(todos, 1):
    print(f"{idx}. {item}")
```

---

### 🧠 mini 训练题（建议独立完成）

#### 练习 1：读取并打印编号待办事项

```python
# 读取 todo.txt，每行一个事项，加编号输出：
# 示例输出：
# 1. Learn Python
# 2. Finish homework
```

#### 练习 2：将用户输入的事项追加到文件中

```python
# 使用 input() 获取输入，并写入 todo.txt（追加模式）
# 输入示例：Write markdown summary
```

#### 练习 3：读取文件，去除空行和前后空格后打印

```python
# 文件可能存在空行或多余空格，处理后输出整洁的事项列表
```

---

## 📅 明日预告（Day 4）

- 掌握：**列表推导式、lambda 表达式、生成器**
- 提升代码简洁性与表达力，写出更 Pythonic 的表达！

---

> 每天进步 1%，30 天后你将比现在强大很多 💪
> —— 持续练习，保持节奏！

```

---

你可以将它保存为 `day3_plan.md`。
如果你需要我把每天的 `.md` 自动整理为文件、压缩包、或者推送到 GitHub，都可以告诉我，我来帮你实现自动化！🔥
```
