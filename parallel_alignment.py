import threading
# from array import array

# seq1 = "ATAGACGACATGGGGACAGCAT"
# seq2 = "TTTAGCATGCGCATATCAGCAA"

seq1 = 'AGC'
seq2 = 'ACA'

match = 2
other = -1
maxScore = 0
maxPosition = (0, 0)
rowcounter = 0
colcounter = 0
rows = len(seq1) + 1
cols = len(seq2) + 1
max_d_count = 0
score_index_list = []
'''
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


L = [[0,  1,  2],
     [3,  4,  5],
     [6,  7,  8],
    row_count = col_count = 1
    #score_index_list.append([row_count, col_count])
    print(score_index_list)
    # for


score_matrix = createScoreMatrix(length_one + 1, length_two + 1)
rowcounter = length_one
colcounter = length_two

antidiagonals_indices(score_matrix)

     [9, 10, 11]]

#>>> antidiagonals(L)
#[[0], [3, 1], [6, 4, 2], [9, 7, 5], [10, 8], [11]]
'''


def antidiagonals_list_generator(L):

    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def antidiagonals_indices(scoring_matrix):
    # Check diagonal
    global score_index_list
    antidiagonals = antidiagonals_list_generator(scoring_matrix)
    max_diag = 0
    for x in range(len(antidiagonals)):
        if len(antidiagonals[x]) > max_diag:
            max_diag = len(antidiagonals[x])
    print(max_diag)


temp_list = []


def worker(num):
    # print('\nWorker: %s' % num)
    return


def createScoreMatrix(rows, cols):
    score_matrix = [[0 for col in range(cols)]for row in range(rows)]
    return score_matrix


def antidiagonals_list_generator(L):

    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def antidiagonals_indices(scoring_matrix):
    # Check diagonal
    global score_index_list
    antidiagonals = antidiagonals_list_generator(scoring_matrix)
    max_diag = 0
    for x in range(len(antidiagonals)):
        if len(antidiagonals[x]) > max_diag:
            max_diag = len(antidiagonals[x])
    print(max_diag)
    row_count = col_count = 1
    # score_index_list.append([row_count, col_count])
    print(score_index_list)
    # for


score_matrix = createScoreMatrix(rows, cols)

antidiagonals_indices(score_matrix)


'''
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


L = [[0,  1,  2],
     [3,  4,  5],
     [6,  7,  8],
     [9, 10, 11]]

#>>> antidiagonals(L)
#[[0], [3, 1], [6, 4, 2], [9, 7, 5], [10, 8], [11]]
'''


'''
def createScoreMatrix(rows, cols):
    score_matrix = [[0 for col in range(cols)]for row in range(rows)]
    return score_matrix

    for i in range(1, rows):
        for j in range(1, cols):
            similarity = match if seq1[i - 1] == seq2[j - 1] else other
            diag_score = score_matrix[i - 1][j - 1] + similarity
            up_score = score_matrix[i - 1][j] + other
            left_score = score_matrix[i][j - 1] + other
            curMax = max(0, diag_score, up_score, left_score)
            if curMax > maxScore:
                maxScore = curMax
                maxPosition = (i, j)
            score_matrix[i][j] = curMax


rows = 4
cols = 5
score_matrix = createScoreMatrix(rows, cols)
# print score_matrix
adiagonals = antidiagonals(score_matrix)
print(adiagonals)
print(len(adiagonals))
threads = []
for x in range(len(adiagonals)):
    print(len(adiagonals[x]))
    for y in range(len(adiagonals[x])):
        t = threading.Thread(target=worker, args=(y,))
        threads.append(t)
        t.start()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
'''
count = 0
for i in range(cols):
    p = 0
    q = i

    while(p < rows and q >= 0):
        print(p, q)
        temp_list.append([p, q])
        # score_index_list.append(temp_list)
        #score_index_list.extend([p, q])
        count = count + 1
        p = p + 1
        q = q - 1
    # score_index_list.append(temp_list)
    # temp_list.clear()
    # score_index_list.append(temp_list)
print(temp_list)
print(count)

for i in range(rows):
    p = i + 1
    q = cols - 1
    # score_index_list.append(temp_list)
    while(p < rows and q >= 1):
        print(p, q)
        temp_list.append([p, q])
        #score_index_list.extend([p, q])
        p = p + 1
        q = q - 1

print(temp_list)
antidiagonals = antidiagonals_list_generator(score_matrix)
print(antidiagonals)
num_diag = len(antidiagonals)
for i in range(num_diag):
    #print(i + 1)
    q = len(antidiagonals[i])
    x = 0
    while(x < q):
        x = x + 1
        print(x)
