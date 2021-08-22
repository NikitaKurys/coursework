import requests, json, time, operator
from tqdm import tqdm


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token}'
        }

    def upload(self, vk_url, name_file):
        API_BASE_URL = 'https://cloud-api.yandex.net:443'
        # Получаем фотографии с профиля и сохраняем их на Яндекс диске
        loading = requests.post(API_BASE_URL + "/v1/disk/resources/upload", headers=self.headers, params={
            'url': vk_url,
            'path': "VK_FILES/" + name_file})


class VKUploader:
    def __init__(self, token: str, user_id):
        self.token = token
        self.user_id = user_id
        self.upload_list = []
        self.json_file = []
        self.params = {
            'owner_id': user_id,
            'access_token': token,
            'album_id': 'profile',
            'v': '5.131',
            'extended': '1',
            'photo_sizes': '1'
        }

    def preparation(self):
        api_vk = requests.get("https://api.vk.com/method/photos.get", params=self.params)
        data = json.loads(api_vk.text)
        for files in tqdm(data['response']['items']):
            file_url = files['sizes'][-1]['url']
            api = requests.get(file_url)
            time.sleep(0.1)
            file_name = str(files['likes']['count']) + '.jpeg'
            size = files['sizes'][-1]['type']
            photo_size = files['sizes'][-1]['width'] + files['sizes'][-1]['height']
            # Готовим список для записи в json-файл
            self.json_file.append({
                "file_name": file_name,
                "size": size
            })
            # Готовим список для записи на Яндекс диск самых больших фотографий
            self.upload_list.append({
                "file_name": file_name,
                "size": photo_size,
                "url": file_url
            })

    def get_photo(self):
        # Сортируем список для записи первых 5 самых больших фото
        self.upload_list.sort(key=operator.itemgetter('size'), reverse=True)
        for i in tqdm(self.upload_list[:5]):
            uploader.upload(i['url'], i['file_name'])
        with open('data.txt', 'w', encoding='utf-8') as file:
            json.dump(self.json_file, file, indent=4)


if __name__ == '__main__':
    token =
    uploader = YaUploader(token)
    token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    addendum = VKUploader(token, user_id='208910963')
    addendum.preparation()
    addendum.get_photo()



