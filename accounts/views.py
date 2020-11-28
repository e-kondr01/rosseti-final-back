from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def check_role(request):
    group = request.user.groups.first().name
    print(request.user)
    resp = {
        'group': group
    }
    return JsonResponse(resp)
