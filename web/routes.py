from web import app
from flask import render_template


@app.route("/")
@app.route("/plotly")
def plot_plotly_global():
    # total confirmed cases globally

    return render_template("plotly.html")
