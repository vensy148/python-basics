# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Intek Institute.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Intek Institute or one of its subsidiaries.  You shall not disclose
# this confidential information and shall use it only in accordance
# with the terms of the license agreement or other applicable
# agreement you entered into with Intek Institute.
#
# INTEK INSTITUTE MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  INTEK
# INSTITUTE SHALL NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY
# LICENSEE AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THIS
# SOFTWARE OR ITS DERIVATIVES.

import math
import os
import string


def hello(name):
    return f'Hello {name.strip()}!'


def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def are_all_conditions_true(conditions):
    if len(conditions) == 0:
        return None

    for condition in conditions:
        if not condition:
            return False

    return True


def is_a_condition_true(conditions):
    if len(conditions) == 0:
        return None

    for condition in conditions:
        if condition:
            return True

    return False


def filter_integers_greater_than(l, n):
    return [i for i in l if i > n]


def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    return sorted([hotel_name for hotel_name, daily_rate in hotel_daily_rates if daily_rate <= maximum_daily_rate])


def calculate_euclidean_distance_between_2_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_euclidean_distance_between_points(points):
    if len(points) < 2:
        raise ValueError('The list MUST contain at least 2 points')

    return sum([
        calculate_euclidean_distance_between_2_points(points[i], points[i + 1])
        for i in range(len(points) - 1)])


def capitalize_words(s):
    """Return a copy of the string with all the words capitalized.

    This function sets the first character in each word of the string `s`
    to uppercase and the rest to lowercase.

    The function removes any duplicate whitespace characters between words.


    If `None` is passed, the function returns `None`.

    @param s: a string that possibly contains words separated by whitespace
        characters.

    @return: a string where the first character in each word of the string
        `s`has been converted to uppercase and all remaining characters of
        this word have been converted to lowercase.

    @raise TypeError: if the argument `s` is not a string.
    """
    if s is None:
        return None

    if not isinstance(s, str):
        raise TypeError('Not a string')

    return ' '.join([word.capitalize() for word in s.split()])


def uppercase_lowercase_words(s):
    """
    Uppercase and lowercase the words of a string depending on the
    position of the words in the string.

    @param s: A string

    @return: A copy of the string `s` with the words converted to
        uppercase or lowercase depending on their position in the string
        (starting with `0`).

    @raise TypeError: if the argument `s` is not a string.
    """
    if s is None:
        return None

    if not isinstance(s, str):
        raise TypeError('Not a string')

    return ' '.join([word.lower() if i % 2 else word.upper() for i, word in enumerate(s.split())])


def factorial(n):
    """
    Return the factorial of an integer.


    A recursive version of the factorial is:

    ```python
    def factorial(n):
        def _factorial_ex(n):
            return 1 if n == 0 or n == 1 else n * _factorial_ex(n - 1)

        if not isinstance(n, int):
            raise TypeError('Not an integer')

        if n < 0:
            raise ValueError('Not a positive integer')

        return _factorial_ex(n)
    ```

    A recursive terminal version of the factorial is:

    ```python
    def factorial(n):
        def _factorial_ex(n, a):
            return a if n == 0 or n == 1 else _factorial_ex(n - 1, a + n)

        if not isinstance(n, int):
            raise TypeError('Not an integer')

        if n < 0:
            raise ValueError('Not a positive integer')

        return _factorial_ex(n, 1)
    ```


    @param n: A positive integer.


    @return: The factorial of the argument `n`.


    @raise TypeError: if the argument `n` is not a string.

    @raise ValueError: if the argumnet `n` is not a positive integer.
    """
    if not isinstance(n, int):
        raise TypeError('Not an integer')

    if n < 0:
        raise ValueError('Not a positive integer')

    value = 1
    for i in range(n):
        value *= i + 1

    return value


def char_to_int(c):
    """
    Return the integer value of the specified digit character.


    @param c: a character representing a digit.

    @return: the integer value of this digit character.


    @raise TypeError: if the argument `c` is not a string.

    @raise ValueError: if the argument `c` is not a single digit.
    """
    if not isinstance(c, str):
        raise TypeError('Not a string')

    if not (c.isdigit() and len(c) == 1):
        raise ValueError('Not a single digit')

    return ord(c) - ord('0')  # Faster than `string.digits.index(c)`


def string_to_int(s):
    """
    Return the integer value of the specified string of digit characters.

    This function doesn't handle string representation of negative integer.


    @param s: a string of digit characters.


    @return: the integer value of this string of digit characters.


    @raise TypeError: if the argument `c` is not a string.

    @raise ValueError: if the argument `c` is not a single digit.
    """
    if not isinstance(s, str):
        raise TypeError('Not a string')

    if not s.isdigit():
        raise ValueError('Not a positive integer string expression')

    # This method is faster than the two following Pythonic ways:
    #
    # 1. `sum([char_to_int(c) * (10 ** (len(s) - i - 1)) for i, c in enumerate(s)])`
    #
    # 2. `sum([char_to_int(c) * (10 ** -i) for i, c in enumerate(s, 1 - len(s))])`
    value = 0

    for c in s:
        value = value * 10 + char_to_int(c)

    return value


def is_palindrome(value):
    """
    Indicate whether the specified string is palindrome, i.e, whether it
    can be read the same backward as forward.

    The function only retains ASCII characters and digits. The function is
    not case-sensitive.


    @param value: any value that can be converted to a string.

    @return: `True` if the the argument `value` is a palindrome; `False`
        otherwise.
    """
    if not isinstance(value, str):
        value = str(value)

    ascii_lowercase_and_digits = string.digits + string.ascii_lowercase
    value = ''.join(c for c in value.lower() if c in ascii_lowercase_and_digits)

    for i in range((len(value) // 2) - (len(value) % 2)):
        if value[i] != value[-i - 1]:
            return False

    return True


ROMAN_NUMERAL_VALUES = {
    'N': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_numeral_to_int(roman_numeral):
    if not isinstance(roman_numeral, str):
        raise TypeError('Not a string')

    if len(roman_numeral) == 0:
        raise ValueError('Empty string')

    for c in roman_numeral:
        if c not in ROMAN_NUMERAL_VALUES:
            raise ValueError('Not a Roman numeral')

    # Iterate over the characters (symbols) defined in the given Roman
    # numeral, adding their cumulative value together ("additive" notation),
    # subtracting the value of a symbol when lower than the value of the
    # next symbol ("subtractive" notation).
    #
    # This code of the function is a Pythonic optimization of the following
    # code that could be presented to students for education purpose::
    #
    #     roman_numeral_value = 0
    #     for i, c in enumerate(roman_numeral):
    #         symbol_value = ROMAN_NUMERAL_VALUES[c]
    #         if i < len(roman_numeral) - 1 and symbol_value < ROMAN_NUMERAL_VALUES[roman_numeral[i + 1]]:
    #             symbol_value = -symbol_value
    #         roman_numeral_value += symbol_value
    #
    #     return roman_numeral_value
    return sum([
        -ROMAN_NUMERAL_VALUES[c] if i < len(roman_numeral) - 1 and ROMAN_NUMERAL_VALUES[c] < ROMAN_NUMERAL_VALUES[roman_numeral[i + 1]]
            else ROMAN_NUMERAL_VALUES[c]
        for i, c in enumerate(roman_numeral)])


MELODY_I_LOVE_YOU = (
    'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
    'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
    'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
    'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
    'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
    'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
    'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
    'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
)

MELODY_HAPPY_BIRTHDAY_TO_YOU = (
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
)

MELODY_FUR_ELISE = (
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'B4', 'C5', 'D5', 'E5',
    'G4', 'F5', 'E5', 'D5',
    'F4', 'E5', 'D5', 'C5',
    'E4', 'D5', 'C5', 'B4',
    'E4', 'E5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
)

NOTES = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']


def play_melody(melody, note_sound_file_path):
    """
    Play a melody composed of linear succession of notes.


    @param melody: A collection (iterable) of notes, named after the
        international pitch notation, of the melody to play.

    @param note_sound_file_path:A string representing the path of the
        directory containing the note sound files. The function will use
        this parameter to find and load each note sound file.


    @return: A list of the file pathname of the notes that have been
        played one after the other.
    """
    import pygame
    pygame.init()
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)  # setup mixer to avoid sound lag

    # Load the sound files into `pygame.mixer.Sound` instances.
    note_sounds = dict([
        (f'{note}{octave}', pygame.mixer.Sound(os.path.join(note_sound_file_path, f'{note}{octave}.ogg')))
        for octave in range(2, 6) for i, note in enumerate(NOTES)])

    note_file_path_names = []

    # Play each note of the melody.
    for note in melody:
        # Determine the file pathname of the note to play.
        note = note.lower()
        note_file_path_name = os.path.join(note_sound_file_path, f'{note}.ogg')

        # Replace any accidental sharp (♯) note with the equivalent accidental
        # flat (♭) notes.
        offset_sharp = note.find('#')
        if offset_sharp > 0:
            # Retrieve the pitch and the octave of the sharp note to play.
            pitch = note[:offset_sharp]
            octave = note[offset_sharp + 1:]

            # A note with the accidental sharp is equivalent to the next note with
            # the accidental flat.
            next_note_index = NOTES.index(pitch) + 1

            # Add the same octave of the sharp note to the flat note to play.
            note = NOTES[next_note_index] + octave

            # Update the file pathname of the note that will be played.
            note_file_path_name = os.path.join(note_sound_file_path, f'{note}.ogg')

        # Append the file pathname of the note to the list to be returned.
        note_file_path_names.append(note_file_path_name)

        # Play the note on an available channel.
        channel = note_sounds[note.lower()].play(maxtime=500)

        # Wait a little bit before playing the next note, but just a bit less
        # than the time allocated to play the current note so that there is a
        # little resonance of the current note while the next note will be
        # played.
        pygame.time.delay(300)

    if len(melody) > 0:
        while channel.get_busy():
            pygame.time.delay(100)

    pygame.quit()

    return note_file_path_names

