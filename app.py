#coding: utf-8
import os
from flask import Flask,render_template
from flask_flatpages import FlatPages

# Define global variables.
DEBUG = True
FLATPAGES_EXTENSION = ".md"
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route("/")
def index():
	sorted_pages = sorted(pages,reverse=True,
		key = lambda p: p.meta["date"] )
	return render_template("all.html",pages=sorted_pages,page = None)

@app.route("/<path:path>/detail/")
def detail(path):
    page = pages.get_or_404(path)
    title = u"%s" % page.meta["title"]
    return render_template('page.html', page=page,title=title)

@app.route("/tags/<tag_name>/")
def tags(tag_name):
    tag_pages = [page for page in pages if page.meta.get("tags") is not None]
    res = []
    for page in tag_pages:
        if tag_name in page.meta["tags"].split(","):
            res.append(page)

    sorted_pages = sorted(res,reverse=True,
    key = lambda p: p.meta["date"] )
    return render_template("all.html",pages=sorted_pages)









