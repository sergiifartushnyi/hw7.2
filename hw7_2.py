
def correct_sentence(text):

    text = text.strip()

    text = text.capitalize()

    if not text.endswith('.'):
        text += '.'

    return f'"{text}"'


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greeting. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))

print('ok')