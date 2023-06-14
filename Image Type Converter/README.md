# Image Type Converter

This Python script offers a way to convert image files between PNG and JPG formats while providing essential information about the images and handling input validation for the directory path and conversion option.

# How to use it 
To use the script , make sure that you have **PIL (Python Imaging Library)**  installed .
You can Install it by running the following command in your command prompt or terminal:
```
pip install pillow
```
To use the script , Open a command prompt or terminal and navigate to the directory where the script is saved .

Run the script by executing the following command :
```
python imgtypecnv.py -d <directory_path> -o <conversion_option>
```
Replace `<directory_path>` with the path to the directory containing the images you want to convert. `<conversion_option>` should be either 1 or 2, indicating the desired conversion operation:

-   Use `1` to convert PNG files to JPG format.
-   Use `2` to convert JPG files to PNG format.

For example, to convert PNG files in the directory "C:\Images" to JPG format, you would run the following command:
```
python imgtypecnv.py -d C:\Images -o 1
```

