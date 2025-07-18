# 示例：madam -> True，"A man a plan a canal Panama" -> True
def is_palindrome(s):
    # 移除非字母数字字符并转换为小写
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # 检查清理后的字符串是否是回文
    return cleaned == cleaned[::-1]

# 测试函数
if __name__ == "__main__":
    test_strings = [
        "madam",
        "A man a plan a canal Panama",]
    for test in test_strings:
        result = is_palindrome(test)
        print(f'"{test}" is a palindrome: {result}')