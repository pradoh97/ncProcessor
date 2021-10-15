set path=reduced\
for /r %%v in (%path%*.nc) do C:\nco\ncks.exe "%path%%%~nv.nc" > "%path%%%~nv.txt"