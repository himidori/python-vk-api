import requests
import os
import glob
import time
import urllib
from vk_api import wall_photo_upload


os.system('clear')
files = glob.glob(os.getcwd() + '/to_upload/*')
msg = urllib.parse.quote_plus(input('message: '))
os.sytem('clear')
print('pictures count: ', len(files))
print('****************************************\n')
for i in range(len(files)):
	wall_photo_upload(files[i], msg)
	print('upload {} executed'.format(i))
	time.sleep(30)