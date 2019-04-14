import sympy

def calculate(math_string,x):
 sinA=sympy.sin(30)
 print(sinA)
 result = sympy.evaluate(x + sinA + 4)
 print(sinA)
 result = (sympy.pi + sympy.exp(1)).evalf()
 print(result)
 x = 4
 print((x + sinA).evalf())

sympy.init_printing(use_unicode=False, wrap_line=False, no_global=True)
x = sympy.symbols('x')
a, b, c = sympy.symbols('a b c')
result = sympy.solve(a * x**2 + b * x +c , x)
sympy.pprint(result)  #latex expresion





#result=(sym.sinA+sum.x),evalf()