from cycler import cycler
import matplotlib.pyplot as plt
import matplotlib
import commpy

# Update matplotlib rcParams for grid and ticks
matplotlib.rcParams['figure.figsize'] = (12, 5)
matplotlib.rcParams['figure.dpi'] = 200

matplotlib.rcParams['axes.grid'] = True  # Enable grid by default
matplotlib.rcParams['grid.color'] = 'black'  # Set grid color
matplotlib.rcParams['grid.alpha'] = 0.7  # Set grid transparency
matplotlib.rcParams['grid.linestyle'] = (0, (6, 4))
matplotlib.rcParams['grid.linewidth'] = 0.5  # Thin grid lines

matplotlib.rcParams['xtick.minor.visible'] = True  # Show minor ticks on x-axis
matplotlib.rcParams['ytick.minor.visible'] = True  # Show minor ticks on y-axis

matplotlib.rcParams['xtick.direction'] = 'in'  # Tick direction (inwards)
matplotlib.rcParams['ytick.direction'] = 'in'

matplotlib.rcParams['axes.prop_cycle'] = cycler(color=['#0000FF', 'r', 'g', 'k'])
matplotlib.rcParams['lines.linewidth'] = 1.5  # Standard line width

matplotlib.rcParams['font.size'] = 12  # Default font size
matplotlib.rcParams['axes.labelsize'] = 15  # Label font size (x, y axis)
matplotlib.rcParams['xtick.labelsize'] = 13  # X-axis tick font size
matplotlib.rcParams['ytick.labelsize'] = 13  # Y-axis tick font size
matplotlib.rcParams['legend.fontsize'] = 10  # Legend font size
matplotlib.rcParams['figure.titlesize'] = 12  # Figure title font size

print("Plotting setup complete!")