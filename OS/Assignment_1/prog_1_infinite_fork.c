#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("Process forked.\n");

    int i = 1;
    while(i++)
    {
        fork();
        printf("Process forked.\n");
    }
}

