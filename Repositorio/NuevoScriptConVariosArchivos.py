import arcpy
carpetaArchivosEntrada = r"C:\Documentos\CURSOS\PYTHON_SIG\shape_datosValle (1)"
carpetaSalida = r"C:\Documentos\CURSOS\PYTHON_SIG\Varios_archivos"

arcpy.env.workspace = carpetaArchivosEntrada
listadoShapes = arcpy.ListFeatureClasses("*")
#se listan los features

#print listadoShapes

for shape in listadoShapes:
    archivoSalida = carpetaSalida +"/"  + shape
    arcpy.Buffer_analysis(shape,archivoSalida,"100 meters")
    print(archivoSalida)

