def reverse_string(string):
    if string == '':
        return "None"
    else:
        return string[::-1]

    if string == string[::-1]:
        return True
    else:
        return string[::-1]

print reverse_string("ee")
