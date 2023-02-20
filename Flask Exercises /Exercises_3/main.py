from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded list of student organizations
organizations = ['Organization 1', 'Organization 2', 'Organization 3', 'Organization 4', 'Organization 5']

# Global dictionary to store registered users
registered_users = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from form
        name = request.form['name']
        organization = request.form['organization']

        # Backend form validation
        if not name:
            error = 'Name is required.'
            return render_template('index.html', organizations=organizations, error=error)

        if not organization:
            error = 'Organization is required.'
            return render_template('index.html', organizations=organizations, error=error)

        if organization not in organizations:
            error = 'Invalid organization.'
            return render_template('index.html', organizations=organizations, error=error)

        # Add user to dictionary
        registered_users[name] = organization

        # Redirect to list of registered users
        return redirect(url_for('users'))

    # Render form on GET request
    return render_template('index.html', organizations=organizations)


@app.route('/users')
def users():
    # Render list of registered users
    return render_template('users.html', registered_users=registered_users)


if __name__ == '__main__':
    app.run(debug=True)
