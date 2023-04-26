import uuid

from django.views.decorators.csrf import csrf_exempt

from .models import UrlShort
import requests
from bs4 import BeautifulSoup
from .utils import generate_shorted_url
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def create_short_url(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            url = json_data['url']
            slug = generate_shorted_url(len(UrlShort.objects.all()))
            shorted_url = request.build_absolute_uri(slug)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            title = soup.title.string
            short_url_item = UrlShort.objects.create(
                url=url,
                slug=slug,
                shorted_url=shorted_url,
                title=title
            )
            return JsonResponse({"short_url":shorted_url},status=200)

        except Exception as e:
            print(e)
            return JsonResponse(status=500)


