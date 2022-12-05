#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints some basic info about python lists
* @p: pointer to PyOject
*/
void print_python_list_info(PyObject *p)
{
	unsigned int i, j;
	PyObject *item;

	if (PyList_CheckExact(p))
	{
		i = PyList_Size(p);
		printf("[*] Size of the Python List = %u\n", i);
		printf("[*] Allocated = %u\n", (unsigned int)Py_REFCNT(p));
		for (j = 0; j < i; ++j)
		{
			item = PyList_GetItem(p, j);
			printf("Element %u: %s\n", j, (Py_TYPE(item))->tp_name);
		}
	}
}
