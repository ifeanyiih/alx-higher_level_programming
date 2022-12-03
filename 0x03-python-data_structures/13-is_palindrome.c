#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to the head of the list
 * Return: 1 if True, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	unsigned int i, j, mid;
	int *list_array, is_pal;

	if (head == NULL || *head == NULL)
		return (1);

	i = 0;
	node = *head;
	while (node != NULL)
	{
		i++;
		node = node->next;
	}

	list_array = malloc(sizeof(int) * i);

	i = 0;
	node = *head;
	while (node != NULL)
	{
		list_array[i] = node->n;
		++i;
		node = node->next;
	}

	is_pal = 1;
	j = 0;
	mid = i / 2, --i;
	while (j < mid)
	{
		if (!(list_array[j] == list_array[i]))
		{
			is_pal = 0;
			break;
		}
		++j, --i;
	}
	free(list_array);
	return (is_pal);
}
