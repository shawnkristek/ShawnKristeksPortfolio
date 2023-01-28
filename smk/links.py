from flask import Blueprint
from flask import redirect, url_for

bp = Blueprint("links", __name__)

#-----------------------------------------------------    
# External links
#-----------------------------------------------------    
@bp.route('/email')
def email():
    return redirect("mailto:shawn@shawnkristek.com")

@bp.route('/linkedin')
def linkedin():
    return redirect("https://www.linkedin.com/in/shawnkristek")

@bp.route('/stackoverflow')
def stackoverflow():
    return redirect("https://stackoverflow.com/users/14810598/shawn-kristek")

@bp.route('/github')
def github():
    return redirect("https://github.com/shawnkristek")

@bp.route('/codepen')
def codepen():
    return redirect("https://codepen.io/bswole")

@bp.route('/repl')
def repl():
    return redirect("https://repl.it/@ShawnKristek")

@bp.route('/freecodecamp')
def freecodecamp():
    return redirect("https://www.freecodecamp.org/bswole")

@bp.route('/facebook')
def facebook():
    return redirect("https://www.facebook.com/shawn.kristek")

@bp.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/b.swole")

@bp.route('/luv')
def luv():
    return redirect("https://loveyoulater.productions")

@bp.route('/skull')
def skull():
    return redirect("https://www.skullyum.com")

@bp.route('/wertz')
def wertz():
    return redirect("https://www.wertzwerkz.net")

@bp.route('/bswole')
def bswole():
    return redirect("https://www.bswole.com")

@bp.route('/pdfresume')
def pdfresume():
    return redirect("https://bit.ly/shawnkristek-swe-resume")