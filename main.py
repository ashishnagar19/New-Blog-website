from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c03278ae96ae6075f019").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"],
                    post["link"]
                    , post["img_url"])
    post_objects.append(post_obj)
@app.route('/')
def site():
    return render_template("index.html", all_posts=post_objects)


@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__== "__main__":
    app.run(debug=True)
