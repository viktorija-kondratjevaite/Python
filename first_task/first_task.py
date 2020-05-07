import numpy as np
from sympy import *
from numpy.linalg import inv

# Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
def f1():
    interval = np.linspace(-1.3, 2.5, num=64 + 1)
    intervals = np.array([interval[:-1], interval[1:]])  # nuima paskutini ir pirma simboli, gaunam 2d array
    intervals = intervals.transpose()  # pirmo masyvo pirmas su antro mas pirmu, ir t.t.
    print(intervals)


# Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
def f2(n):
    arr = np.array([1, 2, 3])
    result = np.tile(arr, 3 * n)
    print(result)


# Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
def f3():
    arr = np.arange(1, 21, 2)
	#arr = np.arange(10 * 2)[1::2]
    print(arr)


# Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
def f4():
    arr = np.zeros((10, 10), dtype=np.int)
	#1 var.
    np.pad(arr, ((1, 1), (1, 1)), 'constant', constant_values=((1, 1), (1,1)))
	#2 var.
    #arr = np.insert(arr, 0, values=1, axis=1)
    #arr = np.insert(arr, 11, values=1, axis=1)
    #arr = np.insert(arr, 0, values=1, axis=0)
    #arr = np.insert(arr, 11, values=1, axis=0)
    print(arr)


# Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
def f5():
    arr = np.zeros((8, 8), dtype=np.int)
    arr[::2, 1::2] = 1  # start and stop - slicing, step - striding
    arr[1::2, ::2] = 1
    print(arr)

# Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
def f6(n):
	np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)


# Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
def f7():
    arr = np.random.rand(3, 5)
    print("Masyvas: {}".format(arr))
    print("Suma:\n{}".format(np.sum(arr)))
    print("Eilučių suma:\n{}".format(np.sum(arr, 1)))
    print("Stulepelių suma:\n{}".format(np.sum(arr, 0)))


# Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį.
# Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
def f8():
    arr = np.random.rand(5, 5)
    print("Masyvas:\n{}".format(arr))
    arr[arr[:, 1].argsort()]
    print("Surūšiuotas:\n{}".format(arr))


# Atvirkštinę matricą 
def f9():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Matrica:\n{}".format(np.matrix(arr)))
    print("Atvirkštinė matrica:\n{}".format(inv(np.matrix(a))))


# Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
def f10():
    arr = np.array([[3, 2], [1, 0]])
    print("Matrica:\n{}".format(arr))
    eigenvalue, eigenvector = np.linalg.eig(arr)
    print("Tikrinės vertės:\n{}".format(eigenvalue))
    print("Tikrinis vektorius:\n{}".format(eigenvector))


# Pasirinktos funkcijos išvestinę
def f11():
    x = symbols('x')
    init_printing(use_unicode=True)
    exp = cos(x)
    derivative = diff(exp, x)
    # derivative = diff(3*x**2+1,x)
    print("Funkcija:\n{}".format(exp))
    print("Funkcijos išvestinė:\n{}".format(derivative))


# Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
def f12():
    x = symbols('x')
    exp = x**2+x+1
    defIntegral = integrate(exp, (x, 1, 3))
    indefIntegral = integrate(exp, x)
    print("Funkcija:\n{}".format(exp))
    print("Apibrėžtinis integralas:\n{}".format(defIntegral))
    print("Neapibrėžtinis integralas:\n{}".format(indefIntegral))

