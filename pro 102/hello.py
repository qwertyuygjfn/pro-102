import cv2
import dropbox
import random
import time
starttime=time.time()
def snapshot ():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videocaptureobject.read()
        print(ret)
        imagename="img"+str(number)+".png"

        cv2.imwrite(imagename,frame)
        result=False
        videocaptureobject.release()
        cv2.destroyAllWindows()
    return imagename
    print("snapshot taken")    
def uploadfiles(imagename):
    
    access_token = 'sl.BFxwUsWMZf1UkwdQYkWjyOtNRnWzuxUMSH-yEu8-T0gRwbPEoqKN1lXqu4RSBmk4FzXbhMw5zH26RzFALYpecaN6sDKr6cOxpgLKauVqlZCpXva2mW5O0EMy9mx720OcqNljOmH5PZ-X'
    file=imagename
    file_from=file
    file_to="/test/"+(imagename)
    dbx=dropbox.Dropbox(access_token)
    with open (file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

    # API v2
  
def main():
    while (True):
        if ((time.time()-starttime)>=5):
            name=snapshot()
            uploadfiles(name)
main()            
   
