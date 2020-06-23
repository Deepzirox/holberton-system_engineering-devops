#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * starway - infinite loop
 * Return: none
 */
void starway(void)
{
	while (1)
		;
}
/**
 * main - entry point
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t child;
	
	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child < 1)
			return (0);
		printf("Zombie process created, PID: %d\n", child);
	}
	starway();
	return (0);
}
