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
	pid_t pid;
	int x;

	for (x = 0; x < 5; x++)
	{
		pid = fork();
		if (pid < 1)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	starway();
	return (0);
}
