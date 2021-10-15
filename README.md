# ncProcessor
A series of scripts to reduce and parse netCDF files to work with data on any spreadsheets program or in Ocean Data View

# Dependencies
Python 3.7 (it may work on any 3.x version), NCO or NetCDF Operators http://nco.sourceforge.net/ (you can grab it from that site) and some nc files :D

# How to use the reducer?
If you want to reduce to certain variables place the reducer.py in the same folder as the .nc files. Don't worry, it won't modify the original files, all the results are placed in a new folder called "reduced".

The predefined variables are the ones in "toinclude" array, namely ['time', 'lat', 'lon', 'sea_surface_salinity', 'sea_surface_temperature', 'platform1']
Feel free to remove/add the ones you need.

Once you have this, you can proceed and execute it.

# How to use the nc to txt tool?
Place it in the same folder as the .nc files. The script has a hardcoded path where it's going to look for the files to convert, also feel free to change it.

Once you have this, you can proceed and execute it.

# How to use the txt to csv tool?
The input for this tool are txt files. Specifically nc files that were converted to txt, to achieve this, you can use the nc to txt tool. Feel free to modify the headers (this are the first row for the CSV file), the resultsDir (where results are going to be placed) and the originalFilesDir (where the txt files are initially).

The getData function has some hardcoded values, this are the variable names from the NC file, also feel free to change them.

Once you have this, you can proceed and execute it.

# Do you have ideas to improve this?
This project was done for a very specific use case so it might not fit your exact needs. Feel free to share your thoughts or questions.
