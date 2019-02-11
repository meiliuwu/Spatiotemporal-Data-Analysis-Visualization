import numpy as np # for the array creation and calculation
import gdal
#from osgeo import gdal # using the gdal module to do the raster processing

# use band 4 (near infrared) and band 3 (red) to calc to NDVI
# assue this .py file path and the landsat folder are both under the lab5 folder
ds1 = gdal.Open('landsat\L71026029_02920000609_B40_CLIP.TIF')
ds2 = gdal.Open('landsat\L71026029_02920000609_B30_CLIP.TIF')

# deal with the FileNotFoundException
if ds1 == None or ds2 == None:
    print "cannot open the file"
    sys.exit()

# get the driver
fmt = 'GTiff' # format should be GeoTiff
driver = gdal.GetDriverByName(fmt)

# create output dataset using the driver
cols = ds1.RasterXSize
rows = ds1.RasterYSize
# parameters in order: filename(path),cols,rows,nBands,dataType
dsOut = driver.Create('NDVI_MeiliuWu.TIF', cols, rows, 1, gdal.GDT_Float32)

# set geotransform & projection
trans = ds1.GetGeoTransform() # borrow the GeoTransform from the band 4 dataset
prj = ds1.GetProjection() # borrow the projection from the band 4 dataset
dsOut.SetGeoTransform(trans) # set geotransform for the output dataset
dsOut.SetProjection(prj) # set projection for the output dataset

# calc the output array
arr1 = ds1.GetRasterBand(1).ReadAsArray().astype(np.float) # save band 4 values to an array as float 
arr2 = ds2.GetRasterBand(1).ReadAsArray().astype(np.float) # save band 3 values to another array as float 

# do the calculation according to part of the NDVI equation
up = arr1 - arr2 
bottom = arr1 + arr2

# handle the case where bottom value is 0
# check where values are 0
zero_values_flags = bottom == 0
# all zero values set to an impossible value so that the result will be noticed
bottom[zero_values_flags] = -99999999

# set values for bands and write raster data
band = dsOut.GetRasterBand(1) # a new band for dsOut
band.SetColorInterpretation(gdal.GCI_GrayIndex) # set the new band as a gray-level image
band.WriteArray(up/bottom) # move the data from the calculated array to the band

print "The NDVI image is successfully created!"

# close the datasets
ds1 = None
ds2 = None
dsOut = None
