#Diogo Coraiola Guimarães

def compose_gf(g, f, x):
return g(f(x))

def compose_ff(f, x):
return f(f(x))

def compose_gg(g, x):
return g(g(x))

def compose_fg(f, g, x):
return f(g(x))

def f(x):
return x**2 + 1

def g(x):
return 2*x - 3

x = 4

result_gf = compose_gf(g, f, x)

result_ff = compose_ff(f, x)

result_gg = compose_gg(g, x)

result_fg = compose_fg(f, g, x)

equal_fg_gf = (result_fg == result_gf)

print("EXEMPLOS DO EXERCÍCIO 6")
print("(g ° f)({}) = {}".format(x, result_gf))
print("(f ° f)({}) = {}".format(x, result_ff))
print("(g ° g)({}) = {}".format(x, result_gg))
print("(f ° g)({}) = {}".format(x, result_fg))
print("(f ° g)({}) = (g ° f)({})? {}".format(x, x, equal_fg_gf))
print("="*40)
print("EXEMPLOS FORMULADOS:")

x1 = 4
result_gf1 = compose_gf(g, f, x1)

x2 = 3
result_ff2 = compose_ff(f, x2)

x3 = 2
result_gg3 = compose_gg(g, x3)

print("(g ° f)({}) = {}".format(x1, result_gf1))
print("(f ° f)({}) = {}".format(x2, result_ff2))
print("(g ° g)({}) = {}".format(x3, result_gg3))