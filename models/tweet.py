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

    @staticmethod
    def load_all_tweets_by_user_id(cursor, user_id):
        sql_query = """
        SELECT text, creation_date FROM Tweets WHERE user_id={}
        """.format(user_id)
        cursor.execute(sql_query)
        data = cursor.fetchall()  #tworzy obiekt data ktory jest lista krotek

        tweets_list = []

        for row in data:
            tweet = Tweet()                     #tworzy liste obiektow klasy Tweet
            tweet.text = row[0]
            tweet.creation_date = row[1]
            tweets_list.append(tweet)
        return tweets_list

    @staticmethod
    def load_all_tweets(cursor):
        sql_query = """
        SELECT user_id, text, creation_date FROM Tweets
        """
        cursor.execute(sql_query)
        data = cursor.fetchall()

        all_tweets = []

        for row in data:
            tweet = Tweet()
            tweet.user_id = row[0]
            tweet.text = row[1]
            tweet.creation_date = row[2]
            all_tweets.append(tweet)
        return all_tweets

    def save_to_db(self, cursor, cnx):
        sql_query = """
        INSERT INTO Tweets(user_id, text, creation_date) VALUES('{}', '{}', '{}')
        """.format(self.user_id, self.text, self.creation_date)

        cursor.execute(sql_query)
        cnx.commit()
