calls = 0


def count_calls(): #подсчитывет вызовы остальных функций
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    count_calls()
    list_low = [item.lower() for item in list_to_search]
    if string.lower() in list_low:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
