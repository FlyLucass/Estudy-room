#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    int tab, ger;

    printf("Gerador de Tabuada de multiflicacao \nQual tabuada voce que gerar?");
    scanf("%d", &tab);
    printf("\nSegue a tabuada do %d:\n", tab);

    for (ger = 0; ger <= 10; ger++)
    {

        int calc = tab * ger;
        printf("%d*%d=  %d \n", tab, ger, calc);
    }

    return 0;
}