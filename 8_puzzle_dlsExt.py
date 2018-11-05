import time
'''helper methods'''

from collections import deque


def display(initial_state):
    print("-------------")
    print("| " + initial_state[0] + " | " + initial_state[1] + " | " + initial_state[2] + " | ")
    print("-------------")
    print("| " + initial_state[3] + " | " + initial_state[4] + " | " + initial_state[5] + " | ")
    print("-------------")
    print("| " + initial_state[6] + " | " + initial_state[7] + " | " + initial_state[8] + " | ")
    print("-------------")

def generate_path(n, explored):
   l = []
   while explored[n] != "s":
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

def DLS(current_state, lim, explored):
    if current_state == "012345678":
        generate_path(current_state, explored)
        return "Solved!"
    elif lim == 0:
        return "cutoff"
    else:
        bool = False
        for e in findNextStates(current_state):
            if e not in curPath(current_state, explored):
                explored[e] = current_state
                result = DLS(e, lim - 1, explored)
                if result == "cutoff":
                    bool = True
                elif result != "Fail":
                    return result
        if bool:
            return "cutoff"
        else:
            return "Fail"


def curPath(n, explored):
    path = set(n)
    while(explored[n] != "s"):
        path.add(explored[n])
        n = explored[n]
    return path



def findNextStates(state):
    list = []
    list_states = []
    for s in state:
        list.append(s)
    pos0 = list.index('0')
    if pos0 == 0:
        list_states.extend([swap(state, 0, 1), swap(state, 0, 3)])  # list[1], list[3]
    elif pos0 == 1:
        list_states.extend([swap(state, 1, 0), swap(state, 1, 2), swap(state, 1, 4)])  # 0 2 4
    elif pos0 == 2:
        list_states.extend([swap(state, 2, 1), swap(state, 2, 5)])  # 1 5
    elif pos0 == 3:
        list_states.extend([swap(state, 3, 0), swap(state, 3, 4), swap(state, 3, 6)])  # 0 4 6
    elif pos0 == 4:
        list_states.extend([swap(state, 4, 1), swap(state, 4, 3), swap(state, 4, 5), swap(state, 4, 7)])  # 1 3 5 7
    elif pos0 == 5:
        list_states.extend([swap(state, 5, 2), swap(state, 5, 4), swap(state, 5, 8)])  # 2 4 8
    elif pos0 == 6:
        list_states.extend([swap(state, 6, 3), swap(state, 6, 7)])  # 3 7
    elif pos0 == 7:
        list_states.extend([swap(state, 7, 4), swap(state, 7, 6), swap(state, 7, 8)])  # 4 6 8
    elif pos0 == 8:
        list_states.extend([swap(state, 8, 5), swap(state, 8, 7)])  # 5 7
    return list_states


def goalTest(state):
    if state == "012345678":
        return True
    return False


def swap(string1, a, b):
    list = []
    for s in string1:
        list.append(s)
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    str = ''.join(list)
    return str


def DepthFirstSearch(initial_state):
    frontier = deque()
    explored = set()
    frontier.append(initial_state)
    while len(frontier) > 0:
        n = frontier.pop() #like a stack
        if goalTest(n):
            return len(explored)
        else:
            for a in findNextStates(n):
                if a not in explored:
                    explored.add(a)
                    frontier.append(a)
    return "No solution", len(explored)

def iterative_deepening_search(start):
    countDepth = 0
    while True:
        solved = DLS(start, countDepth, {start:"s"})
        if solved == "Solved!":
            return
        countDepth+=1


initial = input("initial state: ")
display(initial)
if(DLS(initial, int(input("To what depth would you like to limit the search? ")), {initial:"s"}) == "cutoff"):
       print("No solution was found at this depth. ")




