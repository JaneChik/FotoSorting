# FotoSorting

### Draft project.
For now you need to specify path to the folder containing photos (additional directories not a problem). Script will create folder for each year with folders for each month in it and move photos in them. 
In the end all photos from the initial directory will be sorted by year and month of last changes.
All other files will be not touched.

### Requirements: 
* windows (because of / in the path)
* used libraries: *os*, *shutil*, *datetime*, *filetype* 

### Things to be added:
1. Deal with different path (windows/unix): *os.path.join()*
2. Make it console app (call script from the console/terminal -> specify path)
3. Add opportunity to select sorting by years/monts/both.
4. Add converting to the jpeg: replace original files / create additional folder for jpg / create additional folder for non-jpg.


