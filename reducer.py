# Required libs: os, netCDF4, pathlib

import os
import netCDF4
import pathlib

print('\n----------------------------------------------------------------')
print('Este programa no modifica ni elimina sus archivos netCDF4 originales, todos los archivos modificados van a estar en la carpeta reduced')
print('\nPara usar este programa, tenés que ubicar los archivos .nc y este programa en la misma carpeta')
print('----------------------------------------------------------------\n')
input('Apretá enter para que el programa empiece a trabajar, o cerra para huir...')

resultsDir = 'reduced'

try:
    os.mkdir(resultsDir)
except OSError as error:
    pass

toinclude = ['time', 'lat', 'lon', 'sea_surface_salinity', 'sea_surface_temperature', 'platform1']

files = os.listdir()
processed = 0

for file in files:

    resultFile = resultsDir + '\\' + file[0:-3] + '_filt.nc'
    
    if file.endswith('.nc'):
        
        print('\nReduciendo variables en: ', file)
        
        with netCDF4.Dataset(file) as src, netCDF4.Dataset(resultFile, 'w') as dst:
            # copia los atributos globales de una como un diccionario
            dst.setncatts(src.__dict__)
            # dst.createDimension('estacion', None)
            # dst.createVariable('estacion', 'str', ('estacion'))
            # dst['estacion'][0] = str(file)
            
            # copia las dimensiones
            for name, dimension in src.dimensions.items():
                dst.createDimension(
                    name, (len(dimension) if not dimension.isunlimited() else None))
            # copia solo los datos a incluir
            for name, variable in src.variables.items():
                if name in toinclude:
                    x = dst.createVariable(name, variable.datatype, variable.dimensions)
                    dst[name].setncatts(src[name].__dict__)
                    dst[name][:] = src[name][:]
                    # copiar los atributos de las variables de una como diccionario
            processed += 1

print('\nListo, se procesaron ' + str(processed) + ' archivos.\n')
print('todos los resultados están en: reduced\ \n')
input('\nTocá enter para salir...')