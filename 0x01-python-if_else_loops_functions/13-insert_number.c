#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the list head, a pointer to the head
 * @number: the number to insert
 * Return: address of node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *pos;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	if (*head == NULL)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		pos = *head;
		while (pos != NULL)
		{
			if (pos->n < number)
				pos = pos->next;
			else
			{
				node->next = pos->next;
				pos->next = node;
				break;
			}
		}
	}
	return (node);
}
