from django.core.management.base import BaseCommand, CommandError
from places.models import Location, Image
import requests
from requests.exceptions import ConnectionError
import os
from django.conf import settings
from urllib.parse import urlparse


def load_images_to_location(location_obj, image_url):
    parsed_url = urlparse(image_url)
    img_file_name = os.path.basename(parsed_url.path)
    img_file_path = os.path.join(
        settings.MEDIA_ROOT,
        'places_images',
        img_file_name,
        )
    response = requests.get(image_url, allow_redirects=True)
    with open(img_file_path, 'wb') as file_handler:
        file_handler.write(response.content) 
    Image.objects.create(
        img_url=os.path.join('places_images', img_file_name),
        location=location_obj,
        )


def save_location_to_db(location):
    location_obj, created = Location.objects.get_or_create(
        title=location['title'],
        title_short=location['title'],
        description_short=location['description_short'],
        description_long=location['description_long'],
        lng=location['coordinates']['lng'],
        lat=location['coordinates']['lat'],
        placeid=location['title'],
        )
    return location_obj, created
    

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_url')

    def handle(self, *args, **kwargs):
        json_url = str(kwargs['json_url'])
        try:
            response = requests.get(json_url)
        except ConnectionError as error:
            exit('При вызове сервиса возникла ошибка:\n{}'.format(error))
        location = response.json()
        location_obj, created = save_location_to_db(location)
        if created:
            print('Место {} успешно сохранено в базу данных сайта!'.format(
                location['title'],
                ))
            for image_url in location['imgs']:
                try:
                    load_images_to_location(location_obj, image_url)
                    print('Картинка {} успешно загружена!'.format(image_url))
                except ConnectionError as error:
                    print('Не удалось скачать картинку {}'.format(image_url))
            
