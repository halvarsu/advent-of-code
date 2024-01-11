import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
def get_data(filename):
    with open(filename) as infile:
        data = [[int(val) for val in line.strip()]
                for line in infile.readlines()]
    return data

def print_risks(risks):
    for line in risks:
        for val in line:
            print(val, end='')
        print()

def reconstruct_path(came_from, current):
    total_path = [current]

    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

def solve(risks):
    n = len(risks)
    m = len(risks[0])

    start = (0, 0)
    end = (n - 1, m - 1)

    print(end)
    print(risks[start[0]][start[1]])

    paths = []
    h = make_h(end)
    print(h(start))
    print_risks(risks)
    

    # A* algorithm, shamelessly taken from wikipedia
    open_set = set((start,))
    came_from = {}
    g_score = {start : 0}
    f_score = {start : h(start)}#, (4,4): h((4,4))}

    total_path = None
    i = 0
    while open_set:
        current = min(open_set, key=f_score.get)
        open_set.remove(current)
        if current == end:
            total_path = reconstruct_path(came_from, current)
            break

        for neighbor in get_neighbors(current, n, m):
            tentative_g_score = g_score[current] + d(neighbor, risks)
            if compare_g_score(tentative_g_score, neighbor, g_score):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)
        if i% 100 == 0:
            print(h(neighbor))
        i+=1

    if total_path is None:
        raise ValueError("no path found")

    visualize_scores(g_score, n, m)
    print()
    path_score = defaultdict(int)
    for node in total_path:
        path_score[node] = 1
    visualize_scores(path_score, n, m, v_delim="", h_delim="")


    plot_scores(path_score, n,m, title='ps')
    plot_scores(g_score, n,m, title='gs')
    plot_scores(f_score, n,m, title='fs')
    return g_score[end]

def plot_scores(scores, n, m, title='' ):
    grid = np.zeros((n,m))
    for i,j in scores:
        grid[i,j] = scores[(i, j)]
    plt.imshow(np.array(grid))
    plt.title(title)
    plt.show()

def visualize_scores(score, n, m, v_delim="|", h_delim="-"):
    score_grid = []
    for i in range(n):
        for j in range(m):
            try:
                print(f"{score[(i, j)]:2}",end=v_delim)
            except KeyError:
                print(f"{0:2}",end=v_delim)
        print()
        if h_delim:
            print(3*m*h_delim)


def compare_g_score(tentative, node, g_score):
    try:
        return tentative < g_score[node]
    except KeyError:
        return True

def get_neighbors(node, n, m):
    x,y = node
    return [(x+dx,y+dy) for dx, dy in ((1,0),(0,1),(-1,0),(0,-1))
                    if 0 <= x+dx < n and 0 <= y+dy < m]

def make_h(end):
    def h(node):
        return sum(abs(n - e) for n, e in zip(node, end))
    return h


def d(node, risks):
    return risks[node[0]][node[1]]


def search(start, end):
    node = start
    risk = 0
    while node != end:
        pass


if __name__ == "__main__":
    print(solve(get_data("input")))
