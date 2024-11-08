from flask import Flask, request, render_template

app =Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return render_template('success.html',name=name)
    return render_template('register.html')

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)