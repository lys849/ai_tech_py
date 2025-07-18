from pathlib import Path
path = Path('./project/day3/todo.txt')

from todo_core import show_items, add_aitems, delete_items

show_items(path)
add_aitems(path)
show_items(path)
delete_items(path,3)
show_items(path)
