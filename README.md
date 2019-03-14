# Spatiotemporal Data Analysis Visualization

### Topics
1. **ArcPy package**:

      for vector data: MakeXYEventLayer_management, Select_analysis, SelectLayerByLocation_management, Buffer_analysis, SpatialJoin_analysis, etc.; 

      for raster data: GetRasterProperties_management, CalculateStatistics_management, CompositeBands_management (for compositing a map based on elevation values), etc.

2. **matplotlib** package for the data visualization, including the population change graph, points/lines/polygons overlaying, etc. 

3. **json** package for converting csv to geojson, loading json files, dumping dictionary into json format, etc.

4. **pandas** package to perform dataframe processing, such as reading csv, appending, combining columns, calculation, etc. 

5. **numpy** package for the array creation and calculation

6. **gdal** package for calculating NDVI with landsat images #from osgeo import gdal: using the gdal module to do the raster processing

7. **scikit-learn** package for K-means Clustering and DBSCAN on geotagged tweets (points with coordinates): https://github.com/mwu233/Spatiotemporal-Data-Analysis-Visualization/blob/master/Scikit-learn-clustering/K-means_and_DBSCAN_geotagged_tweets.ipynb 

8. **tweepy** package for collecting tweets from Twitter Streaming API

9. **ogr** package (OpenGIS Simple Features Reference Implementation) for spatial analysis in finding polylines that intersect with a polygon

10. **fiona**, **shapely**, and **geopandas** for geofeature processing, e.g., reading shapefiles, performing spatial relationship verification including within, intersect, etc.
