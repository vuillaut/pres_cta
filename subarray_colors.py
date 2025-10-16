# script to display a subarray with custom colors for certain telescopes

import ctapipe
print(ctapipe.__version__)

# %%
from ctapipe.instrument import SubarrayDescription

# %%
subarray = SubarrayDescription.from_hdf("/Users/thomas/Work/Projets/CTA/data/ctadirac/prod5/proton_20deg_180deg_run10018___cta-prod5b-lapalma_desert-2158m-LaPalma-dark.alpha_test_alpha_test_applied.DL2.h5")

# %%
# Create a new peek display with custom colors
import matplotlib.pyplot as plt
# Create the display
fig, ax = plt.subplots(figsize=(10, 10))
display = subarray.peek(ax=ax)

# Define which telescopes you want to color in grey
grey_telescopes = [1, 4, 5, 9, 10, 11, 35]  # Modify this list with the telescope IDs you want in grey

# Get the patch collection and modify colors
patches = display.telescopes
colors = patches.get_facecolors().copy()

# Get the telescope positions to map indices
tel_ids = list(subarray.tel.keys())

# Color the specified telescopes in grey
for idx, tel_id in enumerate(tel_ids):
    if tel_id in grey_telescopes:
        colors[idx] = [0.5, 0.5, 0.5, 1.0]  # Grey color (RGBA)

patches.set_facecolors(colors)
patches.set_edgecolors(colors)

# Replace the default title
ax.set_title("An example of triggered telescopes of the North array", fontsize=14)

# Create custom legend with new labels
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='tab:blue', label='MST (Medium Size Telescopes)'),
    Patch(facecolor='tab:orange', label='LST (Large Size Telescopes)'),
    Patch(facecolor='tab:grey', label='Non-triggered Telescopes'),
]
ax.legend(handles=legend_elements, loc='upper right')

plt.savefig("triggered_telescopes_north_array.png", dpi=150)
plt.show()

# %%



