from flask import render_template
from flask.views import MethodView
from markdown import markdown
from config import MD_DIR, HOME_PAGE
from .utils import generate_file_tree
import os


class IndexView(MethodView):
    def get(self):
        with open(os.path.join(MD_DIR, HOME_PAGE), 'r', encoding='utf-8') as f:
            text = f.read()
        content = markdown(text)
        menu_tree = generate_file_tree(MD_DIR)
        print(menu_tree)
        return render_template('base.html', content=content, menu_tree=menu_tree)

class PageView(MethodView):
    def get(self, path):
        with open(os.path.join(MD_DIR, path + '.md'), 'r', encoding='utf-8') as f:
            text = f.read()
        content = markdown(text)
        menu_tree = generate_file_tree(MD_DIR)
        print(menu_tree)
        return render_template('base.html', content=content, menu_tree=menu_tree, path=path, path_first=path.split('/')[0])
