import ogr
import gdalconst
import sys

# put the PowerLine.shp and Parcels.shp under the same folder of this .py file
filename1 = 'PowerLine.shp'
filename2 = 'Parcels.shp'

# get driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# open file
lineDS = driver.Open(filename1, gdalconst.GA_ReadOnly)
polygonDS = driver.Open(filename2, gdalconst.GA_ReadOnly)

# verify the file was opened, exit if not
if lineDS is None:
    print 'Failed to open', filename1
    sys.exit()
if polygonDS is None:
    print 'Failed to open', filename2
    sys.exit()

# get data layer
lineLayer = lineDS.GetLayer(0) # 0 indicates the first layer

# get spatial reference
##print lineLayer.GetSpatialRef()
##print

# get feature; there is only one feature in this layer
lineFeat = lineLayer.GetFeature(0) # 0 indicates the first line feature

# get geometry
lineGeom = lineFeat.GetGeometryRef()

#Task 1
# get length of line
lineLen_ft = lineGeom.Length()
# convert feet to mile
lineLen_mile = lineLen_ft / 5280.0
print 'Task 1: calculate the length of the power line in miles ' 
print 'The length of the power line is',round(lineLen_mile,2),"miles."
print

# Task 2.a
# get information of shapefile fields from the Parcels polygon
print 'Task 2.a: print attribute names and attribute data types of the Parcels layer'
polygonLayer = polygonDS.GetLayer(0)
polygonLayerDefn = polygonLayer.GetLayerDefn()
fCount = polygonLayerDefn.GetFieldCount()
print ('Field Name\tField Type').expandtabs(15)
print '--'*15
for i in range(fCount):
    fDefn = polygonLayerDefn.GetFieldDefn(i)
    fName = fDefn.GetName()
    fTypeCode = fDefn.GetType()
    fType = fDefn.GetFieldTypeName(fTypeCode)
    print (fName + '\t' + fType).expandtabs(15)
print

# Task 2.b
# get values of feature fields
print "Task 2.b: print the owners' addresses and the areas of the parcels crossed by the power line."
featureCount = polygonLayer.GetFeatureCount()
print ('Address\tArea(sq ft)').expandtabs(20)
print '--'*20
for i in range(featureCount):
    polygonFeat = polygonLayer.GetFeature(i)
    polygonGeom = polygonFeat.GetGeometryRef()
    if polygonGeom.Intersects(lineGeom):
        # get field by fieldname
        print (polygonFeat.GetField('SITUSADDR') + '\t' + \
               str(polygonFeat.GetField('AREA')))\
              .expandtabs(20)
print

lineDS = None
polygonDS = None
