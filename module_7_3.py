import string


class WordsFinder:
    """
    Класс для поиска и подсчета вхождений слов в нескольких текстовых файлах.

    Attributes:
        file_names (tuple): Кортеж с именами входных текстовых файлов.
    """

    def __init__(self, *files):
        """
        Инициализирует экземпляр WordsFinder с заданными именами файлов.

        Args:
            *files (str): Имена текстовых файлов для обработки.
        """
        self.file_names = files

    def get_all_words(self):
        """
        Извлекает все слова из каждого файла и возвращает их в виде словаря.

        Returns:
            dict: Словарь, где ключи - имена файлов, значения - списки слов.
        """
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower().strip()
                    # Удаление пунктуации, кроме тире, окруженного пробелами
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        """
        Находит 1-индекс первого вхождения слова в списке слов каждого файла.

        Args:
            word (str): Слово для поиска (без учета регистра).

        Returns:
            dict: Словарь, где ключи - имена файлов, значения - 1-индекс первого вхождения слова.
        """
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            # Находим индекс слова (без учета регистра)
            position = next((i + 1 for i, w in enumerate(words) if w == word.lower()), None)
            result[name] = position
        return result

    def count(self, word):
        """
        Подсчитывает количество вхождений слова в списке слов каждого файла.

        Args:
            word (str): Слово для подсчета (без учета регистра).

        Returns:
            dict: Словарь, где ключи - имена файлов, значения - количество вхождений слова.
        """
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            # Считаем количество вхождений слова (без учета регистра)
            count = sum(1 for w in words if w == word.lower())
            result[name] = count
        return result


# Пример использования:
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('text'))
print(finder.count('text'))

