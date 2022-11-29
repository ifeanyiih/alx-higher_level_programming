#include "lists.h"

/**
* check_cycle - checks if a list has a cycle
* @list: the list to check
* Description: checks if a singly linked list has a cycle in it
* Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t p, q;

	p = q = list;
	while (p != NULL)
	{
		p = p->next->next;
		q = q->next;
		if (p == q)
			return (1);
	}
	return (0);
}
