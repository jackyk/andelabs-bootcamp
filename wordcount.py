'''
    wordstr = string.split()
    word_count = {}

    for i in wordstr:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    return word_count
'''














def words(x):
    dict = {}
    for i in x.split():
        if i.isdigit():
            i = int(i)

    for i in x:
        if i in dict:
            dict [i] +=1
    else:
        dict [i] = 1
        return dict

print words("olly olly in come free")



































'''def word_count(string):
    words = string.split()  or unicode(string) #split into list
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        #if type(string) == type(unicode):
            #count[word] += 1
    for i in count:
        print i, ":", count[i]
'''
