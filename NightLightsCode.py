### QGIS Version 3.28.2

### Night Lights Country Extraction Project

## Useful Links 
# World Bank Project Description:  https://worldbank.github.io/OpenNightLights/wb-light-every-night-readme.html
# Light File Downloads: https://www.ncei.noaa.gov/products/dmsp-operational-linescan-system 
## Unzipped files with WinZip (free trial available)
# Country Boundaries: https://thematicmapping.org/downloads/world_borders.php 

##CITE: Image and data processing by NOAA's National Geophysical Data Center. DMSP data collected by US Air Force Weather Agency.
##TIF INFO: The cleaned up avg_vis 
#    contains the lights from cities, towns, and other sites with persistent
#    lighting, including gas flares. Ephemeral events, such as fires have
#    been discarded. Then the background noise was identified and replaced
#    with values of zero. Data values range from 1-63. Areas with zero
#    cloud-free observations are represented by the value 255.



## First, I load in all stable lights tif files & the Country Boundaries Shape File
# This can be done with simple code, but there were only 21 years, so I just did it manually
# See: layer = QgsRasterLayer(file, baseName)

## Next, I draw the sum of all annual night lights in the countries in the shapefile for all of the years in the Raster files

processing.run("saga:rasterstatisticsforpolygons", {'GRIDS':['C:/Users/elisa/OneDrive/Desktop/Night lights/F101992.v4/F101992.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F101993.v4/F101993.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F121994.v4/F121994.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F121995.v4/F121995.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F121996.v4/F121996.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F141997.v4/F141997.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F141998.v4/F141998.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F141999.v4/F141999.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F152000.v4/F152000.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F152001.v4/F152001.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F152002.v4/F152002.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F152003.v4/F152003.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162004.v4/F162004.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162005.v4/F162005.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162006.v4/F162006.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162007.v4/F162007.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162008.v4/F162008.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F162009.v4/F162009.v4b_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F182010.v4/F182010.v4d_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F182011.v4/F182011.v4c_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F182012.v4/F182012.v4c_web.stable_lights.avg_vis.tif','C:/Users/elisa/OneDrive/Desktop/Night lights/F182013.v4/F182013.v4c_web.stable_lights.avg_vis.tif'],'POLYGONS':'C:\\Users\\elisa\\OneDrive\\Desktop\\Night lights\\TM_WORLD_BORDERS-0.3\\TM_WORLD_BORDERS-0.3.shp','NAMING':1,'METHOD':0,'PARALLELIZED':False,'RESULT':'TEMPORARY_OUTPUT','COUNT':False,'MIN':False,'MAX':False,'RANGE':False,'SUM':True,'MEAN':False,'VAR':False,'STDDEV':False,'GINI':False,'QUANTILES':'NONE'})

## Then, double check attribute table is correctly filled and then export 
file_path = r"C:\Users\elisa\OneDrive\Desktop\Night lights\Night Lights Country Boundaries (1992-2013).qgz"

layer = QgsVectorLayer(file_path, "Statistics", "ogr")

QgsVectorFileWriter.writeAsVectorFormat(layer,
r"C:\Users\elisa\OneDrive\Desktop\Night lights\NightLights Sum by Country Year.csv",
"utf-8",driverName = "CSV" , layerOptions = ['GEOMETRY=AS_XYZ'])


###Now, you have a night lights CSV file ready to merge by ISO Code and Year to your larger dataset!
