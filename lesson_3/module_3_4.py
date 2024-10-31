def single_root_words(root_word: str, *other_words) -> list:
    same_words = list()
    for word in other_words:
        if str(word).lower().__contains__(root_word.lower()):
            same_words.append(word)
    return same_words


print(single_root_words('home', 'homebrew', 'hamster', 'homework', 'home_dir', '', 12, True, 'house', None))
