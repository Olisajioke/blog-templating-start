from flask import Flask, render_template
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    post = [Post(i) for i in range(3)]
    return render_template("index.html", posts=post)


@app.route("/blog/<int:post_id>")
def blog_post(post_id: int):
    post = Post(post_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
