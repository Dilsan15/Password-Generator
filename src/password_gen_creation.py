import math

import password_gen_api


class passGenerator:

    def __init__(self, passwordLength, passwordSymbol):

        self.user_password_length = int(passwordLength)
        self.user_password_symbol = passwordSymbol

        self.API_words = []
        self.user_password_gened = ""
        self.my_API = password_gen_api.wordAPI(math.floor(self.user_password_length / 3))

    def contactAPI(self):
        self.API_words = self.my_API.generate_words(2)

    def passwordCreater(self):

        for word in self.API_words:

            self.user_password_gened += word
            self.user_password_gened += self.user_password_symbol

            if self.user_password_gened.count(self.user_password_symbol) == 2:

                self.API_words.clear()
                self.API_words += self.my_API.generate_words(self.user_password_length - len(self.user_password_gened))
                self.user_password_gened += self.API_words[0]
                break

        return self.user_password_gened
