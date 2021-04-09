# https://www.codewars.com/kata/5263c6999e0f40dee200059d 

alternatives = {'1': ['1', '2', '4'],
                '2': ['2', '1', '3', '5'],
                '3': ['3', '2', '6'],
                '4': ['4', '1', '5', '7'],
                '5': ['5', '2', '4', '6', '8'],
                '6': ['6', '3', '5', '9'],
                '7': ['7', '4', '8'],
                '8': ['8', '5', '7', '9', '0'],
                '9': ['9', '6', '8'],
                '0': ['0', '8']}
    
def add_nextcharcter_and_alternatives(answers, next_character):
    new_answers = []
    for current_answer in answers:
        for alterntive_next_char in alternatives[next_character]:
            new_answers.append(current_answer + alterntive_next_char)
    return new_answers

def get_pins(observed):
    answers = []
    for alternative_first_character in alternatives[observed[0]]:
        answers.append(alternative_first_character)
    for i in range(1, len(observed)):
        answers = add_nextcharcter_and_alternatives(answers, observed[i])
    return answers
