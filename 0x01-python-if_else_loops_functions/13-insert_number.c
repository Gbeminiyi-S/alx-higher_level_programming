#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: double pointer to the list's head
 * @number: number to be inserted
 *
 * Return: address of the new node, else, NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new_node = NULL, *prev;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!(*head)) /* if empty list*/
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	if ((*head)->n >= number) /* if insert at Beg. */
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (temp && (temp->n < number))
		{
			prev = temp;
			temp = temp->next;
		}
		if (!temp) /* if insert at end */
		{
			prev->next = new_node;
			new_node->next = NULL;
		}
		else
		{
			prev->next = new_node;
			new_node->next = temp;
		}
	}
	return (new_node);
}
