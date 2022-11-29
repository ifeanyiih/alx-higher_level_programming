#include "lists.h"

/**
* check_cycle - checks if a list has a cycle
* @list: the list to check
* Description: checks if a singly linked list has a cycle in it
* Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *p, *q;

	p = q = list;
	while (p != NULL && q != NULL)
	{
		q = q->next;

		p = p->next;
		if (p == NULL)
				return (0);
		p = p->next;
		if (p == q)
			return (1);
	}
	return (0);
}
