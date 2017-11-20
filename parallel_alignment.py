import threading
#from array import array

'''
def worker(num):
    print 'Worker: %s' % num
    return


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


rows = 4
cols = 5
score_matrix = createScoreMatrix(rows, cols)
# print score_matrix
adiagonals = antidiagonals(score_matrix)
# print len(adiagonals)
for x in range(len(adiagonals)):
    print len(adiagonals[x])
