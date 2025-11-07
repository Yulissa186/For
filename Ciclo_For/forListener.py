# Generated from for.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete listener for a parse tree produced by forParser.
class forListener(ParseTreeListener):

    # Enter a parse tree produced by forParser#prog.
    def enterProg(self, ctx:forParser.ProgContext):
        pass

    # Exit a parse tree produced by forParser#prog.
    def exitProg(self, ctx:forParser.ProgContext):
        pass


    # Enter a parse tree produced by forParser#Assign.
    def enterAssign(self, ctx:forParser.AssignContext):
        pass

    # Exit a parse tree produced by forParser#Assign.
    def exitAssign(self, ctx:forParser.AssignContext):
        pass


    # Enter a parse tree produced by forParser#ForLoop.
    def enterForLoop(self, ctx:forParser.ForLoopContext):
        pass

    # Exit a parse tree produced by forParser#ForLoop.
    def exitForLoop(self, ctx:forParser.ForLoopContext):
        pass


    # Enter a parse tree produced by forParser#PrintExpr.
    def enterPrintExpr(self, ctx:forParser.PrintExprContext):
        pass

    # Exit a parse tree produced by forParser#PrintExpr.
    def exitPrintExpr(self, ctx:forParser.PrintExprContext):
        pass


    # Enter a parse tree produced by forParser#ForStatement.
    def enterForStatement(self, ctx:forParser.ForStatementContext):
        pass

    # Exit a parse tree produced by forParser#ForStatement.
    def exitForStatement(self, ctx:forParser.ForStatementContext):
        pass


    # Enter a parse tree produced by forParser#assignExpr.
    def enterAssignExpr(self, ctx:forParser.AssignExprContext):
        pass

    # Exit a parse tree produced by forParser#assignExpr.
    def exitAssignExpr(self, ctx:forParser.AssignExprContext):
        pass


    # Enter a parse tree produced by forParser#Block.
    def enterBlock(self, ctx:forParser.BlockContext):
        pass

    # Exit a parse tree produced by forParser#Block.
    def exitBlock(self, ctx:forParser.BlockContext):
        pass


    # Enter a parse tree produced by forParser#MulDiv.
    def enterMulDiv(self, ctx:forParser.MulDivContext):
        pass

    # Exit a parse tree produced by forParser#MulDiv.
    def exitMulDiv(self, ctx:forParser.MulDivContext):
        pass


    # Enter a parse tree produced by forParser#AddSub.
    def enterAddSub(self, ctx:forParser.AddSubContext):
        pass

    # Exit a parse tree produced by forParser#AddSub.
    def exitAddSub(self, ctx:forParser.AddSubContext):
        pass


    # Enter a parse tree produced by forParser#Comparison.
    def enterComparison(self, ctx:forParser.ComparisonContext):
        pass

    # Exit a parse tree produced by forParser#Comparison.
    def exitComparison(self, ctx:forParser.ComparisonContext):
        pass


    # Enter a parse tree produced by forParser#Parens.
    def enterParens(self, ctx:forParser.ParensContext):
        pass

    # Exit a parse tree produced by forParser#Parens.
    def exitParens(self, ctx:forParser.ParensContext):
        pass


    # Enter a parse tree produced by forParser#Num.
    def enterNum(self, ctx:forParser.NumContext):
        pass

    # Exit a parse tree produced by forParser#Num.
    def exitNum(self, ctx:forParser.NumContext):
        pass


    # Enter a parse tree produced by forParser#Id.
    def enterId(self, ctx:forParser.IdContext):
        pass

    # Exit a parse tree produced by forParser#Id.
    def exitId(self, ctx:forParser.IdContext):
        pass



del forParser