import os
from flask import Flask, Markup, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', current='index', user='Tushar Pankaj')

@app.route('/<page>/')
def go_to(page):
    page = linkname(page)
    pages = list()
    pages.append('about')
    pages.append('contact')
    for pageiterator in pages:
        if page == pageiterator:
            return render_template('pages/%s.html' % page, current=page, user='Tushar Pankaj')
    abort(404)

def linkname(title):
  title = title.strip()
  title = ''.join(c for c in title if c.isalnum() or c.isspace() or c == '-')
  return title.lower().replace(' ', '-')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
