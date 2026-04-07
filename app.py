from flask import Flask, request, redirect

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    content = "<h1>My DevOps Blog</h1>"
    content += "<form method='POST' action='/add'>"
    content += "<input name='post' placeholder='Write something'>"
    content += "<button>Add</button></form><hr>"

    for p in posts:
        content += f"<p>{p}</p>"

    return content

@app.route('/add', methods=['POST'])
def add():
    post = request.form['post']
    posts.append(post)
    return redirect('/')

app.run(host='0.0.0.0', port=5000)
