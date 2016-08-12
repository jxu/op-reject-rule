// Rewrite of 265 using bit math and integers instead of strings

#include <iostream>
#include <bitset>

const int N = 5; // <=5 for 32 bit int
const int SEQLEN = 1 << N;

bool done(unsigned int seq)
{
    int ones = 0;
    while (seq)
    {
        ones += seq & 1;
        seq >>= 1;
    }
    return 2*ones == SEQLEN;
}

long long S(unsigned int seq, bool seen[])
{
    if (done(seq))
    {
        std::cout << std::bitset<32>(seq) << std::endl;
        return seq;
    }

    long long s = 0;

    for (int i=0; i<=1; i++)
    {
        if (i==0) seq <<= 1; // Append 0 to seq
        else seq += 1; // Append 1 to seq

        int subseq = seq & (SEQLEN - 1);
        if (!seen[subseq])
        {
            seen[subseq] = true;
            s += S(seq, seen);
            seen[subseq] = false;
        }
    }
    return s;
}

int main()
{
    bool seen[SEQLEN] = {0};
    seen[0] = true; // Seen 00000
    std::cout << S(0, seen) << std::endl; // Leading 0s ignored, start with 1
}
