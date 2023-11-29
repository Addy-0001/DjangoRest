from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     #This whole thing is called serialization.
    #     # Model Instance = model_data.
    #     # turn it into a python dictionary
    #     # return json to the client

    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
