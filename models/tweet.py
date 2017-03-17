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

    def load_tweet_by_id(self):

