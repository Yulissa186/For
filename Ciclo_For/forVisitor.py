# Generated from for.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete generic visitor for a parse tree produced by forParser.

class forVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by forParser#prog.
    def visitProg(self, ctx:forParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Assign.
    def visitAssign(self, ctx:forParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#ForLoop.
    def visitForLoop(self, ctx:forParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#PrintExpr.
    def visitPrintExpr(self, ctx:forParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#ForStatement.
    def visitForStatement(self, ctx:forParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#assignExpr.
    def visitAssignExpr(self, ctx:forParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Block.
    def visitBlock(self, ctx:forParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#MulDiv.
    def visitMulDiv(self, ctx:forParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#AddSub.
    def visitAddSub(self, ctx:forParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Comparison.
    def visitComparison(self, ctx:forParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Parens.
    def visitParens(self, ctx:forParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Num.
    def visitNum(self, ctx:forParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#Id.
    def visitId(self, ctx:forParser.IdContext):
        return self.visitChildren(ctx)



del forParser