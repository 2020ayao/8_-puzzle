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


def BreadthFirstSearch(final_state):
    frontier = deque()
    explored = set()
    frontier.append(final_state)
    while len(frontier) > 0:
        n = frontier.popleft()
        for a in findNextStates(n):
            if a not in explored:
                explored.add(a)
                frontier.append(a)
    with open('solvable_8_puzzle.txt', 'a') as the_file:
        for a in explored:
            the_file.write(a)
            the_file.write("\n")
    return len(explored)


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


def swap(string1, a, b):
    list = []
    for s in string1:
        list.append(s)
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    str = ''.join(list)
    return str


final_state = '012345678'
bfs_len = BreadthFirstSearch(final_state)
print("BFS: ", bfs_len)
