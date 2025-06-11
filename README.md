# blurfaces
This is a Windows program using Python that blurs faces in images. 

**This project has an MIT LICENSE. Read the license for more information.**

# Description
This program uses two versions of the Haar cascades classifier for face detection to detect faces in images using OpenCV for Python. It then uses OpenCV to blur the image and Matplotlib to save the image according to dimensions specified, since OpenCV loses the image dimensions in the process.

This program uses two versions to accomplish a higher rate of face detection, but Haar cascades classifiers are not perfect. It has a greater rate of success finding and blurring faces when a person is not wearing glasses. If a person is wearing glasses, then it works best if the person is facing directly forward. Without glasses, it is pretty good at finding faces even if a person has their head slightly turned.

## Table of Contents
- [Install Python](https://github.com/hexabethimal/blurfaces/#install-python)
- [Download and Unzip the file from Releases](https://github.com/hexabethimal/blurfaces/#Download-and-Unzip-the-file-from-Releases)
- [Run BlurFaces.exe](https://github.com/hexabethimal/blurfaces/#run-blurfaces.exe)

## Install Python
Python is a programming language that helps people write instructions for computers in a way that’s easy to read and understand.
1. Download and install the latest version of Python [Python download](https://www.python.org/downloads/)
2. Install Python. **Important** Check the checkbox for 'Add to Path'. Select Custom Install. Under Advanced options during the install, change the Customize install location to `C:\Python313`.

## Download and Unzip the file from Releases
1. Download BlurFaces.zip and unzip it
2. First run pythonlibs.bat
  - This will simply install the required Python libraries: pathlib2, matplotlib, opencv-python
  - If you don't want to run the bat file, you can simply install the libraries yourself using pip
3. Move the blurall.py file to your C:\Python313 folder
4. Move BlurFaces.exe to wherever you want to run the program, such as your Desktop

## Run BlurFaces.exe
1. Double-click to start the BlurFaces that you moved in step 4

## Using BlurFaces
1. If you want to blur a face in a single image, click 'Select Image' button on the right side and choose the image you want. Then choose the scaling option. Lastly, click 'Blur Selected Image' button.
  - When it is finished, this will open a new folder inside your image folder, named 'Blur' with the blurred image inside it. This way it doesn't overwrite the original image file, while preserving the same file name.
3. If you want to blur every image in a folder, first move all of your images to a single folder. Then click 'Select Folder' button on the left side, choose your folder. Then choose the scaling option. Lastly, click 'Blur Selected Image' button.
  - When it is finished, this will open a new folder inside your image folder, named 'Blur' with all the blurred images inside it. This way it doesn't overwrite the original image files, while preserving all the same file names.
