grammar for;

// Parser rules
prog: stat+ ;

stat
    : ID '=' expr                             # Assign
    | cicloFor                                # ForLoop
    | expr                                    # PrintExpr
    ;

cicloFor
    : FOR '(' assignExpr? ';' expr? ';' assignExpr? ')' bloque  # ForStatement
    ;

assignExpr
    : ID '=' expr
    ;

bloque
    : '{' stat* '}'                           # Block
    ;

expr
    : expr ('*' | '/') expr                   # MulDiv
    | expr ('+' | '-') expr                   # AddSub
    | expr (OP_EQ | OP_NE | OP_LT | OP_GT | OP_LE | OP_GE) expr  # Comparison
    | '(' expr ')'                            # Parens
    | ID                                      # Id
    | NUM                                     # Num
    ;

// Lexer rules
FOR: 'for';

OP_EQ: '==';
OP_NE: '!=';
OP_LT: '<';
OP_GT: '>';
OP_LE: '<=';
OP_GE: '>=';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;
