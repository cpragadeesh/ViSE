from ftplib import FTP
import base64
import os

ftp_HOST = 's178972.gridserver.com'
ftp_USERNAME = 'praveenramc.me'
ftp_PASSWORD = 'c0UwIzQ3fnJvVA=='

def connectFTP():
    ftpClient = FTP("s178972.gridserver.com")

    print 'Authenticating...'
    ftpClient.login(user = ftp_USERNAME, passwd = base64.b64decode(ftp_PASSWORD))
    print 'Connected.'

    ftpClient.cwd('/domains/cpragadeesh.net/html/vice-images')

    return ftpClient

def upload(fileDir):
    ftpClient = connectFTP()

    for img in os.listdir(fileDir):
        imgFile = open(fileDir + img)
        print 'Uploading...'
        ftpClient.storbinary('STOR %s'%img, imgFile)
        imgFile.close()
        os.system('rm %s' % (fileDir + img))

        
    
    
