#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    pid_t pid;
    pid = fork();
    int value = 0;

    if (pid < 0)
    {
        printf("Fork failed\n");
        exit(-1);
    }
    else if (pid == 0)
    {
        for(;;)
        {
            printf("Child process, value is %d\n", value);
            value++;
            sleep(2);
        }
    }
    else
    {
        for(;;)
        {
            printf("Parent process, value is %d\n", value);
            sleep(2);
        }
    }
    return 0;
}

