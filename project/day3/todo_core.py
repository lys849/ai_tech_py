def show_items(path):
    contents = path.read_text().strip()
    lines = contents.splitlines()
    for i, line in enumerate(lines,1):
        print(str(i)+'.'+line)

def add_items(path):
    add_todo = input('请输入添加的任务：').strip()
    with path.open('a', encoding='utf-8') as f:
        f.write(f'{add_todo}\n')


def delete_items(path, index):
    contents = path.read_text().strip()
    lines = contents.splitlines()
    if 1 <= index <= len(lines):
        deleted = lines.pop(index - 1)
        print(f'{index}. {deleted} 被删除')
        path.write_text('\n'.join(lines))
    else:
        print(f'错误：任务编号 {index} 不存在')
