import os
import tex2pix
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    document = """
\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{graphicx}
\graphicspath{{/tmp/}}
\begin{document}

What is the minimum number of small squares that must be colored black so that a line of symmetry lies on the diagonal $ \overline{BD}$ of square $ ABCD$? (2008 AMC 8 \#3) \\
\includegraphics[height=2.5cm]{2005AMC8n3.png}
\end{document}
"""
    renderer = tex2pix.Renderer(document)
    renderer.mkpdf('/tmp/output.pdf')
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
