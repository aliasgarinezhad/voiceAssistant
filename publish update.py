import requests
import os

fileName = 'app-debug-' + input('enter version name sir\n') + '.apk'

os.rename("app-release.apk", fileName)

file = open(fileName, 'rb')

print('uploading ' + fileName +  ' ...\n')
response = requests.post('http://rfid-api.avakatan.ir/apk', files={fileName: file})
print(response.text)
input('\n')
