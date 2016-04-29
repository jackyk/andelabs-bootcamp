def find_max_min (A):

    AnswerlistA = []
    AnswerlistB = []

    x = max (A)
    y = min (A)

    if x == y:
      AnswerlistA.append(len(A))

      return AnswerlistA

    #else:
      #AnswerlistB.append(y)
      #AnswerlistB.append(x)

    #return AnswerlistB
print find_max_min([1,2,4,4])












'''
def max_min(A):
    max_, min_ = A[0], A[0]

    for i in A:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i

    return max_ - min_



a=[233,56,7,8,9,3]
print max_min(a)

'''
