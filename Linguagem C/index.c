#include <stdio.h>
#include <stdlib.h>

// alocação_automaitca(apenas detro da função)
// int main(void)
// {
//     int numero;
//     printf("digite um numero inteiro: ");
//     scanf("%i", &numero);

//     int *ponteiro;
//     ponteiro = &numero;
//     printf("O numero: %i esta no endereco de memoria: %p", *ponteiro, (void *)ponteiro);

//     return 0;
// }

// estatica(com variaveis globais)
// int numero;

// int main(void)
// {

//     printf("digite um numero inteiro: ");
//     scanf("%i", &numero);

//     int ponteiro = &numero;
//     printf("O numero: %i, esta no endereco de memoria: %p", numero, ponteiro);
//     return 0;
// }

// alocação_dinamica

// int main(void)
// {
//     int numero = 10;
//     int *ponteiro;
//     ponteiro = (int *)malloc(sizeof(numero));

//     int numero2 = 20;
//     ponteiro = (int *)realloc(ponteiro, 2 * sizeof(int));
//     ponteiro[0] = numero;
//     ponteiro[1] = numero2;

//     printf("%i,%p", ponteiro[0], (void *)&ponteiro[0]);
//     printf("\n%i,%p", ponteiro[1], (void *)&ponteiro[1]);

//     free(ponteiro);
//     ponteiro = NULL;
//     printf("\n%p", (void *)ponteiro);
// }

// int main(void)
// {
//     int *p;
//     p = (int *)malloc(5 * sizeof(int));
// int i;
// for (i = 0; i < 5; i++)
// {
//     printf(" %d ", p[i]);
// }
//     if (p != NULL)
//     {
//         int i;
//         for (i = 0; i < 5; i++)
//         {
//             p[i] = i + 1;
//         }
//         for (i = 0; i < 5; i++)
//         {
//             printf(" %d ", p[i]);
//         }
//         free(p);
//     }
//     else
//     {
//         printf("Erro na alocação");
//     }
//     return 0;
// }

// int main(void)
// {
//     int *p;
//     p = (int *)calloc(5, sizeof(int));
//     int i;
//     for (i = 0; i < 5; i++)
//     {
//         printf(" %d ", p[i]);
//     }
//     printf("\n");
//     if (p != NULL)
//     {
//         int i;
//         for (i = 0; i < 5; i++)
//         {
//             p[i] = i + 1;
//         }
//         for (i = 0; i < 5; i++)
//         {
//             printf(" %d ", p[i]);
//         }
//         free(p);
//     }
//     else
//     {
//         printf("Erro na alocação");
//     }
//     return 0;
// }

int main(void)
{
    int num = 30;
    int *pont = &num;
    printf("%d", num);     // mostra 30 de acordo a variavel
    printf("\n%p", pont);  // mostra endereço de memoria
    printf("\n%d", *pont); // mostra 30 com base no endereço de memoria

    *pont = 90;
    printf("\n%d", num);

    int *ponteiro;
    ponteiro = (int *)malloc(sizeof(int));
    *ponteiro = 10;
    printf("\n%d", *ponteiro);
    printf("\n%p", ponteiro);

    free(pont);
    free(ponteiro);
    pont = NULL;
    ponteiro = NULL;

    return 0;
}