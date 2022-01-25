from Sides import Sides
from BridgeCrossingProblem import BridgeCrossingProblem
from UCS import UCS

inital_state = Sides(1, 24, 5, 1)
goal_state = Sides(-1, 24, 5, 1)
p = BridgeCrossingProblem(initial_state= inital_state, goal_state = goal_state)
ucs = UCS()
solution = p.solv(ucs)
for node in solution.get_path_from_root():
    print(node)
