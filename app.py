import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Page title setup
ui.page_opts(title="PyShiny Histogram App", fillable=True)

# Sidebar slider input for bin selection
with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins",  # Unique input ID
        "Number of Bins",           # Display label
        0,                          # Minimum value
        100,                        # Maximum value
        20                          # Initial/default value
    )

# Reactive histogram output
@render.plot(alt="A histogram showing random data distribution")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    # Create histogram and store bar containers
    n, bins, patches = plt.hist(x, input.selected_number_of_bins(), density=True)

    # Set alternating colors: pink and yellow
    colors = ["pink", "yellow"]
    for i, patch in enumerate(patches):
        patch.set_facecolor(colors[i % 2])
