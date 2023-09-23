from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def json(request):
    dic = {
        "ID" : "123",
        "Name": "Tingwei",
    }
    return Response(dic)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def no_index(request):
    return HttpResponse("No index.")