from django.shortcuts import render
from .models import Location


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
                            location.images.order_by('title')
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
