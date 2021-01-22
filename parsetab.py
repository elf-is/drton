
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftTIMESDIVIDEleftWAAWnonassoc()nonassocSUPINFSUPEQUALSINFEQUALSEQUALSCOMP3AREF AKHIRAN AW DECREMENTATION DIFFERENT DIR DIVIDE DOUZ EQUALS EQUALSCOMP FLOAT ID ILA INCREMENTATION INF INFEQUALS INT JEREB KHATE2 KHREJ KMEL KTEB L3AKSS LKOLA MA7ED MASD9CH MINUS MOJOD NAW3 PLUS QRA RED S7I7 STRING SUP SUPEQUALS TELE3 TIMES WA WALO WLA\n    program : instruction_list\n    \n    incrementation : ID INCREMENTATION\n\n    \n    decrementation :  ID DECREMENTATION\n    \n    var_assign : ID EQUALS expression\n               | ID EQUALS input\n    \n    var_assign : MOJOD var_assign\n    \n    arrayelt_assign : arrayelt EQUALS expression\n    \n    if : ILA '(' condition ')' '{' instruction_list '}'\n        | ILA '(' condition ')' '{' instruction_list '}' WLA '{' instruction_list '}'\n\n    \n    for : LKOLA '(' var_assign  ';' condition ';' incrementation  ')' '{' instruction_list '}'\n        | LKOLA '(' var_assign  ';' condition ';' decrementation  ')' '{' instruction_list '}'\n        | LKOLA '(' expression ';' condition ';' incrementation  ')' '{' instruction_list '}'\n        | LKOLA '(' expression ';' condition ';' decrementation  ')' '{' instruction_list '}'\n    \n    while : MA7ED '(' condition ')' '{' instruction_list '}'\n\n    \n    doWhile :  DIR '{' instruction_list '}' MA7ED '(' condition ')'\n    \n    instruction : var_assign\n                | arrayelt_assign\n                | printing\n                | incrementation\n                | decrementation\n                | expression\n                | try\n                | if\n                | for\n                | KHREJ\n                | KMEL\n                | while\n                | doWhile\n                | input\n                | empty\n\n\n    \n        instruction_list : instruction\n                        |  instruction_list instruction\n    \n    condition : '(' condition ')' AW '(' condition ')'\n              | '(' condition ')' WA '(' condition ')'\n\n    \n    condition : condition WA '(' condition ')'\n              | condition AW '(' condition ')'\n\n    \n    condition : '(' condition ')' WA condition\n              | '(' condition ')' AW condition\n\n    \n    condition : L3AKSS '(' condition ')'\n    \n    condition : expression SUP expression\n              | expression INF expression\n              | expression EQUALSCOMP expression\n              | expression SUPEQUALS expression\n              | expression INFEQUALS expression\n              | expression DIFFERENT expression\n    \n    condition : expression\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | '(' expression ')'\n               | MINUS expression\n               | PLUS expression\n    \n    expression : ID\n    \n    input : QRA '(' expression ')'\n          | QRA '(' ')'\n    \n    try :  JEREB '{' instruction_list '}' MASD9CH '{' instruction_list '}'\n        |  JEREB '{' instruction_list '}' MASD9CH '{' instruction_list '}' AKHIRAN '{' instruction_list '}'\n    \n    expression : INT\n               | FLOAT\n               | STRING\n               | KHATE2\n               | S7I7\n               | WALO\n               | array\n               | arrayelt\n    \n    arraylist :  expression\n    \n    arraylist : arraylist ',' expression\n    \n    array : '[' arraylist ']'\n    \n    array : '[' ']'\n    \n    arrayelt : ID dimensions\n    \n    dimensions : '[' expression ']'\n    \n    dimensions : dimensions '[' expression ']'\n    \n    printing : KTEB '(' condition ')'\n            | KTEB '(' incrementation ')'\n            | KTEB '(' decrementation ')'\n    \n    empty :\n    "
    
_lr_action_items = {'KHREJ':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[13,13,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,13,13,-70,-47,-48,-49,-50,-4,-5,-7,-51,13,13,-56,-69,-72,-74,-75,-76,-55,-73,13,13,13,13,13,13,-8,-14,-57,-15,13,13,13,13,13,13,13,13,13,13,13,13,-9,-10,-11,-12,-13,-58,]),'KMEL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[14,14,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,14,14,-70,-47,-48,-49,-50,-4,-5,-7,-51,14,14,-56,-69,-72,-74,-75,-76,-55,-73,14,14,14,14,14,14,-8,-14,-57,-15,14,14,14,14,14,14,14,14,14,14,14,14,-9,-10,-11,-12,-13,-58,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,144,145,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[19,19,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,51,-66,55,55,55,-59,-60,-61,-62,-63,-64,-65,55,-32,55,55,55,55,55,-2,-3,-71,55,-6,55,83,-54,-66,-53,-52,19,55,89,55,19,55,-70,-47,-48,-49,-50,-4,-5,55,-7,55,-51,19,19,-56,-69,55,-72,-74,-75,-76,55,55,55,55,55,55,55,55,55,-55,-73,55,55,19,19,55,55,19,19,158,158,19,55,55,55,19,-8,-14,-57,-15,19,19,19,19,19,19,19,19,19,19,19,19,-9,-10,-11,-12,-13,-58,]),'MOJOD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,61,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[20,20,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,20,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,20,20,20,-70,-47,-48,-49,-50,-4,-5,-7,-51,20,20,-56,-69,-72,-74,-75,-76,-55,-73,20,20,20,20,20,20,-8,-14,-57,-15,20,20,20,20,20,20,20,20,20,20,20,20,-9,-10,-11,-12,-13,-58,]),'KTEB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[22,22,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,22,22,-70,-47,-48,-49,-50,-4,-5,-7,-51,22,22,-56,-69,-72,-74,-75,-76,-55,-73,22,22,22,22,22,22,-8,-14,-57,-15,22,22,22,22,22,22,22,22,22,22,22,22,-9,-10,-11,-12,-13,-58,]),'(':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,81,84,85,91,93,94,95,97,100,101,102,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,136,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[23,23,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,53,23,23,23,-59,-60,-61,-62,-63,-64,-65,60,61,62,64,23,-32,23,23,23,23,23,-2,-3,-71,23,-6,23,77,-54,-66,-53,-52,23,77,23,77,23,23,-70,-47,-48,-49,-50,-4,-5,23,-7,77,105,-51,23,23,-56,-69,23,-72,-74,122,123,-75,-76,77,23,23,23,23,23,23,77,77,-55,-73,77,77,23,23,147,148,150,23,23,23,77,77,77,23,-8,-14,-57,-15,23,23,23,23,23,23,23,23,23,23,23,23,-9,-10,-11,-12,-13,-58,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,82,83,84,85,88,89,91,92,93,94,95,96,97,99,100,103,104,105,106,107,108,109,110,111,114,115,118,119,120,122,123,125,126,127,128,129,130,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[25,25,-31,-16,-17,-18,-19,-20,42,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,25,25,25,-59,-60,-61,-62,-63,-64,-65,25,-32,25,25,25,25,25,-2,-3,-71,25,-6,25,25,42,-54,-66,-53,-52,25,25,25,25,25,25,-70,42,-47,-48,-49,-50,42,-5,25,42,42,25,42,-54,-51,25,42,-54,25,42,-56,-69,25,42,-72,42,-74,-75,-76,25,25,25,25,25,25,25,25,25,-55,42,-73,25,25,42,42,42,42,42,42,25,25,25,25,25,25,25,25,25,25,25,-8,-14,-57,-15,25,25,25,25,25,25,25,25,25,25,25,25,-9,-10,-11,-12,-13,-58,]),'PLUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,82,83,84,85,88,89,91,92,93,94,95,96,97,99,100,103,104,105,106,107,108,109,110,111,114,115,118,119,120,122,123,125,126,127,128,129,130,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[24,24,-31,-16,-17,-18,-19,-20,41,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,24,24,24,-59,-60,-61,-62,-63,-64,-65,24,-32,24,24,24,24,24,-2,-3,-71,24,-6,24,24,41,-54,-66,-53,-52,24,24,24,24,24,24,-70,41,-47,-48,-49,-50,41,-5,24,41,41,24,41,-54,-51,24,41,-54,24,41,-56,-69,24,41,-72,41,-74,-75,-76,24,24,24,24,24,24,24,24,24,-55,41,-73,24,24,41,41,41,41,41,41,24,24,24,24,24,24,24,24,24,24,24,-8,-14,-57,-15,24,24,24,24,24,24,24,24,24,24,24,24,-9,-10,-11,-12,-13,-58,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[26,26,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,26,26,26,-59,-60,-61,-62,-63,-64,-65,26,-32,26,26,26,26,26,-2,-3,-71,26,-6,26,26,-54,-66,-53,-52,26,26,26,26,26,26,-70,-47,-48,-49,-50,-4,-5,26,-7,26,-51,26,26,-56,-69,26,-72,-74,-75,-76,26,26,26,26,26,26,26,26,26,-55,-73,26,26,26,26,26,26,26,26,26,26,26,26,26,-8,-14,-57,-15,26,26,26,26,26,26,26,26,26,26,26,26,-9,-10,-11,-12,-13,-58,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[27,27,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,27,27,27,-59,-60,-61,-62,-63,-64,-65,27,-32,27,27,27,27,27,-2,-3,-71,27,-6,27,27,-54,-66,-53,-52,27,27,27,27,27,27,-70,-47,-48,-49,-50,-4,-5,27,-7,27,-51,27,27,-56,-69,27,-72,-74,-75,-76,27,27,27,27,27,27,27,27,27,-55,-73,27,27,27,27,27,27,27,27,27,27,27,27,27,-8,-14,-57,-15,27,27,27,27,27,27,27,27,27,27,27,27,-9,-10,-11,-12,-13,-58,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[28,28,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,28,28,28,-59,-60,-61,-62,-63,-64,-65,28,-32,28,28,28,28,28,-2,-3,-71,28,-6,28,28,-54,-66,-53,-52,28,28,28,28,28,28,-70,-47,-48,-49,-50,-4,-5,28,-7,28,-51,28,28,-56,-69,28,-72,-74,-75,-76,28,28,28,28,28,28,28,28,28,-55,-73,28,28,28,28,28,28,28,28,28,28,28,28,28,-8,-14,-57,-15,28,28,28,28,28,28,28,28,28,28,28,28,-9,-10,-11,-12,-13,-58,]),'KHATE2':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[29,29,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,29,29,29,-59,-60,-61,-62,-63,-64,-65,29,-32,29,29,29,29,29,-2,-3,-71,29,-6,29,29,-54,-66,-53,-52,29,29,29,29,29,29,-70,-47,-48,-49,-50,-4,-5,29,-7,29,-51,29,29,-56,-69,29,-72,-74,-75,-76,29,29,29,29,29,29,29,29,29,-55,-73,29,29,29,29,29,29,29,29,29,29,29,29,29,-8,-14,-57,-15,29,29,29,29,29,29,29,29,29,29,29,29,-9,-10,-11,-12,-13,-58,]),'S7I7':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[30,30,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,30,30,30,-59,-60,-61,-62,-63,-64,-65,30,-32,30,30,30,30,30,-2,-3,-71,30,-6,30,30,-54,-66,-53,-52,30,30,30,30,30,30,-70,-47,-48,-49,-50,-4,-5,30,-7,30,-51,30,30,-56,-69,30,-72,-74,-75,-76,30,30,30,30,30,30,30,30,30,-55,-73,30,30,30,30,30,30,30,30,30,30,30,30,30,-8,-14,-57,-15,30,30,30,30,30,30,30,30,30,30,30,30,-9,-10,-11,-12,-13,-58,]),'WALO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,84,85,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[31,31,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,31,31,31,-59,-60,-61,-62,-63,-64,-65,31,-32,31,31,31,31,31,-2,-3,-71,31,-6,31,31,-54,-66,-53,-52,31,31,31,31,31,31,-70,-47,-48,-49,-50,-4,-5,31,-7,31,-51,31,31,-56,-69,31,-72,-74,-75,-76,31,31,31,31,31,31,31,31,31,-55,-73,31,31,31,31,31,31,31,31,31,31,31,31,31,-8,-14,-57,-15,31,31,31,31,31,31,31,31,31,31,31,31,-9,-10,-11,-12,-13,-58,]),'JEREB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[33,33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,33,33,-70,-47,-48,-49,-50,-4,-5,-7,-51,33,33,-56,-69,-72,-74,-75,-76,-55,-73,33,33,33,33,33,33,-8,-14,-57,-15,33,33,33,33,33,33,33,33,33,33,33,33,-9,-10,-11,-12,-13,-58,]),'ILA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[34,34,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,34,34,-70,-47,-48,-49,-50,-4,-5,-7,-51,34,34,-56,-69,-72,-74,-75,-76,-55,-73,34,34,34,34,34,34,-8,-14,-57,-15,34,34,34,34,34,34,34,34,34,34,34,34,-9,-10,-11,-12,-13,-58,]),'LKOLA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[35,35,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,35,35,-70,-47,-48,-49,-50,-4,-5,-7,-51,35,35,-56,-69,-72,-74,-75,-76,-55,-73,35,35,35,35,35,35,-8,-14,-57,-15,35,35,35,35,35,35,35,35,35,35,35,35,-9,-10,-11,-12,-13,-58,]),'MA7ED':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,117,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[36,36,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,36,36,-70,-47,-48,-49,-50,-4,-5,-7,-51,36,36,-56,-69,-72,-74,-75,-76,136,-55,-73,36,36,36,36,36,36,-8,-14,-57,-15,36,36,36,36,36,36,36,36,36,36,36,36,-9,-10,-11,-12,-13,-58,]),'DIR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[37,37,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,37,37,-70,-47,-48,-49,-50,-4,-5,-7,-51,37,37,-56,-69,-72,-74,-75,-76,-55,-73,37,37,37,37,37,37,-8,-14,-57,-15,37,37,37,37,37,37,37,37,37,37,37,37,-9,-10,-11,-12,-13,-58,]),'QRA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,45,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[38,38,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,38,-2,-3,-71,-6,-54,-66,-53,-52,38,38,-70,-47,-48,-49,-50,-4,-5,-7,-51,38,38,-56,-69,-72,-74,-75,-76,-55,-73,38,38,38,38,38,38,-8,-14,-57,-15,38,38,38,38,38,38,38,38,38,38,38,38,-9,-10,-11,-12,-13,-58,]),'[':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,47,48,49,50,52,53,55,56,57,58,59,60,61,62,63,64,66,68,69,70,71,72,73,74,76,77,83,84,85,89,91,93,94,95,97,100,103,104,105,106,107,108,109,110,111,114,115,118,120,122,123,132,135,137,138,142,143,146,147,148,150,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[39,39,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,49,-66,39,39,39,-59,-60,-61,-62,-63,-64,-65,39,-32,39,39,39,39,39,-2,-3,74,39,-6,39,39,49,-66,-53,-52,39,39,39,39,39,39,-70,-47,-48,-49,-50,-4,-5,39,-7,39,49,-51,39,49,39,-56,-69,39,-72,-74,-75,-76,39,39,39,39,39,39,39,39,39,-55,-73,39,39,39,39,39,39,39,39,39,39,39,39,39,-8,-14,-57,-15,39,39,39,39,39,39,39,39,39,39,39,39,-9,-10,-11,-12,-13,-58,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,66,68,69,70,71,72,73,76,84,93,94,97,100,103,104,118,120,155,161,165,171,187,188,189,190,191,192,],[-77,0,-1,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,-70,-47,-48,-49,-50,-4,-5,-7,-51,-56,-69,-72,-74,-75,-76,-55,-73,-8,-14,-57,-15,-9,-10,-11,-12,-13,-58,]),'}':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,26,27,28,29,30,31,32,40,46,47,48,50,55,56,57,58,59,63,66,68,69,70,71,72,73,76,84,85,91,93,94,97,100,103,104,118,120,132,135,142,143,146,154,155,161,165,171,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,],[-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-54,-66,-59,-60,-61,-62,-63,-64,-65,-32,-2,-3,-71,-6,-54,-66,-53,-52,-77,-77,-70,-47,-48,-49,-50,-4,-5,-7,-51,112,117,-56,-69,-72,-74,-75,-76,-55,-73,-77,-77,-77,155,161,165,-8,-14,-57,-15,-77,-77,-77,-77,-77,-77,187,188,189,190,191,192,-9,-10,-11,-12,-13,-58,]),'TIMES':([9,19,21,26,27,28,29,30,31,32,48,54,55,56,57,58,66,67,68,69,70,71,72,75,76,82,83,84,88,89,92,94,96,97,99,119,120,125,126,127,128,129,130,],[43,-54,-66,-59,-60,-61,-62,-63,-64,-65,-71,43,-54,-66,43,43,-70,43,43,43,-49,-50,43,43,43,43,-54,-51,43,-54,43,-69,43,-72,43,43,-73,43,43,43,43,43,43,]),'DIVIDE':([9,19,21,26,27,28,29,30,31,32,48,54,55,56,57,58,66,67,68,69,70,71,72,75,76,82,83,84,88,89,92,94,96,97,99,119,120,125,126,127,128,129,130,],[44,-54,-66,-59,-60,-61,-62,-63,-64,-65,-71,44,-54,-66,44,44,-70,44,44,44,-49,-50,44,44,44,44,-54,-51,44,-54,44,-69,44,-72,44,44,-73,44,44,44,44,44,44,]),'EQUALS':([19,21,48,51,89,97,120,],[45,52,-71,45,45,-72,-73,]),'INCREMENTATION':([19,83,158,],[46,46,46,]),'DECREMENTATION':([19,83,158,],[47,47,47,]),')':([26,27,28,29,30,31,32,46,47,48,54,55,56,57,58,64,66,68,69,70,71,78,79,80,82,83,84,86,90,92,94,97,98,99,120,124,125,126,127,128,129,130,139,140,141,149,151,152,153,156,157,159,160,162,163,164,172,173,],[-59,-60,-61,-62,-63,-64,-65,-2,-3,-71,84,-54,-66,-53,-52,93,-70,-47,-48,-49,-50,100,103,104,-46,-54,-51,113,116,118,-69,-72,121,84,-73,141,-40,-41,-42,-43,-44,-45,152,153,-39,-38,-37,-35,-36,167,168,169,170,171,172,173,-33,-34,]),']':([26,27,28,29,30,31,32,39,48,55,56,57,58,65,66,67,68,69,70,71,75,84,94,96,97,119,120,],[-59,-60,-61,-62,-63,-64,-65,66,-71,-54,-66,-53,-52,94,-70,-67,-47,-48,-49,-50,97,-51,-69,120,-72,-68,-73,]),',':([26,27,28,29,30,31,32,48,55,56,57,58,65,66,67,68,69,70,71,84,94,97,119,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,95,-70,-67,-47,-48,-49,-50,-51,-69,-72,-68,-73,]),';':([26,27,28,29,30,31,32,48,50,55,56,57,58,66,68,69,70,71,72,73,82,84,87,88,89,93,94,97,118,120,125,126,127,128,129,130,133,134,141,149,151,152,153,172,173,],[-59,-60,-61,-62,-63,-64,-65,-71,-6,-54,-66,-53,-52,-70,-47,-48,-49,-50,-4,-5,-46,-51,114,115,-54,-56,-69,-72,-55,-73,-40,-41,-42,-43,-44,-45,144,145,-39,-38,-37,-35,-36,-33,-34,]),'SUP':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,106,-54,-51,-69,-72,106,-73,]),'INF':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,107,-54,-51,-69,-72,107,-73,]),'EQUALSCOMP':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,108,-54,-51,-69,-72,108,-73,]),'SUPEQUALS':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,109,-54,-51,-69,-72,109,-73,]),'INFEQUALS':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,110,-54,-51,-69,-72,110,-73,]),'DIFFERENT':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,82,83,84,94,97,99,120,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,111,-54,-51,-69,-72,111,-73,]),'WA':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,78,82,83,84,86,90,94,97,98,99,120,121,124,125,126,127,128,129,130,133,134,139,140,141,149,151,152,153,162,163,164,172,173,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,101,-46,-54,-51,101,101,-69,-72,101,-46,-73,138,101,-40,-41,-42,-43,-44,-45,101,101,101,101,-39,-38,-37,-35,-36,101,101,101,-33,-34,]),'AW':([26,27,28,29,30,31,32,48,55,56,57,58,66,68,69,70,71,78,82,83,84,86,90,94,97,98,99,120,121,124,125,126,127,128,129,130,133,134,139,140,141,149,151,152,153,162,163,164,172,173,],[-59,-60,-61,-62,-63,-64,-65,-71,-54,-66,-53,-52,-70,-47,-48,-49,-50,102,-46,-54,-51,102,102,-69,-72,102,-46,-73,137,102,-40,-41,-42,-43,-44,-45,102,102,102,102,-39,-38,-37,-35,-36,102,102,102,-33,-34,]),'{':([33,37,113,116,131,166,167,168,169,170,174,],[59,63,132,135,142,175,176,177,178,179,180,]),'L3AKSS':([53,60,62,77,105,114,115,122,123,137,138,147,148,150,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'MASD9CH':([112,],[131,]),'WLA':([155,],[166,]),'AKHIRAN':([165,],[174,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instruction_list':([0,59,63,132,135,142,175,176,177,178,179,180,],[2,85,91,143,146,154,181,182,183,184,185,186,]),'instruction':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[3,40,3,3,40,40,3,3,3,40,40,40,3,3,3,3,3,3,40,40,40,40,40,40,]),'var_assign':([0,2,20,59,61,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[4,4,50,4,87,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'arrayelt_assign':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'printing':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'incrementation':([0,2,53,59,63,85,91,132,135,142,143,144,145,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[7,7,79,7,7,7,7,7,7,7,7,156,159,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'decrementation':([0,2,53,59,63,85,91,132,135,142,143,144,145,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[8,8,80,8,8,8,8,8,8,8,8,157,160,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'expression':([0,2,23,24,25,39,41,42,43,44,45,49,52,53,59,60,61,62,63,64,74,77,85,91,95,105,106,107,108,109,110,111,114,115,122,123,132,135,137,138,142,143,146,147,148,150,154,175,176,177,178,179,180,181,182,183,184,185,186,],[9,9,54,57,58,67,68,69,70,71,72,75,76,82,9,82,88,82,9,92,96,99,9,9,119,82,125,126,127,128,129,130,82,82,82,82,9,9,82,82,9,9,9,82,99,99,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'try':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'if':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'for':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'while':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'doWhile':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'input':([0,2,45,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[17,17,73,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'empty':([0,2,59,63,85,91,132,135,142,143,146,154,175,176,177,178,179,180,181,182,183,184,185,186,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'arrayelt':([0,2,23,24,25,39,41,42,43,44,45,49,52,53,59,60,61,62,63,64,74,77,85,91,95,105,106,107,108,109,110,111,114,115,122,123,132,135,137,138,142,143,146,147,148,150,154,175,176,177,178,179,180,181,182,183,184,185,186,],[21,21,56,56,56,56,56,56,56,56,56,56,56,56,21,56,56,56,21,56,56,56,21,21,56,56,56,56,56,56,56,56,56,56,56,56,21,21,56,56,21,21,21,56,56,56,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'array':([0,2,23,24,25,39,41,42,43,44,45,49,52,53,59,60,61,62,63,64,74,77,85,91,95,105,106,107,108,109,110,111,114,115,122,123,132,135,137,138,142,143,146,147,148,150,154,175,176,177,178,179,180,181,182,183,184,185,186,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'dimensions':([19,55,83,89,],[48,48,48,48,]),'arraylist':([39,],[65,]),'condition':([53,60,62,77,105,114,115,122,123,137,138,147,148,150,],[78,86,90,98,124,133,134,139,140,149,151,162,163,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instruction_list','program',1,'p_program','darija_compiler.py',203),
  ('incrementation -> ID INCREMENTATION','incrementation',2,'p_incrementation','darija_compiler.py',211),
  ('decrementation -> ID DECREMENTATION','decrementation',2,'p_decrementation','darija_compiler.py',219),
  ('var_assign -> ID EQUALS expression','var_assign',3,'p_var_assign','darija_compiler.py',226),
  ('var_assign -> ID EQUALS input','var_assign',3,'p_var_assign','darija_compiler.py',227),
  ('var_assign -> MOJOD var_assign','var_assign',2,'p_var_assign_global','darija_compiler.py',234),
  ('arrayelt_assign -> arrayelt EQUALS expression','arrayelt_assign',3,'p_arrayelt_assign','darija_compiler.py',241),
  ('if -> ILA ( condition ) { instruction_list }','if',7,'p_if','darija_compiler.py',248),
  ('if -> ILA ( condition ) { instruction_list } WLA { instruction_list }','if',11,'p_if','darija_compiler.py',249),
  ('for -> LKOLA ( var_assign ; condition ; incrementation ) { instruction_list }','for',11,'p_for','darija_compiler.py',260),
  ('for -> LKOLA ( var_assign ; condition ; decrementation ) { instruction_list }','for',11,'p_for','darija_compiler.py',261),
  ('for -> LKOLA ( expression ; condition ; incrementation ) { instruction_list }','for',11,'p_for','darija_compiler.py',262),
  ('for -> LKOLA ( expression ; condition ; decrementation ) { instruction_list }','for',11,'p_for','darija_compiler.py',263),
  ('while -> MA7ED ( condition ) { instruction_list }','while',7,'p_while','darija_compiler.py',270),
  ('doWhile -> DIR { instruction_list } MA7ED ( condition )','doWhile',8,'p_doWhile','darija_compiler.py',278),
  ('instruction -> var_assign','instruction',1,'p_instruction','darija_compiler.py',285),
  ('instruction -> arrayelt_assign','instruction',1,'p_instruction','darija_compiler.py',286),
  ('instruction -> printing','instruction',1,'p_instruction','darija_compiler.py',287),
  ('instruction -> incrementation','instruction',1,'p_instruction','darija_compiler.py',288),
  ('instruction -> decrementation','instruction',1,'p_instruction','darija_compiler.py',289),
  ('instruction -> expression','instruction',1,'p_instruction','darija_compiler.py',290),
  ('instruction -> try','instruction',1,'p_instruction','darija_compiler.py',291),
  ('instruction -> if','instruction',1,'p_instruction','darija_compiler.py',292),
  ('instruction -> for','instruction',1,'p_instruction','darija_compiler.py',293),
  ('instruction -> KHREJ','instruction',1,'p_instruction','darija_compiler.py',294),
  ('instruction -> KMEL','instruction',1,'p_instruction','darija_compiler.py',295),
  ('instruction -> while','instruction',1,'p_instruction','darija_compiler.py',296),
  ('instruction -> doWhile','instruction',1,'p_instruction','darija_compiler.py',297),
  ('instruction -> input','instruction',1,'p_instruction','darija_compiler.py',298),
  ('instruction -> empty','instruction',1,'p_instruction','darija_compiler.py',299),
  ('instruction_list -> instruction','instruction_list',1,'p_instruction_list','darija_compiler.py',308),
  ('instruction_list -> instruction_list instruction','instruction_list',2,'p_instruction_list','darija_compiler.py',309),
  ('condition -> ( condition ) AW ( condition )','condition',7,'p_condition_big','darija_compiler.py',328),
  ('condition -> ( condition ) WA ( condition )','condition',7,'p_condition_big','darija_compiler.py',329),
  ('condition -> condition WA ( condition )','condition',5,'p_condition_medium1','darija_compiler.py',337),
  ('condition -> condition AW ( condition )','condition',5,'p_condition_medium1','darija_compiler.py',338),
  ('condition -> ( condition ) WA condition','condition',5,'p_condition_medium2','darija_compiler.py',346),
  ('condition -> ( condition ) AW condition','condition',5,'p_condition_medium2','darija_compiler.py',347),
  ('condition -> L3AKSS ( condition )','condition',4,'p_condition','darija_compiler.py',364),
  ('condition -> expression SUP expression','condition',3,'p_condition_comp','darija_compiler.py',371),
  ('condition -> expression INF expression','condition',3,'p_condition_comp','darija_compiler.py',372),
  ('condition -> expression EQUALSCOMP expression','condition',3,'p_condition_comp','darija_compiler.py',373),
  ('condition -> expression SUPEQUALS expression','condition',3,'p_condition_comp','darija_compiler.py',374),
  ('condition -> expression INFEQUALS expression','condition',3,'p_condition_comp','darija_compiler.py',375),
  ('condition -> expression DIFFERENT expression','condition',3,'p_condition_comp','darija_compiler.py',376),
  ('condition -> expression','condition',1,'p_condition_exp','darija_compiler.py',383),
  ('expression -> expression PLUS expression','expression',3,'p_expression','darija_compiler.py',390),
  ('expression -> expression MINUS expression','expression',3,'p_expression','darija_compiler.py',391),
  ('expression -> expression TIMES expression','expression',3,'p_expression','darija_compiler.py',392),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','darija_compiler.py',393),
  ('expression -> ( expression )','expression',3,'p_expression','darija_compiler.py',394),
  ('expression -> MINUS expression','expression',2,'p_expression','darija_compiler.py',395),
  ('expression -> PLUS expression','expression',2,'p_expression','darija_compiler.py',396),
  ('expression -> ID','expression',1,'p_expression_id','darija_compiler.py',410),
  ('input -> QRA ( expression )','input',4,'p_input','darija_compiler.py',417),
  ('input -> QRA ( )','input',3,'p_input','darija_compiler.py',418),
  ('try -> JEREB { instruction_list } MASD9CH { instruction_list }','try',8,'p_try','darija_compiler.py',425),
  ('try -> JEREB { instruction_list } MASD9CH { instruction_list } AKHIRAN { instruction_list }','try',12,'p_try','darija_compiler.py',426),
  ('expression -> INT','expression',1,'p_expression_terminals','darija_compiler.py',436),
  ('expression -> FLOAT','expression',1,'p_expression_terminals','darija_compiler.py',437),
  ('expression -> STRING','expression',1,'p_expression_terminals','darija_compiler.py',438),
  ('expression -> KHATE2','expression',1,'p_expression_terminals','darija_compiler.py',439),
  ('expression -> S7I7','expression',1,'p_expression_terminals','darija_compiler.py',440),
  ('expression -> WALO','expression',1,'p_expression_terminals','darija_compiler.py',441),
  ('expression -> array','expression',1,'p_expression_terminals','darija_compiler.py',442),
  ('expression -> arrayelt','expression',1,'p_expression_terminals','darija_compiler.py',443),
  ('arraylist -> expression','arraylist',1,'p_arraylist_1','darija_compiler.py',451),
  ('arraylist -> arraylist , expression','arraylist',3,'p_arraylist_2','darija_compiler.py',458),
  ('array -> [ arraylist ]','array',3,'p_array','darija_compiler.py',466),
  ('array -> [ ]','array',2,'p_array_empty','darija_compiler.py',473),
  ('arrayelt -> ID dimensions','arrayelt',2,'p_arrayelt','darija_compiler.py',480),
  ('dimensions -> [ expression ]','dimensions',3,'p_dimensions','darija_compiler.py',487),
  ('dimensions -> dimensions [ expression ]','dimensions',4,'p_demensions','darija_compiler.py',494),
  ('printing -> KTEB ( condition )','printing',4,'p_printing','darija_compiler.py',506),
  ('printing -> KTEB ( incrementation )','printing',4,'p_printing','darija_compiler.py',507),
  ('printing -> KTEB ( decrementation )','printing',4,'p_printing','darija_compiler.py',508),
  ('empty -> <empty>','empty',0,'p_empty','darija_compiler.py',515),
]
