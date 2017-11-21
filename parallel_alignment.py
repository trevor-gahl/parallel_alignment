import threading
#from array import array


def worker(num):
    print '\nWorker: %s' % num
    return


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


def antidiagonals(L):

    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


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
# print len(adiagonals)
threads = []
for x in range(len(adiagonals)):
    # print len(adiagonals[x])
    for y in range(len(adiagonals[x])):
        t = threading.Thread(target=worker, args=(y,))
        threads.append(t)
        t.start()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
