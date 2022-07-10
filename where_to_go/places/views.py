from django.shortcuts import render
from .models import Location
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict


def index(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    locations = Location.objects.all()
    for location in locations:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [location.lng, location.lat],
                },
                "properties": {
                    "title": location.title_short,
                    "placeId": location.placeid,
                    "details": {
                        'title': location.title,
                        'imgs': [
                            img.img_url.url for img in
                            location.image_set.all()
                            ],
                        'description_short': location.description_short,
                        'description_long': location.description_long,
                        'coordinates': {
                            'lng': location.lng,
                            'lat': location.lat,
                            }
                        }
                    }
            }
        )
    return render(
        request, 'index.html',
        context={"places_geojson": places_geojson},
        )


def location_detail(request, place_id):
    location_obj = get_object_or_404(Location, pk=place_id)
    images_urls = [image.img_url.url for image in location_obj.images.all()]
    location = model_to_dict(location_obj)
    location['images'] = images_urls
    serialized_location = JsonResponse(
        location,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4},
        )
    return serialized_location
