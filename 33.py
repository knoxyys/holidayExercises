import random

outcomes = ['Yes.', 'No.', 'Maybe.', 'Ask again later.']

question = input("What's your question? ")
print(outcomes[random.randint(0, 3)])