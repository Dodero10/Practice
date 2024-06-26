import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def activation_function(x, act_name):
    if not is_number(x):
        print("x must be a number")
        return
    if act_name not in ["sigmoid", "relu", "elu"]:
        print(f"{act_name} is not supported")
        return
    
    x = float(x)
    
    if act_name == "sigmoid":
        result = 1 / (1 + math.exp(-x))
    elif act_name == "relu":
        result = max(0, x)
    elif act_name == "elu":
        alpha = 0.01
        result = x if x > 0 else alpha * (math.exp(x) - 1)
    
    print(f"{act_name}: f({x}) = {result}")
