import os
from flask import Flask, Markup, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', current='index')

@app.route('/profile/')
def profile():
    return render_template('system/profile.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('system/register.html')

@app.route('/signin/', methods=['POST'])
def signin():
    if validateuser(username=request.form['user[username]'], password=request.form['user[password]']):
        return render_template('system/signin.html', user=request.form['user[username]'])
    else:
        return render_template('system/signin.html', failed=True)

@app.route('/signout/')
def signout():
    return render_template('system/signout.html')

@app.route('/<page>/')
def go_to(page):
    page = linkname(page)
    pages = list()
    pages.append('about')
    pages.append('contact')
    for pageiterator in pages:
        if page == pageiterator:
            return render_template('pages/%s.html' % page, current=page)
    abort(404)

def linkname(title):
  title = title.strip()
  title = ''.join(c for c in title if c.isalnum() or c.isspace() or c == '-')
  return title.lower().replace(' ', '-')

def validateuser(username, password):
    return True;

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
