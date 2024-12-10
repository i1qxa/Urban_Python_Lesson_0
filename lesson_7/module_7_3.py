class WordsFinder:
    __LIST_SYMBOLS_FOR_REMOVE = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']

    def __init__(self, *file_names: str):
        self.list_file_names = file_names

    def __remover(self, input_str_list: list[str]) -> list[str]:
        input_str = ""
        for item in input_str_list:
            input_str += item.lower()
        for symbol in self.__LIST_SYMBOLS_FOR_REMOVE:
            input_str.replace(symbol, "")
        return input_str.split(" ")

    def get_all_words(self):
        all_words = {}
        for file_name in self.list_file_names:
            with open(file_name, encoding="utf-8") as file:
                all_words[file_name] = (self.__remover(file.read().replace("\n", "\n ").split("\n")))
        return all_words

    def find(self, word: str):
        res = {}
        list_words = self.get_all_words()
        for item in list_words:
            try:
                res[item] = list_words[item].index(word.lower()) + 1
            except ValueError:
                pass
        return res

    def count(self, word: str):
        res = {}
        list_words = self.get_all_words()
        for item in list_words:
            try:
                res[item] = list_words[item].count(word.lower())
            except ValueError:
                pass
        return res


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
