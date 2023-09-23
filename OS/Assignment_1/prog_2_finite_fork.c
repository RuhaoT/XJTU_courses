#include <stdio.h>
#include <unistd.h>

int main()
{

    printf("Process forked.\n");
    int i;
    for (i = 0; i < 3; i++)
    {
        fork();
        printf("Process forked.\n");
        sleep(3);
    }
    return 0;
}

