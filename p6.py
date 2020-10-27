

####### p6.py ########
def mat_positive_bool(X, H):
    """
    mat_positive와 유사하지만, 

    H_(i,j) 번 째 요소가 양수면 X_(i, j)의 값을 그대로 사용하고,
    H_(i,j) 번 째 요소가 0 이하의 숫자면, 0을 출력하는 행렬을
    return 한다.
    """
    column_num = len(X)
    row_num = len(X[0])

    for i in range(column_num):
        for j in range(row_num):
            if H[i][j] <= 0:
                X[i][j] = 0
    return X
