from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fitness.auth import login_required
from fitness.db import get_db

bp = Blueprint('diary', __name__)

@bp.route('/')
def index():
#    db = get_db()
#    posts = db.execute(
#        'SELECT p.id, title, body, created, author_id, username'
#        ' FROM post p JOIN user u ON p.author_id = u.id'
#        ' ORDER BY created DESC'
#    ).fetchall()
#    return render_template('blog/index.html', posts=posts)
    return render_template('blog/index.html')