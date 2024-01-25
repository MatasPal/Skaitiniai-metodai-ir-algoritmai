
#!pip install pyshp

import matplotlib.pyplot as plt
import shapefile
from shapely import geometry
import pyshp as pyshp

shape = shapefile.Reader("ne_10m_admin_0_countries.shp")

id = -1
for i in range(len(shape)):
  feature = shape.shapeRecords()[i]
  if feature.record.NAME_EN == "Croatia":
    id = i
    break 

if id == -1:
  print("Tokios šalies nėra")
else:
  print("id: " + str(id) )

#id = 5
feature = shape.shapeRecords()[id]
print(feature.record.NAME_EN)
largestAreaID = 0
if feature.shape.__geo_interface__['type'] == 'MultiPolygon': 
  print(len(feature.shape.__geo_interface__['coordinates']))
  area = 0
  for i in range(len(feature.shape.__geo_interface__['coordinates'])):
    points = feature.shape.__geo_interface__['coordinates'][i][0]
    polygon = geometry.Polygon(points)
    if polygon.area > area:
      area = polygon.area
      largestAreaID = i

  xxyy = feature.shape.__geo_interface__['coordinates'][largestAreaID][0]
else:
  xxyy = feature.shape.__geo_interface__['coordinates'][0]

  
xy = list(zip(*xxyy))
print(xy)
X = xy[0]
Y = xy[1]
plt.plot(X,Y, 'bo-')

print(shape)

