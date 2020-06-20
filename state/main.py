from canvas import Canvas
from brushtool import BrushTool
from selectiontool import SelectionTool

canvas = Canvas()
canvas.set_current_tool(SelectionTool())
canvas.mouse_down()
canvas.mouse_up()