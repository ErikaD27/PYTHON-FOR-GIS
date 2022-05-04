import arcpy
from arcpy import env
from arcpy.sa import*


CarpetaEntrada = arcpy.GetParameterAsText(0)
folderSalida = arcpy.GetParameterAsText(1)
metros = arcpy.GetParameterAsText(2)

arcpy.env.workspace = CarpetaEntrada
fc = arcpy.ListFeatureClasses("*")
arcpy.AddMessage(fc)

for i in fc:
    direccionShape = CarpetaEntrada+ "/"+i
    archivoSalida = folderSalida + "/" + "_HOLA_" + i
    arcpy.Buffer_analysis(direccionShape,archivoSalida, metros+"meters")
