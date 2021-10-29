# Required libs: os, netCDF4, pathlib

import os
import netCDF4
import pathlib

def getData(lines):
    data = [[], [], [], [], [], []]   
    
    guardarDatos = False
    dataSet = 0
    for line in lines:
        
        #Empieza un conjunto de datos
        if 'platform' in line:
            dataSet = 5
            guardarDatos = True
            continue
        if 'time' in line:
            dataSet = 0
            guardarDatos = True
            continue
        if 'lat' in line:
            dataSet = 1
            guardarDatos = True
            continue
        if 'lon' in line:
            dataSet = 2
            guardarDatos = True
            continue
        if 'sea_surface_salinity' in line:
            dataSet = 3
            guardarDatos = True
            continue
        if 'sea_surface_temperature' in line:
            dataSet = 4
            guardarDatos = True
            continue
        
        if guardarDatos:
            #Extrae la plataforma
            if dataSet == 5:
                data[dataSet].append(str(line).replace('"','')[:-2].strip())
        
            #Extrae tiempo como número entero
            elif dataSet == 0:
                data[dataSet].append(int(line.replace(" ", "")[:-2]))
            
            #Extrae temperatura, salinidad, longitud y latitud con sus decimales    
            elif any([char.isdigit() for char in line]):
                data[dataSet].append(float(line.replace(" ", "")[:-2]))
        
        #El conjunto de datos terminó
        if ';' in line:
            guardarDatos=False
    
    return data    


print('\n----------------------------------------------------------------')
print('Este programa no modifica ni elimina sus archivos txt originales, todos los archivos modificados van a estar en la carpeta reduced/csv/')
print('\nPara usar este programa, tenés que haber ejecutado antes el nc_to_txt.bat')
print('----------------------------------------------------------------\n')
input('Apretá enter para que el programa empiece a trabajar, o cerra para huir...')

resultsDir = 'reduced/csv/'

try:
    os.mkdir(resultsDir)
except OSError as error:
    pass

processed = 0

headers = 'Time, Latitude, Longitude, Salinity, Temp_ext, Platform'

for file in os.listdir("reduced/"):
    startLine = 0
    endLine = 0
    platform = ""
    
    if file.endswith(".txt"):
        resultFile = resultsDir + '/' + file
        print('\nConvirtiendo en CSV a: ', file)
        
        with open("reduced/" + file) as old, open(resultsDir + file, 'w') as new:
            
            lineNumber = 0
            
            lines = old.readlines()
            
            for line in lines:
                lineNumber += 1
                if 'data:' in line:
                   startLine = lineNumber
                if '} // group /' in line:
                   endLine = lineNumber
            
            dataSet = getData(lines[startLine:endLine - 1])
            
            new.write(headers)
            
            if(dataSet[5]):
                platform = dataSet.pop(5).pop(0)
            
            length = len(dataSet[0])
            
            #Itera según la cantidad máxima de datos (data) que haya en un grupo.
            for data in range(length):
                
                new.write('\n')
                #Recorre el grupo de datos correspondiente y escribe el dato en el txt.
                for dataGroup in range(len(dataSet)):
                    if len(dataSet[dataGroup]) > 0:
                        
                        newData = (str(dataSet[dataGroup].pop(0)))
                        new.write(newData)
                    else:
                        new.write("")
                    if dataGroup != length:
                        new.write(",")
                
                new.write(platform)
            processed += 1
                
                
print('\n\nListo, se procesaron ' + str(processed) + ' archivos.\n')
print('todos los resultados están en: reduced\csv\ \n')        
input('\nTocá enter para salir...')