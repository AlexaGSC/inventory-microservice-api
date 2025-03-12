from django.http import JsonResponse
from django.contrib.auth.models import User

def listar_usuarios(request):
    usuarios = list(User.objects.values())
    return JsonResponse(usuarios, safe=False)
