import requests



class CurrencyExchange:

    def __init__(self):
        self.cache = dict()
        self.currency_for_exchange = None

    def check_cache(self, func, currency):

        print("Checking the cache...")
        if currency in self.cache:
            print("It is in the cache!")
            return self.cache[currency]

        print("Sorry, but it is not in the cache!")
        result = func(currency)
        self.cache[currency] = result

        return result

    def get_exchange_rate(self, currency):
        print(f"Wait... ")
        response = requests.get(f"http://www.floatrates.com/daily/{self.currency_for_exchange}.json")
        if response.ok:
            result = response.json()

            try:

                result = result.get(f"{currency}").get("rate")
            except AttributeError:
                return

            return round(result, 2)

        else:
            return

    def menu(self):
        self.currency_for_exchange = input("Currency for exchange > ").lower()
        self.play_currency_exchange()

    def play_currency_exchange(self):
        amount_of_many = self.correct_float_input("Amount of many > ")
        currency = input("What to change > ").lower()
        exchange_rate = self.check_cache(self.get_exchange_rate, currency)
        if not exchange_rate:
            print("Incorrect parameters")
            self.play_currency_exchange()
            return
        print(f"You received {round(amount_of_many * exchange_rate, 2)} {currency.upper()}.")
        self.play_currency_exchange()

    @staticmethod
    def correct_float_input(string):
        user_input = input(string)
        while True:
            try:
                float(user_input)
            except ValueError:
                if "," in user_input:
                    user_input = user_input.replace(",", ".")
                    continue
                print("Incorrect format")
                user_input = input(string)
                continue
            else:
                break
        return float(user_input)



currency_ex = CurrencyExchange()
currency_ex.menu()
