#include <stdio.h>
#include <stdint.h>

#define M 83456729
#define n 10
#define L 18 // count rad classes
#define HASHTABLE_BITS 22
#define HASHTABLE_SIZE (1 << HASHTABLE_BITS)

#define EMPTY_VAL ((uint32_t)(-1))

// special: primes > N/2 get special rad 1 that is coprime to all
const int rad[] = 
{
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 1, 
    10, 21, 22, 1, 6, 5, 26, 3, 14, 1,
    30, 1, 2, 33, 34
};

int rad_repr[L];
int rad_freq[L];
int coprime[L][L];

// Handmade linear probing hash table for fun
uint64_t keys[L][HASHTABLE_SIZE]; // auto-init to 0
uint32_t values[L][HASHTABLE_SIZE]; 

// multiplicative hash
size_t hash_key(uint64_t key)
{
    return (key * 0x9E3779B97F4A7C15ULL) >> (64 - HASHTABLE_BITS);
}

// flat array for now
void table_insert(int i, uint64_t key, uint32_t val)
{
    values[i][key] = val;
}

uint32_t table_get(int i, uint64_t key)
{
    return EMPTY_VAL;
}


int extract_count(uint64_t bits, int i)
{
    return (bits >> (3*i)) & 7;
}

uint64_t pack_key(int i, uint64_t bits)
{
    return ((uint64_t)i << 56) | bits;
}

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a % b);
}

uint64_t f(uint64_t seen, int i, int depth)
{   
    // even-odd optimization
    // the full path using 2 through n (even) must be
    // even-odd-...-even, so all prefix paths must be too
    if (depth % 2 != rad_repr[i] % 2)
        return 0;

    uint32_t cached = table_get(i, seen);

    if (cached != EMPTY_VAL)
        return cached;

    if (seen == (1ull << (3*i)))
        return 1;

    uint64_t new_seen = seen - (1ull << (3*i));
    uint64_t res = 0;

    for (int j = 0; j < L; ++j)
    {
        int count_j = extract_count(new_seen, j);
        if (coprime[i][j] && count_j > 0)
            res = (res + count_j * f(new_seen, j, depth-1)) % M;
    }

    table_insert(i, seen, res);
    return res;
}

int main()
{
    // temp array that maps rad to count
    int rad_count[n+1] = {0};

    for (int i = 2; i <= n; i++) 
        rad_count[rad[i]]++;

    // extract unique rad classes
    int l = 0;
    for (int r = 0; r <= n; r++) // goes through rad values in order
    {   
        if (rad_count[r] > 0)
        {
            rad_repr[l] = r;
            rad_freq[l] = rad_count[r];
            
            printf("%d %d\n", rad_repr[l], rad_freq[l]);
            l++;
        }
    }

    for (int i = 0; i < L; ++i) 
    {
        for (int j = 0; j < L; ++j) 
        {
            coprime[i][j] = (gcd(rad_repr[i], rad_repr[j]) == 1);
        }
    }

    uint64_t full = 0;
    for (int i = 0; i < L; i++)
        full |= (uint64_t)(rad_freq[i]) << (3 * i);

    uint64_t res = 0;
    for (int i = 0; i < L; i++)
    {
        res = (res + rad_freq[i] * f(full, i, n)) % M;
    }

    printf("%lu\n", res);
}