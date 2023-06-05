# 17.12

def decor(f):

    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs);
        count = 0;
        dic = {};
        for i in range(len(res)):
            for j in range(len(res[i])):
                if (res[i][j] != 0):
                    count = count + 1;
                    dic[(i, j)] = res[i][j];

        if ( count < (len(res) * len(res[0]) * 0.1) ):
            return dic;
        else:
            return res;

    return wrapper;


def enter_matrix():
    n, m = list(map(int, input("Enter matrix size (n x m) separated by comma: ").replace(" ", "").split(",")));
    mx = [];
    for i in range(n):
        mx = mx + [[]];
        for j in range(m):
            mx[-1] = mx[-1] + [float(input(f"Enter ({i}, {j}) element of matrix: "))]
    return mx;

@decor
def matrix_add(mx1, mx2):

    res = [];

    for i in range(len(mx1)):
        res = res + [[]];
        for j in range(len(mx1[i])):
            res[i] = res[i] + [mx1[i][j] + mx2[i][j]];

    return res;

test1mx1 = [[1, 2, 3, 4], [5.5, 6, 7, 8], [10, -5, 3, 0], [0, 1, 1, 0]];
test1mx2 = [[-1, 20, 7, 15], [-5, -6, 14, 2], [1, 0, 0, 0], [0, 0, 0, 0]];

test2mx1 = [[0, 0, 0, 0], [0, 200, 0, 0], [0, -8, 0, 0], [0, 0, 0, 0]];
test2mx2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 8, 0, 0], [0, 0, 0, 0]];

print(f"result: {matrix_add(test1mx1, test1mx2)}");
print(f"result: {matrix_add(test2mx1, test2mx2)}");
