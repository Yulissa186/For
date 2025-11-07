from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .main import main # importa la función del main

@csrf_exempt  # para pruebas; en producción es mejor usar token CSRF
def ejecutar(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            codigo = data.get("codigo", "")
            logs = main(codigo)
            return JsonResponse({"logs": logs})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
