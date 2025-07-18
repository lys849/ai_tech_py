# 示例输入：calculator(4, 5, "+") -> 输出 9
def calculator(num1, num2, operation):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "输入必须是数字"
    if not isinstance(operation, str):
        return "操作必须是字符串"
    
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "除数不能为零"
    else:
        return "无效的操作"
    

# 测试代码
if __name__ == "__main__": 
    print(calculator(4, 5, "+"))  # 输出：9
    print(calculator(10, 2, "-"))  # 输出：8
    print(calculator(3, 7, "*"))   # 输出：21
    print(calculator(8, 2, "/"))   # 输出：4.0
    print(calculator(8, 0, "/"))   # 输出：除数不能为零
    print(calculator(8, "a", "+")) # 输出：输入必须是数字
    print(calculator(8, 2, "x"))   # 输出：无效的操作