#include <stdio.h>
#include <stdlib.h>
#include <sys/param.h>

#define BOARD_LEN 40
#define TURNS 10000000
#define DICE_SIDES 4

enum Board 
{
    GO   = 0,
    A1   = 1,
    CC1  = 2,
    A2   = 3,
    T1   = 4,
    R1   = 5,
    B1   = 6,
    CH1  = 7,
    B2   = 8,
    B3   = 9,
    JAIL = 10,
    C1   = 11,
    U1   = 12,
    C2   = 13,
    C3   = 14,
    R2   = 15,
    D1   = 16,
    CC2  = 17,
    D2   = 18,
    D3   = 19,
    FP   = 20,
    E1   = 21,
    CH2  = 22,
    E2   = 23,
    E3   = 24,
    R3   = 25,
    F1   = 26,
    F2   = 27,
    U2   = 28,
    F3   = 29,
    G2J  = 30,
    G1   = 31,
    G2   = 32,
    CC3  = 33,
    G3   = 34,
    R4   = 35,
    CH3  = 36,
    H1   = 37,
    T2   = 38,
    H2   = 39
};

int counter[BOARD_LEN];

int compare_squares(const void* a, const void* b) 
{
    int x = counter[*(const int*)a];
    int y = counter[*(const int*)b];
    return y - x;  /* reverse */

}

int main() 
{
    for (int i=0; i<BOARD_LEN; ++i)
        counter[i] = 0;
    int pos = 0;
    int doubles = 0;

    for (int t=0; t<TURNS; ++t)
    {
        /* roll dice */
        int d1 = rand() % DICE_SIDES + 1;
        int d2 = rand() % DICE_SIDES + 1;
        int d = d1 + d2;

        if (d1 == d2) doubles += 1;
        else          doubles = 0;

        //printf("dice %d+%d=%d doubles:%d\n", d1, d2, d, doubles); 

        if (doubles == 3)
        {
            doubles = 0;
            pos = JAIL;
        } 
        else 
            pos = (pos + d) % BOARD_LEN;

        /* handle special squares */
        /* go to jail */
        if (pos == G2J) 
            pos = JAIL;

        /* chance */
        if (pos == CH1 || pos == CH2 || pos == CH3)
        {
            int card = rand() % 16;
            //printf("chance %d\n", card);
            if (card == 0)
                pos = GO;
            else if (card == 1)
                pos = JAIL;
            else if (card == 2)
                pos = C1;
            else if (card == 3)
                pos = E3;
            else if (card == 4)
                pos = H2;
            else if (card == 5)
                pos = R1;
            else if (card == 6 || card == 7)
            {
                while (pos != R1 && pos != R2 && pos != R3)
                    pos = (pos + 1) % BOARD_LEN;
            }
            else if (card == 8)
            {
                while (pos != U1 && pos != U2)
                    pos = (pos + 1) % BOARD_LEN;
            } 
            else if (card == 9) 
                pos = (pos - 3 + BOARD_LEN) % BOARD_LEN;
        }


        /* chest */
        if (pos == CC1 || pos == CC2 || pos == CC3) 
        {
            int card = rand() % 16;
           //printf("chest %d\n", card);
            if (card == 0)
                pos = GO;
            else if (card == 1)
                pos = JAIL;
       }


        /* record position after roll */
        //printf("pos %d\n", pos);
        counter[pos] += 1;

    }

    /* top 3 squares */
    int topsq[BOARD_LEN];
    for (int i=0; i<BOARD_LEN; ++i)
        topsq[i] = i;

    qsort(topsq, BOARD_LEN, sizeof(int), compare_squares);

    for (int i=0; i<3; ++i)
    {
        int sq = topsq[i];
        printf("%d %d\n", sq, counter[sq]);
    }

    printf("%02d%02d%02d\n", topsq[0], topsq[1], topsq[2]);

}
