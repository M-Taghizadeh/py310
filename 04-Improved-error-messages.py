# Better error messages
# 1: SyntaxError
# 2: IndentationError
# 3: AttributeErrors


# 1: SyntaxError: '{' was never closed or '(' was never closed
# ------------------------------------------------------------------------
# expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
# some_other_code = foo()
# ------------------------------------------------------------------------
# print("hello world!" 
# print("hello world!")
# ------------------------------------------------------------------------
# try:
#     x = 2
# something = 3
# ------------------------------------------------------------------------
# number = "mohammad"
# if name = "mohammad":
#     pass    
# ------------------------------------------------------------------------


# 2: IndentationError
# def task():
#     if True:
#     x = 2
# ------------------------------------------------------------------------


# 3: AttributeErrors => give suggestions 
# product = "car"
# print(produc) # NameError: name 'produc' is not defined. Did you mean: 'product'?
# ------------------------------------------------------------------------
