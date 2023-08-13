from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.survey import Survey


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["Post"])
def submit_survey():
    if not Survey.val_form(request.form):
        return redirect("/")

    survey_id = Survey.create(request.form)
    return redirect(f"/{survey_id}")


@app.route("/<int:survey_id>")
def display_results(survey_id):
    survey = Survey.get_one(survey_id)
    return render_template("results.html", survey=survey)
