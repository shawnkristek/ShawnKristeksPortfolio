from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import Markup
from werkzeug.exceptions import abort

from smk.auth import login_required
from smk.db import get_db

bp = Blueprint("blog", __name__, url_prefix="/blog")

@bp.route("/")
def blog():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        "SELECT p.id, author_id, parent_id, title, meta_title, slug, summary, published, created_at, updated_at, published_at, content, img, username, firstname, lastname"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created_at DESC"
    ).fetchall()
    return render_template("blog/feed.html", posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = (
        get_db()
        .execute(
            "SELECT p.id, author_id, parent_id, title, meta_title, slug, summary, published, created_at, updated_at, published_at, content, img, username, firstname, lastname"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,)
        )
        .fetchone()
    )

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        summary = request.form["summary"]
        slug = request.form["slug"]
        img = request.form["img"]
        error = None

        if not title:
            error = "Title is required."
        if not slug:
            slug = title.lower().replace(' ','-')
        if not summary:
            error = "Summary is required." 
        if not img:
            img = "img/my-hero-bg.jpg"
        if not content:
            error = "Content is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, content, summary, slug, img, author_id) VALUES (?, ?, ?, ?, ?, ?)",
                (title, content, summary, slug, img, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("blog.blog"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        img = request.form["img"]
        slug = request.form["slug"]
        summary = request.form["summary"]
        error = None

        if not title:
            error = "Title is required."
        if not content:
            error = "Content is required."
        if not img:
            error = "Img is required."
        if not summary:
            error = "Summary is required."
        if not slug:
            error = "Slug is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, content = ? , img = ?, slug = ?, summary = ? WHERE id = ?", (title, content, img, slug, summary, id)
            )
            db.commit()
            return redirect(url_for("blog.blog"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.blog"))

@bp.route("/<int:id>/<slug>", methods=("GET",) )
def post(id, slug):
    """Display a post.
    Ensures that the post exists.
    """
    post = get_post(id, False)
    content = Markup(post['content'])
    return render_template("blog/post.html", post=post, content=content)
