from flask import Flask, request, render_template

app = Flask(__name__)
rews = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rews.append({'name': request.form.get('name'),
                     'text': request.form.get('text')})
    name2 = request.args.get('n')
    return render_template('index.html', rews=rews, name2=name2)


if __name__ == '__main__':
    app.run(debug=True)