import sys
import os
import cv2 
import matplotlib.pyplot as plt 
import pathlib2
  
folderWithImages = ""   
face_detect = cv2.CascadeClassifier('C:\\Python313\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml') 
face_detect2 = cv2.CascadeClassifier('C:\\Python313\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml') 

def StartCheck(isFileOrFolder, folderWithImages, fileImage, scaling):    
    if isFileOrFolder == 'folder':     
        if folderWithImages:                         
            filesList = os.listdir(folderWithImages)                
            filePath = pathlib2.Path(folderWithImages).resolve()    
            newFilePath = str(filePath) + '\\blur\\'        
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath)        
            for file in filesList:                       
                if os.path.isfile(os.path.join(filePath, file)):
                    newFileName = file.rsplit('.', 1)[0] + '_b.png'
                    newFile = newFilePath + newFileName                    
                    FindAndBlurFace(str(filePath) + '\\' + file, newFile, scaling)          
            sys.exit() 
    else:
        if fileImage:
            filePath = pathlib2.Path(fileImage).parent.resolve() 
            newFilePath = str(filePath) + '\\blur\\'  
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath) 
            newFileName = fileImage.rsplit('.', 1)[0] + '_b.png'
            newFileName = newFileName.rsplit('\\', 1)[1]
            newFile = newFilePath + newFileName            
            FindAndBlurFace(fileImage, newFile, scaling) 
            sys.exit() 
   

def FindAndBlurFace(imgPath, newFilePath, scaling):
    # Reading an image using OpenCV 
    # OpenCV reads images by default in BGR format    
    image = cv2.imread(imgPath)       
    
    # Converting BGR image into a RGB image 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
    face_data = face_detect.detectMultiScale(image, 1.3, 5) 
      
    # Draw rectangle around the faces which is our region of interest (ROI) 
    for (x, y, w, h) in face_data:         
        roi = image[y:y+h, x:x+w] 
        # applying a gaussian blur over this new rectangle area 
        #roi = cv2.GaussianBlur(roi, (23, 23), 30) 
        roi = cv2.stackBlur(roi, (101,101))
        # impose this blurred image on original image to get final image 
        image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi 
        
    # Display the output 
    height, width, channels = image.shape    
    SaveImage(image, newFilePath, width / 100 , height / 100, scaling) 
    
    #2nd pass
    image = cv2.imread(imgPath)           
    # Converting BGR image into a RGB image 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
    face_data = face_detect2.detectMultiScale(image, 1.3, 5) 
      
    # Draw rectangle around the faces which is our region of interest (ROI) 
    for (x, y, w, h) in face_data: 
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        roi = image[y:y+h, x:x+w] 
        # applying a gaussian blur over this new rectangle area 
        #roi = cv2.GaussianBlur(roi, (23, 23), 30) 
        roi = cv2.stackBlur(roi, (101,101))
        # impose this blurred image on original image to get final image 
        image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi 
        
    # Display the output 
    height, width, channels = image.shape
    
    SaveImage(image, newFilePath, width / 100 , height / 100, scaling) 

# A function for plotting the images     
def SaveImage(img, newFile, width, height, scaling): 
    if (scaling == '100'):
        plt.figure(figsize=(width, height), dpi=125)
    plt.imshow(img) 
    plt.axis('off') 
    plt.style.use('default')     
    plt.savefig(newFile, bbox_inches='tight', pad_inches=0)    
    
isFileOrFolder = str(sys.argv[1]) 
folderWithImages = str(sys.argv[2])
fileImage = str(sys.argv[3])
scaling = str(sys.argv[4])
StartCheck(isFileOrFolder, folderWithImages, fileImage, scaling)