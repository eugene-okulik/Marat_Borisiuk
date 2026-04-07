text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
# print(words)
for word in words:
    if word.endswith('.'):
        print(word[:-1] + 'ing' + '.', end=' ')
    elif word.endswith(','):
        print(word[:-1] + 'ing' + ',', end=' ')
    else:
        print(word + 'ing', end=' ')
