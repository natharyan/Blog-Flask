from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail 
import json
import os
from datetime import datetime
import pymysql
pymysql.install_as_MySQLdb()

local_server = True
with open('config.json','r') as c:
    params = json.load(c)["params"]

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-AppPassword']
)
mail = Mail(app)
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db.init_app(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    slug = db.Column(db.String(12), nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().limit(params['no_of_posts']).all()
    return render_template('index.html', params = params, posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', params = params)

@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params = params, posts = posts)
    if request.method == 'POST':
        # redirect to admin panel
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_user'] and userpass == params['admin_password']:
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params = params, posts = posts)
    
    return render_template('login.html', params = params)

@app.route("/edit/<string:sno>", methods = ['GET','POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            author = request.form.get('author')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            if sno=='0':
                post = Posts(title = title, author = author, slug = slug, content = content, img_file = img_file, date = date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title = title
                post.author = author
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/' + sno)
        post = Posts.query.filter_by(sno = sno).first()
        return render_template('edit.html', params = params, post = post)
    return "<h3>Please log in and try again</h3>"

@app.route("/uploader", methods = ['GET','POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Successfully"

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name = name, phone_num = phone, msg = message, date = datetime.now(), email = email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from Blog', sender = email, recipients = [params['gmail-user']], body = 'name: ' + name + '\n' + 'message:' + '\n' + message + '\n' + 'phone: ' + phone)
    return render_template('contact.html', params = params)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html', params = params, post = post)

app.run(debug=True)