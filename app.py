#coding: utf-8
import os
from flask import Flask,render_template,redirect,url_for
from flask_flatpages import FlatPages,pygments_style_defs
from flask import g
import datetime

DEBUG = True
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

def title(title = None):
	if title is None:
		return 'none'
	return title

app.jinja_env.globals['title'] = title

@app.route("/")
def index():
	sorted_pages = sorted(pages,reverse=True,
		key = lambda p: p.meta["date"] )

	return render_template("all.html",pages=sorted_pages,page = None)

#  続きを読む
@app.route("/<path:path>/detail/")
def detail(path):
    page = pages.get_or_404(path)
    title = u"%s" % page.meta["title"]
    app.jinja_env.globals['title'] = title
    page.meta["path"] = path
    return render_template('page.html', page=page,title=title)

@app.route("/tags/<tag_name>/")
def tags(tag_name):
    # タグのあるページだけを取得
    tag_pages = [page for page in pages if page.meta.get("tags") is not None]
    res = []
    for page in tag_pages:
        if tag_name in page.meta["tags"].split(","):
            res.append(page)

    sorted_pages = sorted(res,reverse=True,
    key = lambda p: p.meta["date"] )
    return render_template("all.html",pages=sorted_pages)









