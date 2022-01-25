from WaterJugsProblem import WaterJugsProblem
from WaterFillerAlgorithm import WaterFiller

problem = WaterJugsProblem()
filler = WaterFiller()
solution = filler.search(problem = problem)
for node in solution.get_path_from_root():
    print(node)