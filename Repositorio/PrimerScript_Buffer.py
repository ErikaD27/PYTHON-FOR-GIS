import arcpy

direccionArchivo = r"C:\Documentos\CURSOS\PYTHON_SIG\shape_datosValle (1)\valle_depto.shp"
direccionSalida = r"C:\Documentos\CURSOS\PYTHON_SIG\shape_datosValle (1)\valle_depto_buffer_.shp"
print("archivo de salida")

distancia = "1000 meters"
arcpy.Buffer_analysis(direccionArchivo,direccionSalida,distancia)

print("finalizado")