class Tweet(object):

    id = None
    user_id = None
    text = None
    creation_date = None

    def __init__(self):
        self.id = -1
        self.user_id = 0
        self.text = ""
        self.creation_date = None

    @staticmethod
    def load_tweet_by_id(cursor, id):
        sql_query = """
        SELECT user_id, text, creation_date FROM Tweets WHERE id={}
        """.format(id)
        cursor.execute(sql_query)
        row = cursor.fetchone()         #tworzy obiekt ktory jest krotka wartosci z kolumn w rzedzie o danym id

        if row is not None:
            loaded_tweet = Tweet()
            loaded_tweet.id = id
            loaded_tweet.user_id = row[0]
            loaded_tweet.text = row[1]
            loaded_tweet.creation_date = row[2]
            return loaded_tweet
        else:
            return None

