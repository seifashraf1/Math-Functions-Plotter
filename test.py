from plotter import *
import pytest 

def gen(expr):
    y=[]
    x = var('x')
    list = np.linspace(-100,100 , 100)        
    for i in list:                      #substituting in the equation to get the y-values
        res = expr.subs(x, i)
        y.append(res)
    
    return y

def test_pow():
    f="x**3" 
    expr = sympify(f)
    assert MainWidget().plot_graph(f,-100,100)==gen(expr)

def test_log():
    f="ln(5*x)" 
    expr = sympify(f)
    assert MainWidget().plot_graph(f,-100,100)==gen(expr)

def test_sin():
    f="sin(x)" 
    expr = sympify(f)
    assert MainWidget().plot_graph(f,-100,100)==gen(expr)

def test_exp():
    f="e**(x)" 
    expr = sympify(f)
    assert MainWidget().plot_graph(f,-100,100)==gen(expr)

def test_func():
    f="e**(x)+x^5+sin(x+90)+1/(-x)" 
    expr = sympify(f)
    assert MainWidget().plot_graph(f,-100,100)==gen(expr)