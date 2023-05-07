import os

def is_md(filename):
    return filename.split('.')[-1] == 'md'


def generate_file_tree(root_dir):
    file_tree = {}
    root = root_dir.split(os.sep)[-1]
    for t_root, dirs, files in os.walk(root_dir):
        tmp_tree = {}
        t_root = t_root.split(os.sep)[-1]
        tmp_tree[t_root] = ['.'.join(file.split('.')[:-1]) for file in files if is_md(file)]
        if not file_tree:
            file_tree = tmp_tree
        else:
            file_tree[root].append(tmp_tree)
    return file_tree[root]