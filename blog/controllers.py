from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
@blog.route('/<lang_code>/')
def index():
    return render_template('blog-home.html')


@blog.route('/post_01')
@blog.route('/<lang_code>/post_01')
def post_01():
    return render_template('blog-post_01.html')
