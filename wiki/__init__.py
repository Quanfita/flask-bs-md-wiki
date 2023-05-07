from .application import app
from .views import IndexView, PageView

app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/<path:path>', view_func=PageView.as_view('page'))
