import numpy as np
import matplotlib.pyplot as plt

from ctapipe.instrument import CameraGeometry
from ctapipe.visualization import CameraDisplay
from ctapipe.utils import get_dataset_path
from ctapipe.io import EventSource
from ctapipe.calib import CameraCalibrator
from ctapipe.image.cleaning import tailcuts_clean
from ctapipe.image.hillas import hillas_parameters
from copy import deepcopy
import os
from ctapipe.io import read_table


### CONFIG ###
filename = '/Users/thomasvuillaume/Work/CTA/Data/DL0/Simtel/LST_mono/proton_20deg_180deg_run1___cta-prod3-demo-2147m-LaPalma-baseline-mono.dl1.h5'
# filename = '/Users/thomasvuillaume/Work/CTA/Data/LST1/20200218/v0.6.1_v05/dl1_LST-1.Run02011.0000.h5'
output_dir = 'lst_MC_images'
number_images = 100
clip_times = [0, 50]


geom = CameraGeometry.from_name('LSTCam')
# image_table = read_table(filename, path='/dl1/event/telescope/image/LST_LSTCam')
image_table = read_table(filename, path='/dl1/event/telescope/images/tel_001')


os.makedirs(output_dir, exist_ok=True)



visible_axis = True

fig, axes = plt.subplots(1, 2, figsize=(15,5))

d0 = CameraDisplay(geom, ax=axes[0])
axes[0].set_title('charges')
d0.add_colorbar(ax=axes[0])
d0.colorbar.set_label('photo-electrons')

d1 = CameraDisplay(geom, ax=axes[1])
axes[1].set_title('times')
d1.add_colorbar(ax=axes[1])
d1.colorbar.set_label('nano-seconds')

for ax in axes:
        ax.get_xaxis().set_visible(visible_axis)
        ax.get_yaxis().set_visible(visible_axis)
        if not visible_axis:
            ax.axis('off')
            ax.set_title('')

fig.patch.set_visible(visible_axis)

for ii, (image, pulse_time) in enumerate(image_table['image', 'peak_time'][:number_images]):

    pulse_time[(pulse_time<clip_times[0]) | (pulse_time>clip_times[1])] = 0
    d0.image = image
    d1.image = pulse_time
    
    plt.savefig(os.path.join(output_dir, f'event_{ii}.png'), dpi=200, transparent=True)
    
    




