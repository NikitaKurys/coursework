import requests, json, time, pyprind


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token}'
        }

    def upload(self, vk_url, name_file):
        API_BASE_URL = 'https://cloud-api.yandex.net:443'
        #Получаем фотографии с профиля и сохраняем их на Яндекс диске
        loading = requests.post(API_BASE_URL + "/v1/disk/resources/upload", headers=self.headers, params={
            'url': vk_url,
            'path': "VK_FILES/" + name_file})


class VKUploader(YaUploader):

    def get_photo(self, user_id):
        api_vk = requests.get("https://api.vk.com/method/photos.get", params={
            'owner_id': user_id,
            'access_token': token,
            'album_id': 'profile',
            'v': '5.131',
            'extended': '1'
        })

        json_file = []
        data = json.loads(api_vk.text)
        #Делаем прогресс-бар
        bar = pyprind.ProgPercent(len(data['response']['items']))
        for files in data['response']['items']:
            file_url = files['sizes'][-1]['url']
            api = requests.get(file_url)
            time.sleep(0.1)
            file_name = str(files['likes']['count']) + '.jpeg'
            size = files['sizes'][-1]['type']
            uploader.upload(file_url, file_name)
            #Готовим словарь для записи  в json-файл
            json_file.append({
                "file_name": file_name,
                "size": size
            })
            bar.update()
        with open('data.txt', 'w', encoding='utf-8') as file:
            json.dump(json_file, file)



if __name__ == '__main__':
    token =
    uploader = YaUploader(token)
    token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    addendum = VKUploader(token)
    addendum.get_photo('552934290')




