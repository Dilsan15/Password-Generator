import math
from src.password_gen_bkend import password_gen_api


class Pass_Generator:
    """Called by My_Applicatoin, communicates with API to get unique random words off of a large dataset. Dynamically
    computes how long each word should be and how many words can fit in a password"""
    def __init__(self, password_length, password_symbol):

        # Variables which will be used to generate password
        self.user_password_length = int(password_length)
        self.user_password_symbol = password_symbol

        self.API_words = []
        self.user_password_gened = ""
        self.my_API = password_gen_api.Word_API(math.floor(self.user_password_length / 3))

    def contact_api(self):
        # Creates class and communicates with API
        self.API_words = self.my_API.generate_words(2)

    def password_creator(self):
        # Iterates through words retrieved by API, and creates password based off of these words

        for word in self.API_words:

            self.user_password_gened += word
            self.user_password_gened += self.user_password_symbol

            if self.user_password_gened.count(self.user_password_symbol) == 2:
                self.API_words.clear()
                self.API_words += self.my_API.generate_words(self.user_password_length - len(self.user_password_gened))
                self.user_password_gened += self.API_words[0]
                break

        return self.user_password_gened
