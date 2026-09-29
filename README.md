# Lyon metro route planner

A Python coursework project that represents four Lyon metro lines as a weighted graph and uses an A* search routine to propose a route between stations. The interface lets the user select stations and a departure time, with preferences for travel duration or fewer transfers. This repository has multiple contributors; the graph, search routine and interface can be inspected in the source files below.

## Implementation

- `a_estrella.py`: priority-queue search and path reconstruction.
- `ini.py`: station graph, edge travel times, waiting-time and transfer heuristic, and Matplotlib route output.
- `menu.py`: Tkinter interface and map-based station selection.
- `Lyon/`: map image and generated route image.

The graph and service frequencies are hard-coded for this coursework model. The heuristic includes transfer penalties and timetable estimates; this is an illustrative route planner, not a verified optimal journey planner or a live transit service.

## Run

Use Python 3.10 or newer (the code uses `match`) with a desktop environment and Tkinter. Install NetworkX, Matplotlib and Pillow, then run from the repository root:

```bash
python -m pip install networkx matplotlib pillow
python menu.py
```

On Windows, `A_Star_Maps.bat` also launches the interface. The program reads `Lyon/metro_lyon.png` and writes `Lyon/recorrido_final.png`. The GUI is not packaged and has not been verified across operating systems.
