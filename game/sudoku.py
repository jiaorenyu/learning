
import copy


array=[
    [0,8,0,6,0,0,4,0,9],
    [2,0,9,0,0,0,0,6,0],
    [0,3,0,4,0,9,0,0,0],
    [0,0,0,1,0,0,0,4,0],
    [0,1,0,0,9,0,7,0,5],
    [8,0,0,0,3,7,0,9,1],
    [0,0,3,0,0,0,8,0,6],
    [0,6,0,0,5,0,0,0,0],
    [0,0,0,7,4,0,3,0,2]
    ]

values=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    
guess_values=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
    


def unfinish(data):
    for ldata in data:
        for v in ldata:
            if v == 0:
                return True
    return False

def conflict(data, i, j, pv):
    for v in data[i]:
        if pv == v:
            return True
    for x in range(len(data)):
        if data[x][j] == pv:
            return True
    
    for x in range(3):
        for y in range(3):
            xxi = i/3
            yyj = j/3
            xx = xxi*3+x
            yy = yyj*3+y
            if data[xx][yy] == pv:
                return True
    return False

def get_line_values(data, index, line_type):
    current_values = []
    
    if line_type == "row":
        for v in data[index]:
            if v != 0:
                current_values.append(v)
            
    elif line_type == "col":
        for i in range(len(data)):
            if data[i][index] != 0:
                current_values.append(data[i][index])

    possible_values = []  
    for i in range(1,10):
        if i not in current_values:
            possible_values.append(i)

    return set(possible_values)
    

def get_matrix_values(data, row, col, msize):
    c_values = []
    ##print(data)
    for i in range(msize):
        for j in range(msize):
            ##print(row*msize+i, col*msize+j)
            v = data[row*msize+i][col*msize+j]
            if v != 0:
                c_values.append(v)

    possible_values = []  
    for i in range(1,10):
        if i not in c_values:
            possible_values.append(i)

    return set(possible_values)

def get_values(data,i,j):
    pvalues = []
    line_value_row = get_line_values(data,i,"row")
    line_value_col = get_line_values(data,j,"col")
    matrix_value = get_matrix_values(data, i/3, j/3, 3)
    pvalues = list(line_value_row & line_value_col & matrix_value)
    
    return pvalues

def happen_counts(line_values, v):
    counter = 0
    for vs in line_values:
        if v  in vs:
            counter += 1

    return counter

def update_values(values, pv, i, j):
    for x in range(len(values[i])):
        if values[i][x] != 0 and pv in values[i][x]:
            values[i][x].remove(pv)
    for x in range(len(values)):
        if values[x][j] != 0 and pv in values[x][j]:
            values[x][j].remove(pv)

    xi = i/3
    yj = j/3
    for x in range(3):
        for y in range(3):
            xx = xi*3+x
            yy = yj*3+y
            if values[xx][yy] != 0 and pv in values[xx][yy]:
                values[xx][yy].remove(pv)

def update_data(data, i, line_type):
    if line_type == "row":
        row_values = []
        for vs in values[i]:
            if vs != 0:
                row_values.append(vs)
        for j in range(len(data[i])):
            v = data[i][j]
            if v != 0:
                continue
            pvalues = values[i][j]
            if len(pvalues) == 0:
                return False
            for pv in pvalues:
                if happen_counts(row_values, pv) == 1:
                    if conflict(data, i, j, pv):
                        return False
                    data[i][j] = pv
                    values[i][j] = 0
                    update_values(values, pv, i, j)
                    break
                    
    elif line_type == "col":
        col_values = []
        for j in range(len(values)):
            vs = values[j][i]
            if vs != 0:
                col_values.append(vs)
        for j in range(len(data)):
            v = data[j][i]
            if v != 0:
                continue
            pvalues = values[j][i]
            if len(pvalues) == 0:
                return False
            for pv in pvalues:
                if happen_counts(col_values, pv) == 1:
                    if conflict(data, j,i, pv):
                        return False
                    data[j][i] = pv
                    values[j][i] = 0
                    update_values(values, pv, j, i)
                    break
    return True

def print_col(data, j):
    for i in range(len(data)):
        print(data[i][j])

def fill_lines(data):
    for i in range(len(data)):
        #print("old possible", values[i])
        #print("old", data[i])
        if not update_data(data,i,"row"):
            return False
        #print("new possible", values[i])
        #print("new", data[i])
    for j in range(len(data[0])):
        #print("old possible")
        #print_col(values,j)
        #print("old data")
        #print_col(data,j)
        if not update_data(data, j, "col"):
            return False
        #print("new possible")
        #print_col(values,j)
        #print("new data")
        #print_col(data,j)
    return True 

def print_data(data, datatype="new data"):
    print(datatype)
    for l in data:
        print(l)
    print("------------")

def print_mat(i, j):
    print(values[i*3][j*3:j*3+3])
    print(values[i*3+1][j*3:j*3+3])
    print(values[i*3+2][j*3:j*3+3])

def update_mat(data, i, j):
    mat_values = []
    for x in range(3):
        for y in range(3):
            xx = i*3+x
            yy = j*3+y
            vs = values[xx][yy]
            if vs != 0:
                mat_values.append(vs)
    for x in range(3):
        for y in range(3):
            xx = i*3+x
            yy = j*3+y
            if data[xx][yy] != 0:
                continue
            pvalues = values[xx][yy]
            if len(pvalues)==0:
                return False
            for pv in pvalues:
                if happen_counts(mat_values, pv) == 1:
                    if conflict(data, xx, yy, pv):
                        return False
                    data[xx][yy] = pv
                    values[xx][yy] = 0
                    update_values(values, pv, xx, yy)
                    break
    return True

def fill_mat(data):
    for i in range(3):
        for j in range(3):
            #print_data(data)
            #print_mat(1,1)
            if not update_mat(data, i, j):
                return False
    return True 

def cal_pvalues(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                values[i][j] = get_values(data,i,j)

def scan(data):
    data_new = copy.deepcopy(data)
    
    cal_pvalues(data)
    
    #print_data(data)
    #print_data(values, "possible")
    if not fill_lines(data_new):
        return [False, None] 
    #print_data(data_new)
    if not fill_mat(data_new):
        return [False, None] 
    #print_data(data_new)
    return [True, data_new]


   

status_save = []

def get_min(values):
    [i,j] = [0,0]
    min_len = 10
    for x in range(len(values)):
        for y in range(len(values[0])):
            if values[x][y] != 0:
                if len(values[x][y]) < min_len:
                    [i, j] = [x, y]
                    min_len = len(values[x][y])
    
    return [i, j]

def guess(data, values, status_save):
    [i,j] = get_min(values)   
        
    if len(values[i][j]) == 0:
        return False
    pv = values[i][j].pop()
    if len(values[i][j]) == 0:
        values[i][j] = 0
    status_save.append([i, j, copy.deepcopy(data), copy.deepcopy(values)])
    data[i][j] = pv
    return True

def recover(data, values, status_save):
    if len(status_save) == 0:
        return False

    [i,j, data, values] = status_save.pop()
    
    return True

def sudoku(array):
    counter = 0
    data = copy.deepcopy(array)
    ori = copy.deepcopy(array)
    flag = True 
    while (unfinish(data)):
        flag=True
        while(unfinish(data)):
            counter += 1
            print("counter",counter)
            print_data(data)   
            [stat, data_new] = scan(data)
            if not stat:
                flag = False 
                break
            if data_new == data: break;
            data = copy.deepcopy(data_new)
        if (unfinish(data)):
            if flag:
                if not guess(data, values, status_save):
                    if not recover(data, values, status_save):
                        return False
            else:
                if not recover(data, values, status_save):
                    return False
                if not guess(data, values, status_save):
                    if not recover(data, values, status_save):
                        return False
                    
        
    print_data(ori, "ori")
    print_data(data, "new")   

    return True

if __name__=="__main__":
    result=sudoku(array)
    if result:
        print("OK")
    else:
        print("Failed")
