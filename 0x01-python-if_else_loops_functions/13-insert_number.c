#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the list head, a pointer to the head
 * @number: the number to insert
 * Return: address of node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *node;

		if (head == NULL)
			return (NULL);
		node = mallo(sizeof(listint_t));
		if (node == NULL)
			return (NULL);
		node->n = number;
		node->next = *head;
		head = node;
		return (node);
}
