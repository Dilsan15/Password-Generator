import requests


class wordAPI:

    def __init__(self, passwordLength):
        self.passwordLength = str(passwordLength)

    def generate_words(self, numberOfWords):
        wordRequest = requests.get(
            f"https://random-word-api.herokuapp.com/word?number={numberOfWords}&length={self.passwordLength}")
        return wordRequest.json()
