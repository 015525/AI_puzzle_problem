from astar import solver
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian

if __name__ == "__main__":
    solver.solve(123456780, manhattan())
    solver.solve(123456780, euclidian())

