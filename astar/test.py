from astar.solver import solver
from astar.heuristic.heuristic import manhattan
from astar.heuristic.heuristic import euclidian

if __name__ == "__main__":
    a = solver()
    a.solve(123456780, manhattan())
    a.solve(123456780, euclidian())

