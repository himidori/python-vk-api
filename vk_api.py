import requests

ACCESS_TOKEN = 'your token here'


def wall_photo_upload(image_path, message):
	upload_server = requests.get('https://api.vk.com/method/photos.getWallUploadServer?group_id={}&access_token={}'.format(113447877, ACCESS_TOKEN)).json()['response']['upload_url']
	imageData = open(image_path, "rb")
	images = {}
	images['file'] = imageData
	post = requests.post(url = upload_server, files = images).json()
	server = post['server']
	photo = post['photo']
	hash = post['hash']
	save_photo = requests.get('https://api.vk.com/method/photos.saveWallPhoto?group_id={}&photo={}&server={}&hash={}&access_token={}'.format(113447877, photo, server, hash, ACCESS_TOKEN)).json()['response'][0]['id']
	post_photo = requests.get('https://api.vk.com/method/wall.post?owner_id={}&message={}&access_token={}&attachments={}&from_group=1&signed=1'.format(-113447877, message, ACCESS_TOKEN, save_photo)).json()