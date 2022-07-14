from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'qOVippE1KBWyBb/t0doA4Iv5eRFUauuVZ9a1+yzxLjo='


@app.route('/')
def start_page():
    """This function described the start page"""
    def counter():
        """This function will calculate and return the amount of sessions"""
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
        return str(session['counter'])
    if 'username' in session:
        return render_template('start_page.html', name=session['username'],
                               counter=int(counter()))
    else:
        return render_template('start_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """This function described the login page"""
    if 'username' not in session:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('start_page'))
        return render_template('login_page.html')
    else:
        return render_template('login_page.html', name=session['username'])


@app.route('/logout')
def logout():
    """This function described logout"""
    session.pop('username', None)
    session.pop('counter', None)
    return redirect(url_for('start_page'))


if __name__ == '__main__':
    app.run(debug=True)
