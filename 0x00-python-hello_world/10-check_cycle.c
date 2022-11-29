#include "lists.h"

/**
* check_cycle - checks if a list has a cycle
* @list: the list to check
* Description: checks if a singly linked list has a cycle in it
* Return: 0 if no cycle, 1 otherwise
*/
int check_cycle(listint_t *list)
{
	while (list != NULL)
	{
		if (list == list->next->next)
			return (1);
		list = list->next;
	}
	return (0);
}
