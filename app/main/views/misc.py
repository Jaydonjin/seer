from flask import render_template

from app.main import main


@main.route("/faq.htm")
def faq():
    return render_template('main/faq.html')
