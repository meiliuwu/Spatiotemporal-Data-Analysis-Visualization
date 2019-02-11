import arcpy
import os

arcpy.CheckOutExtension("Spatial")

# set up the workspace
arcpy.env.workspace = 'c:\data'

# calculate slope
outraster = arcpy.sa.Slope("elevation.tif")

# get min and max
arcpy.CalculateStatistics_management(outraster)
MINResult = arcpy.GetRasterProperties_management(outraster, "MINIMUM")
zMin = float(MINResult.getOutput(0))
MAXResult = arcpy.GetRasterProperties_management(outraster, "MAXIMUM")
zMax = float(MAXResult.getOutput(0))

# create output
outName = 'c:\data\SlopeColored.tif'

if os.path.exists(outName):
    os.remove(outName)

# create raster of scaled Slope values
f = ((outraster -zMin)/(zMax-zMin))
# create the red raster
R = 255* (outraster/outraster)
# green and blue raster values are identical
G = f * 255
B = f * 255
 
#Compose single band datasets to a TIFF format raster file
arcpy.CompositeBands_management(str(R)+';'+str(G)+';'+str(B),outName)

print "Task2 is finished."
