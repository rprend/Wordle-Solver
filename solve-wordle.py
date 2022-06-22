def get_wordle_data():
    allowed_guesses = []
    wordle_answers = []

    with open("wordle-allowed-guesses.txt") as f_guesses:
        allowed_guesses = f_guesses.read().split('\n')
    with open("wordle-answers-alphabetical.txt") as f_answers:
        wordle_answers = f_answers.read().split('\n')

    return allowed_guesses, wordle_answers

# Given a list of 5 letter strings made of the characters A-Z, order A-Z in the
# order of which is the most common to the least common. This only needs to be done once,
# after which I'll save it in a file.
# long_string: A LONG STRING, NOT A LIST OF STRINGS
# returns: A dictionary of letter counts.
def generate_letter_hierarchy(long_string):
    letters = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    str_length = len(long_string)

    for letter in letters:
        letter_count[letter] = long_string.count(letter) / str_length

    return letter_count

# Given a single 5 letter word and a set of criteria, this function tests to see that
# the word passes all constraints. If it does, it returns true, otherwise, false.
# TODO: Change from a pass fail strict system to some kind of scoring. Eg failing a constraint
# like "dont have this letter" is better than not having a guess -- wait there will always be a
# guess, so that would be a stupid idea. Never mind, carry on.
def passes_constraints(word, constraints):
    # Each constraint pair is a two character string for each of the letters. There are five constraint pairs per
    # guess, and the constraints list can have any amount of constraint pairs.
    #
    # The first character of each pair contains the letter, the second character
    # contains one of 'N', 'Y', 'G', for greeN, Yellow, and Gray, respectively.

    # To test a constraint. There is a naive solution where we do a nested loop: go over each constraint, then
    # go over each letter, and if one fails we return false. Let's program that, we can be fancy later.
    # print(word)
    # print(constraints)

    # Note that we use capital letters for Constraints, and lower case for the letters
    # themselves.
    for straint in constraints:
        # Check the non place-dependent constraints, Gray and (part of) Yellow.
        # For these, we iterate over the constraint, and then check to see if that letter exists
        # in the word. If not, fail.
        #
        # Then, check the place-dependent constraints, Green and (part of) Yellow. For these,
        # we iterate over each place on the board, and check to see if there's
        for space in range(5):
            straint_letter = straint[space * 2]
            straint_type = straint[space * 2 + 1]

            letter = word[space]

            # Gray, must not be anywhere in the word.
            if straint_type == 'G' and straint_letter in word:
                return False
            # Yellow, must be in the word
            if straint_type == 'Y' and straint_letter not in word:
                return FALSE

            # greeN, must contain in this spot.
            if straint_type == 'N' and letter != straint_letter:
                return False
            # Yellow, must NOT be in this spot.
            if straint_type == 'Y' and letter == straint_letter:
                return False

    return True

def main():
    allowed_guesses, wordle_answers = get_wordle_data()

    letter_hierarchy = generate_letter_hierarchy("".join(wordle_answers))

    print(passes_constraints("magic", ["mNoGoGoGrG"]))
main()
