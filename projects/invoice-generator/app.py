from weasyprint import HTML
from flask import Flask, render_template
import os
from datetime import datetime

html = HTML('invoice.html')
html.write_pdf('invoice.pdf')

app = Flask(__name__)

@app.route('/')
def hello_world():
    today = datetime.today().strftime("%B %-d, %Y")
    return render_template('invoice.html',
                           date = today)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)