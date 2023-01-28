import os
from flask import Flask, url_for, redirect, render_template, request, flash, send_from_directory
from flask_mail import Message, Mail
from forms import ContactForm
from json import load
from box import Box
from config import config

config_name = None
"""Create and configure an instance of the Flask application."""
app = Flask(__name__, instance_relative_config=True)
# load the instance config, if it exists, when not testing
# app.config.from_pyfile("config.py", silent=True)
if config_name == None:
    config_name = 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# store the database in the instance folder
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, "smk.sqlite")
)

# register the database commands
import db
db.init_app(app)

#----------------------------------------------------
# import JSON file object for dynamic portfolio
#----------------------------------------------------
with open('static/js/db.json') as f:
    box_db = Box(load(f))

# apply the blueprints to the app
import auth, blog, links
app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)
app.register_blueprint(links.bp)

# APP routes
# Website Internal routes
@app.route('/', methods=['GET','POST'])
def index():
    form = ContactForm()

    if form.is_submitted():
        if form.validate():
            flash("Message sent.")
            msg = Message(  subject = "Got your message!", 
                            sender=('Shawn Kristek','shawn@shawnkristek.com'), 
                            recipients=[form.email.data],
                            cc=['shawn@shawnkristek.com'],
                            reply_to='shawn@shawnkristek.com'
                            )
            msg.body = """
            Dear %s,
            
            Thank you for reaching out to me. 
            
            Your subject:
            %s
            Your message:
            %s
            
            Talk soon,
            Shawn Kristek
            Full Stack Engineer and Developer
            shawn@shawnkristek.com""" % (form.name.data, form.subject.data, form.message.data)
            mail.send(msg)
            
    return render_template('index.html',
                            projects=box_db.projects,
                            resume=box_db.resume,
                            skills=box_db.skills,
                            challenges=box_db.challenges,
                            form=form)

#-----------------------------------------------------    
# Contact Form Links
#-----------------------------------------------------    
@app.route('/contact')
def contact():
    return redirect('/#contact')

#-----------------------------------------------------    
# Project Links
#-----------------------------------------------------    
@app.route('/project/<project_id>')
def project(project_id):
    return render_template('resume/project-details.html', proj=box_db.projects[int(project_id)])

#-----------------------------------------------------    
# Challenge Links
#-----------------------------------------------------    
@app.route('/challenge/<challenge_id>')
def challenge(challenge_id):
    return render_template('resume/challenge-details.html', challenge=box_db.challenges[int(challenge_id)])

@app.route('/quotes')
def quotes():
    return render_template('quotivation/quotes.html')

@app.route('/resume')
def resume():
    return send_from_directory('static',filename='files/resume.pdf')
