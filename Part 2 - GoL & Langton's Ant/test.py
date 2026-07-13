from logic_gates import GliderLogicGates
from pygame_viewer import run_pygame_life
import conway
CELL_SCALE = 10
not_gate = GliderLogicGates()
life = not_gate.setup_not_gate(80, True)
run_pygame_life(life, cell_scale= CELL_SCALE, fps = 20, title="GOL")
print(not_gate.run_not_gate(True))
