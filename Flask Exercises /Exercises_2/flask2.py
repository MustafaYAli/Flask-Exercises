directory_path = "/Users/joey/Desktop/spring_2023/Software_eng/Flask Exercises/Exercises_2"

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            if num % 2 == 0:
                result = 'even'
            else:
                result = 'odd'
        except ValueError:
            try:
                float(request.form['number'])
                result = 'not an integer'
            except ValueError:
                result = 'not a number'

        if not request.form['number']:
            result = 'no number provided'
            return redirect(url_for('result', result=result))

        return render_template('result.html', result=result, number=request.form['number'])
    else:
        return render_template('home.html')


@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
