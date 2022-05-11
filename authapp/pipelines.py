import requests
from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

from django.utils import timezone
from social_core.exceptions import AuthException, AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('http', 'api.vk.com', 'method/users.get',
                          None, urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'personal', 'photo_max_orig')), access_token=response['access_token'], v=5.131)), None))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    data_sex = {
        1: UserProfile.FEMALE,
        2: UserProfile.MALE,
        3: None
    }

    user.userprofile.gender = data_sex[data['sex']]

    if data['about']:
        user.userprofile.about = data['about']

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year

    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['personal']['langs']:
        user.userprofile.langs = data['personal']['langs'][0]
        if len(data['personal']['langs']) > 1:
            for number in range(len(data['personal']['langs'])):
                if number > 0:
                    user.userprofile.langs = f"{user.userprofile.langs}, {data['personal']['langs'][number]}"

    if user.image:
        photo = requests.get(data['photo_max_orig'])
        path_photo = f"users_image/{user.pk}.jpg"
        with open(f"media/{path_photo}", 'wb') as file:
            file.write(photo.content)
        user.image = path_photo

    user.age = age
    user.save()
