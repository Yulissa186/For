from django.shortcuts import render
from django.http import JsonResponse
from antlr4 import *
from .forLexer import forLexer
from .forParser import forParser
from .EvalVisitor import EvalVisitor


def index(request):
    return render(request, "Ciclo_For/index.html")


def ejecutar_codigo(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo", "")
        try:
            # Crear flujo de entrada para ANTLR
            input_stream = InputStream(codigo)
            lexer = forLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = forParser(stream)
            tree = parser.prog()

            # Crear el visitor e interpretar el código
            visitor = EvalVisitor()
            visitor.visit(tree)

            # Recuperar resultados
            resultado = visitor.memory            # Variables finales
            iteraciones = visitor.logs            # Lista de iteraciones

            return JsonResponse({
                "resultado": str(resultado),
                "iteraciones": iteraciones
            })

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Método no permitido"})
