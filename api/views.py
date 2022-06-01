from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Please visit this url http://localhost:8000/api/products/"})
