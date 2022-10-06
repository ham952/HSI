from pickletools import uint8
import numpy as np
import rasterio
import spectral
import matplotlib.pyplot as plt
import os
from hs_process import hsio, spatial_mod 

data_dir = r'E:\PhD\HyperSpectral\Pika L Dataset\Downloads\Pika L airborne flight datacubes'
data_cube_hdr = os.path.join(data_dir, 'Pika_L-datacube.bsq.hdr')

# data_dir = r'E:\PhD\HyperSpectral\Extra Dataset\hs_process\hs_process sample data'
# data_cube_hdr = os.path.join(data_dir,'Wells_rep2_20180628_16h56m_pika_gige_7-Radiance Conversion-Georectify Airborne Datacube-Convert Radiance Cube to Reflectance from Measured Reference Spectrum.bip.hdr')

io = hsio()

# Load Data cube
io.read_cube(data_cube_hdr)

print(io.spyfile)

print('\n')

io.read_spec(data_cube_hdr)
print(io.spyfile_spec)

# print('name_long: {0}'.format(io.name_long))
# print('name_short: {0}'.format(io.name_short))
# print('name_plot: {0}'.format(io.name_plot))



# Perform simple spatial cropping
my_spatial_mod = spatial_mod(io.spyfile)  # initialize spatial_mod instance to crop the image
array_crop, metadata = my_spatial_mod.crop_single(pix_e_ul=0, pix_n_ul=0, crop_e_m=462, crop_n_m=1194)
# array_crop, metadata = my_spatial_mod.crop_single(pix_e_ul=250, pix_n_ul=100, crop_e_m=8, crop_n_m=3)

# Show image
# io.show_img(array_crop)

ax = plt.subplot()


# array = array_crop.astype(float)
array = array_crop
# band_r = 120
# band_g = 76
# band_b = 32

band_r = 59
band_g = 37
band_b = 16

try:
    fig = ax.imshow(array, (band_r, band_g, band_b))
except:
    #fig = ax.imshow(array[:, :, [band_r, band_g, band_b]]*5.0)
    # fig = ax.imshow((array[:, :, [band_r, band_g, band_b]]*255.0).astype(np.uint8))
    fig = ax.imshow((array[:, :, [band_r, 0, 0]]*255.0).astype(np.uint8))   # single band
    fig = ax.imshow((array[:, :, [band_r]]*255.0).astype(np.uint8))

plt.show()
# plt.imshow(array[:, :, [band_r, band_g, band_b]]*255.astype(np.uint8))