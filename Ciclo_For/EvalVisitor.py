from .forParser import forParser
from .forVisitor import forVisitor


class EvalVisitor(forVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}   # Guarda las variables
        self.logs = []     # Guarda las iteraciones para mostrar en la web

    # --- Reglas principales ---
    def visitProg(self, ctx: forParser.ProgContext):
        for stat in ctx.stat():
            self.visit(stat)
        return self.memory

    # --- Sentencias ---
    def visitAssign(self, ctx: forParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitAssignExpr(self, ctx: forParser.AssignExprContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrintExpr(self, ctx: forParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitForStatement(self, ctx: forParser.ForStatementContext):
        # Inicialización (ej: i = 0)
        if ctx.assignExpr(0):
            self.visit(ctx.assignExpr(0))

        iteracion = 0

        # Bucle principal
        while True:
            # Condición (ej: i < 3)
            condition = 1.0
            if ctx.expr():
                condition = self.visit(ctx.expr())
            if condition == 0.0:
                break

            iteracion += 1

            # Guarda el estado actual de las variables
            estado = f"Iteración {iteracion}: {self.memory}"
            self.logs.append(estado)
            print(estado)

            # Ejecuta el bloque del ciclo
            self.visit(ctx.bloque())

            # Incremento (ej: i = i + 1)
            if ctx.assignExpr(1):
                self.visit(ctx.assignExpr(1))

        # Resultado final del ciclo
        self.logs.append(f"Resultado final: {self.memory}")
        return self.memory

    def visitBlock(self, ctx: forParser.BlockContext):
        for stat_ctx in ctx.stat():
            self.visit(stat_ctx)
        return 0

    # --- Expresiones ---
    def visitNum(self, ctx: forParser.NumContext):
        return float(ctx.getText())

    def visitId(self, ctx: forParser.IdContext):
        var_name = ctx.ID().getText()
        if var_name in self.memory:
            return self.memory[var_name]
        raise NameError(f"Error: Variable '{var_name}' no definida")

    def visitAddSub(self, ctx: forParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right

    def visitMulDiv(self, ctx: forParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Error: División por cero")
            return left / right
        return 0.0

    def visitComparison(self, ctx: forParser.ComparisonContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '==': return 1.0 if left == right else 0.0
        if op == '!=': return 1.0 if left != right else 0.0
        if op == '<':  return 1.0 if left < right else 0.0
        if op == '>':  return 1.0 if left > right else 0.0
        if op == '<=': return 1.0 if left <= right else 0.0
        if op == '>=': return 1.0 if left >= right else 0.0
        return 0.0

    def visitParens(self, ctx: forParser.ParensContext):
        return self.visit(ctx.expr())
