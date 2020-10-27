####### p1.py ########
def mat_mul(X, Y):
    """
    두 행렬 X, Y가 주어졌을 때, 행렬 곱 X x Y를 return 하도록 한다.

    예를 들면, 
    X = [[0.93459321, 0.20840165],
        [0.53553147, 0.49286453]]
    
    Y = [[0.98689162, 0.86354536],
        [0.87284605, 0.18337937]]

    일 때, mat_mul(X, Y)는 
    [[1.10424477, 0.84528019],
    [0.95870638, 0.5528369 ]] 을 return 한다.
    """
    new_column = len(X[0])
    new_row = len(Y)
    common_num = len(X)
    ans = []

    for i in range(new_column):
        tmp = []
        for j in range(new_row):
            element = 0
            for k in range(common_num):
                element += X[i][k] * Y[k][j]
            tmp.append(element)
        ans.append(tmp)

    return ans
