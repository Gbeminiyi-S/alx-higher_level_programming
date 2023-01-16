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
	listint_t *temp = *head, *new_node = NULL;

	while (temp && (temp->next->n <= number))
	{
		temp = temp->next;
	}

	if (temp)
	{
		new_node = malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = temp->next;
		temp->next = new_node;
		return (new_node);
	}
	return (NULL);
}
