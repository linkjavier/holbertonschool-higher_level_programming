#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it.
 * @list: Address to list
 * Return: 0 if there is no cycle or 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list, *check2 = list;

	if (list == NULL)
		return (0);
	while (check1 != NULL && check2 != NULL && check2->next != NULL)
	{
		check1 = check1->next;
		check2 = check2->next->next;
		if (check1 == check2)
			return (1);
	}
	return (0);
}
