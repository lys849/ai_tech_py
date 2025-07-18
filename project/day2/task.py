# 简要说明：
# 输入 abc123xy45 -> 输出 数字个数：5，总和：15

def count_digits_and_sum(s):
    digit_count = 0
    digit_sum = 0
    
    for char in s:
        if char.isdigit():
            digit_count += 1
            digit_sum += int(char)
    
    return f"数字个数：{digit_count}，总和：{digit_sum}"

# 测试代码
if __name__ == "__main__":
    input_string = "abc123xy45"
    result = count_digits_and_sum(input_string)
    print(result)  # 输出：数字个数：5，总和：15