from flask import Flask, request
from models.tweet import Tweet
from models.user import  User
from mysql.connector import connect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    html = """
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <form method="POST">
                Lista tweetow:  <br>
            </form>
        </body>
    </html>
    """
    if request.method == "GET":
        cnx = connect(user="root", password="coderslab", host="localhost", database="twitter")
        print("Connected")

        cursor = cnx.cursor()

        all_tweets = Tweet.load_all_tweets(cursor)

        for tweet in all_tweets:
            html += """
            {} {} {} <br>""".format(tweet.user_id, tweet.text, tweet.creation_date)

        return html
    else:
        pass



app.run()