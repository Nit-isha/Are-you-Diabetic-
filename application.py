
from flask import Flask, render_template, request
from Main import Check

application = Flask(__name__)


@application.route("/", methods=['GET'])
def index_get():
    return render_template('index.html', msg='')


@application.route('/', methods=['POST'])
def index_post():
    pregnancy = request.form.get('pregnancy')
    glucose = request.form.get('glucose')
    bp = request.form.get('bp')
    skin = request.form.get('skin')
    insulin = request.form.get('insulin')
    BMI = request.form.get('BMI')
    dbf = request.form.get('dbf')
    Age = request.form.get('Age')

    data = (pregnancy, glucose, bp, skin, insulin, BMI, dbf, Age)
    msg = Check(data)

    return render_template('index.html', msg=msg)


if __name__ == "__main__":
    application.run(debug=True)
