import time
from queue import PriorityQueue

from Maps.maps import Map


def get_euclidean_heuristics(x: int, y: int, current_goal: tuple, m: Map) -> PriorityQueue:
    heuristics = PriorityQueue()
    for s in m.get_successors(x, y):
        distance = ((x - s[0]) ** 2 + (y - s[1]) ** 2) ** 0.5
        heuristics.append((distance, s))


def a_star(m: Map, heuristics) -> list:
    start_time = time.time()

    visited = []
    visited_goals = []
    current_goal = None
    queue = PriorityQueue()
    cost = 1
    ans = []
    queue.put((0, m.me))
    while queue.queue:

        current = queue.get()

        # finding nearest goal
        if current_goal is None:
            min_dis = -1
            for g in m.goals:
                h = heuristics(m.me[0], m.me[1], g, m)
                if min_dis > h.get()[0] or min_dis == -1:
                    min_dis = h.get()[0]
                    current_goal = h.get()[1]
            h = heuristics(m.me[0], m.me[1], current_goal, m)
            queue.put((cost + h.get()[0], current))

        h = heuristics(m.me[0], m.me[1], current_goal, m)
        children = m.get_successors(current[1][0], current[1][1])

        # Check it is visited goal or not
        if current in m.goals and current not in visited_goals:
            visited_goals.append(current)
            ans += visited
            visited.clear()
            queue = PriorityQueue()
            queue.put((0, current))
            current_goal = None

        if len(visited_goals) == len(m.goals):
            break  # you can expand goal nodes too

        if current[1] not in visited:
            for i in children:
                if i not in visited:
                    queue.put((cost + h.get()[0], i))

            visited.append(current[1])

    print('A* Search')
    print('Duration:', time.time() - start_time)
    return ans
