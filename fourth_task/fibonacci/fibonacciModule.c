#include <Python.h>

int C_Fibonacci(int n){

	int a = 0;
	int b = 1;
	int next = 0;
	
	for (int i = 1; i <=n; i++){
		next = a + b;
		a = b;
		b = next;
	}
	
	return a;
}

static PyObject* fibError;

static PyObject* fibonacci(PyObject* self, PyObject* args)
{
	int n;
	if(!PyArg_ParseTuple(args, "i", &n))
		return NULL;
			
	if(n<1) {
		PyErr_SetString(fibError, "Please enter a number greater than zero."); 
		return NULL;
	}
	
	return Py_BuildValue("i", C_Fibonacci(n));
}

static PyMethodDef fibonacciModuleMethods[]={
	{"fibonacci", (PyCFunction)fibonacci, METH_VARARGS, "Calculates Fibonacci numbers"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonaccimodule={
	PyModuleDef_HEAD_INIT,
	"fibonacciModule",
	"Fibonacci Module",
	-1,
	fibonacciModuleMethods
};

PyMODINIT_FUNC PyInit_fibModule(void)
{
	PyObject *mod =  PyModule_Create(&fibonaccimodule);
	fibError = PyErr_NewException("fibModule.error", NULL, NULL);
	Py_INCREF(fibError);
	PyModule_AddObject(mod, "error", fibError);
	return mod;
}