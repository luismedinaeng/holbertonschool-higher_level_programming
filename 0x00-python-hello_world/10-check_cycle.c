#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Finds a loop in a listint_t list
 * @head: Head of the list
 *
 * Description: Finds a loop in a linked list
 *
 * Return: The node where is the loop or NULL if does not have loop
 */
int check_cycle(listint_t *list)
{
	listint_t *add_a, *add_b;

	if (list == NULL)
		return (0);

	add_a = list;
	add_b = list;

	while (1)
	{
		add_a = add_a->next;
		if (add_b->next == NULL)
			return (0);
		else if ((add_b->next)->next == NULL)
			return (0);

		add_b = (add_b->next)->next;

		if (add_a == add_b)
			break;
	}
	return (1);
}
