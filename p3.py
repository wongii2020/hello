####### p3.py ########
def mat_sum(X, dim):
    """
    dim = 0이면 column-way sum
    dim = 1이면 row-way sum
    
    예를 들면,
    X = [[0.03675048, 0.07706246, 0.69890549],
       [0.04466621, 0.92735904, 0.79369379],
       [0.66768943, 0.69086682, 0.46034004]] 이면

    mat_sum(X, 0) = [0.74910611, 1.69528832, 1.95293931]
    mat_sum(X, 1) = [0.81271843, 1.76571904, 1.81889628]
    """
    column_num = len(X)
    row_num = len(X[0])
    ans = []

    if dim ==0:
        for i in range(column_num):
            element = 0
            for j in range(row_num):
                element += X[j][i]
            ans.append(element)
        return ans

    elif dim ==1:
        for i in range(column_num):
            element = 0
            for j in range(row_num):
                element += X[i][j]
            ans.append(element)
        return ans
    else:
        return "wrong dim"
