# import the following libraries
#pip3 install pytesseract
#pip3 install image
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

val = input("Enter the file name: ")
inputFileName = val+'.jpg'
oututFileName = val+'.txt'
# opening an image from the source path
#img = Image.open('4600187.jpg')
img = Image.open(inputFileName)	

# describes image format in the output
#print(img)						
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ='C:/Tesseract/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
#with open('4600187.txt',mode ='w') as file:
with open(oututFileName,mode ='w') as file:
    file.write(result)
    #print(result)
    print("Converted "+inputFileName+" To Text file "+oututFileName)
    
output=""
with open(oututFileName) as f:
    for line in f:
        if not line.isspace():
            output+=line
            
f= open(oututFileName,"w")
f.write(output)
