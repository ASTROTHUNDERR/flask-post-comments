from cs50 import SQL
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
db = SQL('mysql://root@localhost/website')


@app.route('/', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        author = request.form.get('author')
        content = request.form.get('content')
        db.execute('INSERT INTO posts (author, content) VALUES (?, ?)', author, content)

    return render_template('post.html')



@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_comment = request.form.get('post-comment')
        id = request.form.get('post_id')
        author = db.execute('SELECT author FROM posts WHERE id = ?', id)
        db.execute('INSERT INTO post_comments (post_id, post_author,content) VALUES (?, ?, ?)', id, author[0]['author'], post_comment)


    posts = db.execute('SELECT * FROM posts')
    comments = db.execute('SELECT * FROM post_comments')
    return render_template('posts.html', posts=posts, comments=comments)

  
  
if __name__ == '__main__':
    app.run(debug=True)
