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
	listint_t *node, *pos, *nxt;

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
		nxt = pos->next;
		while (nxt != NULL)
		{
			if (number < pos->n && pos == *head)
			{
				node->next = pos;
				*head = node;
				break;
			}
			else if (nxt->n > number)
			{
				node->next = nxt;
				pos->next = node;
				break;
			}
			else
			{
				pos = pos->next;
				nxt = nxt->next;
			}
		}
		if (nxt == NULL)
		{
				node->next = NULL;
				pos->next = node;
		}
	}
	return (node);
}
