# Generated from for.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        3,2,28,8,2,1,2,1,2,3,2,32,8,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,61,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,72,8,5,10,5,12,5,75,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,3,1,0,
        7,8,1,0,9,10,1,0,12,17,82,0,13,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,
        6,40,1,0,0,0,8,44,1,0,0,0,10,60,1,0,0,0,12,14,3,2,1,0,13,12,1,0,
        0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,
        5,18,0,0,18,19,5,1,0,0,19,23,3,10,5,0,20,23,3,4,2,0,21,23,3,10,5,
        0,22,17,1,0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,
        11,0,0,25,27,5,2,0,0,26,28,3,6,3,0,27,26,1,0,0,0,27,28,1,0,0,0,28,
        29,1,0,0,0,29,31,5,3,0,0,30,32,3,10,5,0,31,30,1,0,0,0,31,32,1,0,
        0,0,32,33,1,0,0,0,33,35,5,3,0,0,34,36,3,6,3,0,35,34,1,0,0,0,35,36,
        1,0,0,0,36,37,1,0,0,0,37,38,5,4,0,0,38,39,3,8,4,0,39,5,1,0,0,0,40,
        41,5,18,0,0,41,42,5,1,0,0,42,43,3,10,5,0,43,7,1,0,0,0,44,48,5,5,
        0,0,45,47,3,2,1,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,6,0,0,52,9,1,0,0,0,53,
        54,6,5,-1,0,54,55,5,2,0,0,55,56,3,10,5,0,56,57,5,4,0,0,57,61,1,0,
        0,0,58,61,5,18,0,0,59,61,5,19,0,0,60,53,1,0,0,0,60,58,1,0,0,0,60,
        59,1,0,0,0,61,73,1,0,0,0,62,63,10,6,0,0,63,64,7,0,0,0,64,72,3,10,
        5,7,65,66,10,5,0,0,66,67,7,1,0,0,67,72,3,10,5,6,68,69,10,4,0,0,69,
        70,7,2,0,0,70,72,3,10,5,5,71,62,1,0,0,0,71,65,1,0,0,0,71,68,1,0,
        0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,11,1,0,0,0,75,73,
        1,0,0,0,9,15,22,27,31,35,48,60,71,73
    ]

class forParser ( Parser ):

    grammarFileName = "for.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "';'", "')'", "'{'", "'}'", 
                     "'*'", "'/'", "'+'", "'-'", "'for'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FOR", "OP_EQ", 
                      "OP_NE", "OP_LT", "OP_GT", "OP_LE", "OP_GE", "ID", 
                      "NUM", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_cicloFor = 2
    RULE_assignExpr = 3
    RULE_bloque = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "stat", "cicloFor", "assignExpr", "bloque", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    FOR=11
    OP_EQ=12
    OP_NE=13
    OP_LT=14
    OP_GT=15
    OP_LE=16
    OP_GE=17
    ID=18
    NUM=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.StatContext)
            else:
                return self.getTypedRuleContext(forParser.StatContext,i)


        def getRuleIndex(self):
            return forParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = forParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 788484) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForLoopContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cicloFor(self):
            return self.getTypedRuleContext(forParser.CicloForContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(forParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = forParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = forParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(forParser.ID)
                self.state = 18
                self.match(forParser.T__0)
                self.state = 19
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = forParser.ForLoopContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.cicloFor()
                pass

            elif la_ == 3:
                localctx = forParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_cicloFor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStatementContext(CicloForContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.CicloForContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(forParser.FOR, 0)
        def bloque(self):
            return self.getTypedRuleContext(forParser.BloqueContext,0)

        def assignExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.AssignExprContext)
            else:
                return self.getTypedRuleContext(forParser.AssignExprContext,i)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)



    def cicloFor(self):

        localctx = forParser.CicloForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cicloFor)
        self._la = 0 # Token type
        try:
            localctx = forParser.ForStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(forParser.FOR)
            self.state = 25
            self.match(forParser.T__1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 26
                self.assignExpr()


            self.state = 29
            self.match(forParser.T__2)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 786436) != 0):
                self.state = 30
                self.expr(0)


            self.state = 33
            self.match(forParser.T__2)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 34
                self.assignExpr()


            self.state = 37
            self.match(forParser.T__3)
            self.state = 38
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def getRuleIndex(self):
            return forParser.RULE_assignExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)




    def assignExpr(self):

        localctx = forParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(forParser.ID)
            self.state = 41
            self.match(forParser.T__0)
            self.state = 42
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_bloque

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlockContext(BloqueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.BloqueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.StatContext)
            else:
                return self.getTypedRuleContext(forParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)



    def bloque(self):

        localctx = forParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            localctx = forParser.BlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(forParser.T__4)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 788484) != 0):
                self.state = 45
                self.stat()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(forParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return forParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(forParser.ExprContext)
            else:
                return self.getTypedRuleContext(forParser.ExprContext,i)

        def OP_EQ(self):
            return self.getToken(forParser.OP_EQ, 0)
        def OP_NE(self):
            return self.getToken(forParser.OP_NE, 0)
        def OP_LT(self):
            return self.getToken(forParser.OP_LT, 0)
        def OP_GT(self):
            return self.getToken(forParser.OP_GT, 0)
        def OP_LE(self):
            return self.getToken(forParser.OP_LE, 0)
        def OP_GE(self):
            return self.getToken(forParser.OP_GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(forParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(forParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a forParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(forParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = forParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = forParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 54
                self.match(forParser.T__1)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(forParser.T__3)
                pass
            elif token in [18]:
                localctx = forParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(forParser.ID)
                pass
            elif token in [19]:
                localctx = forParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(forParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = forParser.MulDivContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = forParser.AddSubContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = forParser.ComparisonContext(self, forParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 69
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expr(5)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




