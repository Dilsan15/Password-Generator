# Import to allow for communication between API
import requests


class Word_API:
    """Communicates with API to retrieve a list of words of length and number of which depend on the user input"""

    def __init__(self, password_length):
        # Gets variable from password_gen
        self.password_length = str(password_length)

    def generate_words(self, number_of_words):
        # Gets words from API with string formatting
        wordRequest = requests.get(
            f"https://random-word-api.herokuapp.com/word?number={number_of_words}&length={self.password_length}")
        return wordRequest.json()
