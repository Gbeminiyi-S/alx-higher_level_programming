#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 *
 * Return: 1 if it has a cycle, else, 0
 */
int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t *hare = list, *tortoise = list;

		while (hare && tortoise)
		{
			tortoise = tortoise->next;
			hare = hare->next->next;
			if (hare == tortoise)
				return (1);
		}
	}
	return (0);
}
