from antlr4 import *
from forLexer import forLexer
from forParser import forParser
from EvalVisitor import EvalVisitor

visitor = EvalVisitor()
buffer = []        # Para almacenar líneas de un bloque
open_braces = 0    # Contador de llaves abiertas

while True:
    try:
        prompt = ">>> " if open_braces == 0 else "... "
        line = input(prompt)

        if line.strip() == "salir":
            break

        open_braces += line.count("{")
        open_braces -= line.count("}")

        buffer.append(line)

        # Si todas las llaves cerradas, ejecuta bloque
        if open_braces == 0 and buffer:
            code = "\n".join(buffer) + "\n"
            input_stream = InputStream(code)
            lexer = forLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = forParser(stream)
            tree = parser.prog()        # regla inicial
            visitor.visit(tree)
            buffer = []  # Limpiar buffer

    except EOFError:
        break
    except Exception as e:
        print(f"Error: {e}")
        buffer = []
        open_braces = 0
