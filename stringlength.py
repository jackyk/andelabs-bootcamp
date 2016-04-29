def string_length(x):
    list_for_string = []
    if type(x) == str:
        r = len(x)
        list_for_string.append(r)
        return list_for_string
        list_for_list = []
    for a in x:
        v =len(a)
        list_for_list.append(v)
    return list_for_list
string_length([1,2,3],[2,5,6])
