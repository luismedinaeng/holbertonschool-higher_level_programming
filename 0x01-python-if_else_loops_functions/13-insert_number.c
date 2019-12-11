#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node on a sorted linked list
 * @head: Head of the list
 * @number: Data to add to the list
 *
 * Return: The address of the new node or NULL if it failed
 * If the index exceeds the limits of the list,
 * does not add a node and return NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_element;

	if (number <= (*head)->n)
	{
		new_element = malloc(sizeof(listint_t));
		if (new_element == NULL)
			return (NULL);

		new_element->n = number;

		new_element->next = (*head);
		*head = new_element;

		return (new_element);
	}
	else
	{
		if (*head != NULL)
			return (insert_node(&((*head)->next), number));
		else
			return (NULL);
	}
}
