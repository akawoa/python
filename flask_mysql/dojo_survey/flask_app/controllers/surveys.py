from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.survey import Survey

@app.route('/')
def survey_index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def create_survey():
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"]
    }

    if not Survey.validate_survey(data):
        return redirect('/')
    Survey.save(data)
    return redirect('/surveys')

@app.route('/surveys')
def view_all():
    surveys = Survey.get_all()
    print(surveys)
    return render_template('result.html', all_surveys = surveys)