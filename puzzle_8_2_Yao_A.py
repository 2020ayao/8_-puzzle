# Adam Yao
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


def generate_path(list):
    row1 = ""
    row2 = ""
    row3 = ""
    for i in list[::-1]:
        for x in range(0, 3):
            row1 += i[x]
        row1 += "  "
        for x in range(3, 6):
            row2 += i[x]
        row2 += "  "
        for x in range(6, 9):
            row3 += i[x]
        row3 += "  "

    print(row1)
    print(row2)
    print(row3)
    print("\n")

'''print("-------------")
print("| " + state[0] + " | " + state[1] + " | " + state[2] + " | ")
print("-------------")
print("| " + state[3] + " | " + state[4] + " | " + state[5] + " | ")
print("-------------")
print("| " + state[6] + " | " + state[7] + " | " + state[8] + " | ")
print("-------------")
state = explored[state]'''


def BreadthFirstSearch(initial_state):
    frontier = deque()
    explored = {}
    frontier.append(initial_state)
    while len(frontier) > 0:
        n = frontier.popleft()
        if goalTest(n):
            counter = 0
            state_checker = n
            list = [] #this list will add the path backward, purpose: generate_path
            list.append('012345678') #solved case
            while state_checker != initial_state:
                state_checker = explored[state_checker]
                counter += 1 #shortest_path counter
                list.append(state_checker)
            #list.append(initial_state)
            generate_path(list)
            return counter
        else:
            for a in generate_children(n):
                if a not in explored.keys(): #if not in explored, map a to n, a is key, n is value
                    explored[a] = n
                    frontier.append(a)
    return "No solution", len(explored)


def DepthFirstSearch(initial_state):
    frontier = deque()
    explored = {}
    frontier.append(initial_state)
    while len(frontier) > 0:
        n = frontier.pop()  # like a stack
        if goalTest(n):
            counter = 0
            state_checker = n
            list = []
            list.append('012345678')
            while state_checker != initial_state:
                state_checker = explored[state_checker]
                list.append(state_checker)
                counter += 1
            #list.append(initial_state)
            generate_path(list)
            return counter

        else:
            for a in generate_children(n):
                if a not in explored:
                    explored[a] = n
                    frontier.append(a)
    return "No solution", len(explored)


def generate_children(state):
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


initial_state = input("Initial state: ")
# display(initial_state)

start = time.time()
bfs_len = BreadthFirstSearch(initial_state)
dfs_len = DepthFirstSearch(initial_state)
display(initial_state)
print("Shortest Length BFS: ", bfs_len)
print("Shortest Length DFS: ", dfs_len)
print(time.time() - start)
