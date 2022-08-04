import requests


class Word_API:

    def __init__(self, password_length):
        self.passwordLength = str(password_length)

    def generate_words(self, number_of_words):
        wordRequest = requests.get(
            f"https://random-word-api.herokuapp.com/word?number={number_of_words}&length={self.passwordLength}")
        print("hello")
        return wordRequest.json()
