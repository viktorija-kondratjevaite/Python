#include <Python.h>
#include "structmember.h"
#include <stdio.h>

typedef struct{
  PyObject_HEAD
  float a;
  float b;
  float c;
} Triangle;

static PyObject* triangleError;

static void Triangle_dealloc(Triangle* self){
	Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject * Triangle_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Triangle *self;

    self = (Triangle *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->a = 1;
        self->b = 1;
		self->c = 1;
    }

    return (PyObject *)self;
}

static int Triangle_init(Triangle *self, PyObject *args, PyObject *kwds)
{
	float tempA, tempB, tempC;
	if (!PyArg_ParseTuple(args, "fff", &tempA, &tempB, &tempC))
        return -1;
	
	if(tempA <= 0 || tempB <= 0 || tempC <= 0 || tempA + tempB <= tempC || tempA + tempC <= tempB || tempB + tempC <= tempA){
		PyErr_SetString(triangleError, "Cannot form triangle from given sides...");
		return -1;
	}

	self->a=tempA;
	self->b=tempB;
	self->c=tempC;
	
    return 0;
}

//***********************************************************************************************************

static PyObject * Triangle_perimeter(Triangle* self)
{
	char str[20];
	sprintf(str, "%.3f", self->a+self->b+self->c);
	return Py_BuildValue("s", str);
}

static PyObject * Triangle_area(Triangle* self)
{
	float semiPerimeter = (self->a+self->b+self->c)/2;
	char str[20];
	sprintf(str, "%.3f", sqrt(semiPerimeter*(semiPerimeter-self->a)*(semiPerimeter-self->b)*(semiPerimeter-self->c)));
	return Py_BuildValue("s", str);
}

static PyObject* Triangle_str(Triangle* self){
	char str1[20];
	char str2[20];
	char str3[20];
	sprintf(str1, "%.2f", self->a);
	sprintf(str2, "%.2f", self->b);
	sprintf(str3, "%.2f", self->c);
	return PyUnicode_FromFormat("a=%s, b=%s, c=%s", str1, str2, str3);
}

//***********************************************************************************************************

static PyMemberDef Triangle_members[] = {
    {"a", T_FLOAT, offsetof(Triangle, a), 0, "First side of triangle"},
    {"b", T_FLOAT, offsetof(Triangle, b), 0, "Second side of triangle"},
	{"c", T_FLOAT, offsetof(Triangle, c), 0, "Third side of triangle"},
    {NULL}  
};

static PyMethodDef Triangle_methods[] = {
    {"perimeter", (PyCFunction)Triangle_perimeter, METH_NOARGS, "Returns the perimeter of triangle."},
	{"area", (PyCFunction)Triangle_area, METH_NOARGS, "Returns the area of triangle."},
    {NULL}  
};

//***********************************************************************************************************

static PyTypeObject TriangleType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "triangle.Triangle",             /* tp_name */
    sizeof(Triangle),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Triangle_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    (reprfunc)Triangle_str,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "This is a triangle",        /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Triangle_methods,             /* tp_methods */
    Triangle_members,             /* tp_members */
    0,           				/* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Triangle_init,      /* tp_init */
    0,                         /* tp_alloc */
    Triangle_new,                 /* tp_new */
};

static struct PyModuleDef triangleModule ={
  PyModuleDef_HEAD_INIT, 
  "triangleModule", // name of module
  "Triangle type", // module documentation, may be NULL
  -1, // size of per- interpreter state of the module, or -1 if the module keeps state in global variables. 
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_triangle (void){ //import triangleModule
  PyObject* m;
  //TriangleType.tp_new = PyType_GenericNew;
  if (PyType_Ready(&TriangleType)< 0) 
    return NULL;
  m = PyModule_Create(&triangleModule);
  if (m == NULL)
    return NULL;
  Py_INCREF(&TriangleType);
  PyModule_AddObject(m, "Triangle", (PyObject*)&TriangleType);
  
  triangleError = PyErr_NewException("triangle.error", NULL, NULL);
  Py_INCREF(triangleError);
  PyModule_AddObject(m, "error", triangleError);
  
  return m; 
}




