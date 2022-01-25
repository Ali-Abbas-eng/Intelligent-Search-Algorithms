from GUIGraph import GUIGraph
from KingProblem import KingProblem
from UCS import UCS

if(__name__ == "__main__"):
    adjacency_matrix = [[0, 5, 3, 0, 0, 0, 10],
                        [0, 0, 0, 6, 0, 0, 0 ],
                        [0, 0, 0, 0, 0, 0, 0 ],
                        [0, 0, 0, 0, 0, 0, 0 ],
                        [0, 0, 8, 0, 0, 0, 0 ],
                        [0, 0, 0, 4, 2, 0, 0 ],
                        [0, 0, 0, 0, 3, 0, 0 ]]


    graph = GUIGraph(adjacency_matrix = adjacency_matrix, directed = True, build_from_adjacency_matrix = True)
    graph.source = 0
    graph.distination = 6
    problem = KingProblem(graph = graph)
    ucs = UCS()
    graph.plot()
    solution = ucs.search(problem = problem)
    for node in solution.get_path_from_root():
        print(node)
