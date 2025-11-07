from antlr4 import *
from forLexer import forLexer
from forParser import forParser
from EvalVisitor import EvalVisitor

def ejecutar_codigo(codigo: str):
    """
    Ejecuta el código recibido como string usando tu intérprete ANTLR
    y devuelve los logs de ejecución.
    """
    visitor = EvalVisitor()
    input_stream = InputStream(codigo)
    lexer = forLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = forParser(stream)
    tree = parser.prog()
    visitor.visit(tree)
    return visitor.logs
