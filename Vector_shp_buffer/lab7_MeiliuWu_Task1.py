import arcpy

## set up working environment
#arcpy.env.workspace = "c:\lab_data.gdb"
arcpy.env.workspace = "lab_data.gdb"
arcpy.env.overwriteOutput = True

## Task 1:
## set feature class name
fc1 = "PowerLine"
fc2 = "Parcels"

## buffer analysis
# the buffer analysis requires the input to be a feature layer
arcpy.MakeFeatureLayer_management(fc1, "PowerLine_lyr")
# can add more optional parameters
arcpy.Buffer_analysis("PowerLine_lyr", "PowerLine_buffer", "250 feet") 

# select feature by location
arcpy.MakeFeatureLayer_management(fc2,"Parcels_lyr")

arcpy.MakeFeatureLayer_management("PowerLine_buffer",\
                                  "PowerLine_buffer_lyr")

arcpy.SelectLayerByLocation_management("Parcels_lyr",\
                                       "COMPLETELY_WITHIN",\
                                       "PowerLine_buffer_lyr")

# create output feature class 
sr = arcpy.Describe("Parcels_lyr").spatialReference
# spatial reference
arcpy.CreateFeatureclass_management(arcpy.env.workspace,\
                                    "Parcels_COMPLETELY_WITHIN",\
                                    "POLYGON",\
                                    fc2,\
                                    "SAME_AS_TEMPLATE",\
                                    "SAME_AS_TEMPLATE",\
                                    sr)

# add selection to output feature class (input, output)
arcpy.Append_management("Parcels_lyr","Parcels_COMPLETELY_WITHIN")

print "Task 1 is done successfully!"

