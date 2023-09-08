import unittest


def calculate_word_value(word):
    total_value = 0
    word_multiplier = 1

    for cell in word:
        letter_value = cell.letter.value
        cell_multiplier = cell.multiplier if cell.multiplier_type == 'letter' else 1
        total_value += letter_value * cell_multiplier

        if cell.multiplier_type == 'word':
            word_multiplier *= cell.multiplier

    return total_value * word_multiplier


