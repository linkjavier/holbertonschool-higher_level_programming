#include "lists.h"

/**
 * is_palindrome - Main function where calling match() function
 * @head: Address to head.
 * Return: match() to compare
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	return (match(head, *head));
}

/**
 * match - validates if palindrome
 * @first: Address to first.
 * @last: Address to last.
 * Return: 1
 */

int match(listint_t **first, listint_t *last)
{
	if (!last)
		return (1);
	if (match(first, last->next))
	{
		if ((*first)->n == last->n)
		{
			*first = (*first)->next;
			return (1);
		}
	}
	return (0);
}
