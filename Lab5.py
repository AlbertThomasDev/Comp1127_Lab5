from tree import *
import operator

def stack():
    return ("stack",[])

def contents(stk):
    return stk[1]

def top(stk):
    if is_stack(stk):
        if stack_empty(stk):
            return "Stack is empty"
        else:
            return contents(stk)[0]
    else:
        return "Error"

def is_stack(stk):
    return type(stk) == type(()) and stk[0] == "stack"

def stack_empty(stk):
    if is_stack(stk):
        return contents(stk) == []
    else:
        return "Error"

def push(stk,el):
    if is_stack(stk):
        contents(stk).insert(0,el)
    else:
        return "Error"

def pop(stk):
    if is_stack(stk):
        if stack_empty(stk):
            return TypeError("Stack is empty")
        else:
            contents(stk).pop(0)
    else:
        return TypeError("Error")


def isOperator(optr):
    return optr in ["+","-","*","/","//","%","**"]

def applyOperator(string_operator,left_num,right_num):
    operator_mapping = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv,"//":operator.floordiv,"%":operator.mod,"**":operator.pow}
    if isOperator(string_operator):
        return operator_mapping[string_operator](left_num, right_num)

def eval_Postfix(tree):
    if is_btree(tree):
        tree_list = post_order(tree)
        tree_stack = stack()
        #print(tree_stack)
        for i in range(len(tree_list)):
            if isOperator(tree_list[i]):
                left = contents(tree_stack)[0]
                pop(tree_stack)
                right = contents(tree_stack)[0]
                pop(tree_stack)
                push(tree_stack,applyOperator(tree_list[i],right,left))
                #print(tree_stack)    
            else:
                push(tree_stack,tree_list[i])
                #print(tree_stack)
        return contents(tree_stack)[0]
    else:
        return "Error"
