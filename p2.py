####### p2.py ########
def mat_add(X, Y, dim):
    """
    두 행렬이 주어질 때, 
    dim=0인 경우 X, Y 둘 다 이차원 행렬이라 가정하고 두 행렬의 합을
    return

    dim=1인 경우, Y는 column vector이며, X의 모든 column vector와
    Y의 column vector의 합을 return

    dim=2인 경우, Y는 scalar 값이므로, X의 모든 원소에 Y를 더한 행렬을
    return

    단, X는 항상 2차원 행렬이라 가정한다.
    """
    ans = []

    if dim ==0:
        for i in range(2):
            tmp=[]
            for j in range(2):
                element = X[i][j] + Y[i][j]
                tmp.append(element)
            ans.append(tmp)
        return ans

    elif dim ==1:
        for i in range(2):
            tmp=[]
            for j in range(2):
                element = X[i][j] + Y[i]
                tmp.append(element)
            ans.append(tmp)
        return ans

    elif dim ==2:
        for i in range(2):
            tmp=[]
            for j in range(2):
                element = X[i][j] + Y
                tmp.append(element)
            ans.append(tmp)
        return ans

    else:
        return "wrong dim"
