
import time
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

class fingureprint():
    
    def __init__(self):
       pass

    
    def enroll(self):
                
        ## Enrolls new finger
        ## Tries to initialize the sensor
        
        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        ## Gets some sensor information
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

        ## Tries to enroll new finger
        try:
            print('Waiting for finger...')

        ## Wait that finger is read
            while ( f.readImage() == False ):
                pass

        ## Converts read image to characteristics and stores
            f.convertImage(0x01)

        ## Checks if finger is already enrolled
            result = f.searchTemplate()
            positionNumber = result[0]

            if ( positionNumber >= 0 ):
                print('Template already exists at position #' + str(positionNumber))
                exit(0)

            print('Remove finger...')
            time.sleep(2)

            print('Waiting for same finger again...')

            ## Wait that finger is read again
            while ( f.readImage() == False ):
                pass

    ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

    ## Compares the charbuffers
            if ( f.compareCharacteristics() == 0 ):
                raise Exception('Fingers do not match')
                

    ## Creates a template
            f.createTemplate()

    ## Saves template at new position number
            positionNumber = f.storeTemplate()
            print('Finger enrolled successfully!')
            print('New template position #' + str(positionNumber))
                  
            s=str(positionNumber)

            result = hashlib.sha256(s.encode())
            self.fhashen = result.hexdigest()

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)
            
    def search(self):

        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

## Gets some sensor information
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
        try:
            print('Waiting for finger...')

    ## Wait that finger is read
            while ( f.readImage() == False ):
                pass

    ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)

    ## Searchs template
            result = f.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if ( positionNumber == -1 ):
                print('No match found!')
                exit(0)
            else:
                print('Found template at position #' + str(positionNumber))
                print('The accuracy score is: ' + str(accuracyScore))
            
            s=str(positionNumber)

            result = hashlib.sha256(s.encode())
            self.fhashsc = result.hexdigest()

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)

fp = fingureprint()
fp.enroll()
print("***************************")
print(fp.fhashen)
print("***************************")

for i in range (0,1000):
    i=i

fp.search()
print("***************************")
print(fp.fhashsc)
