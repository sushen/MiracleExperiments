import random

class Reply():
    """ This class will take care of reply we make """
    def __init__(self, reply_text):
        self.text = reply_text

    def randomRelpy(self):
        print("Random Choice called")
        #  Not Working
        # random.choice(self.text)

