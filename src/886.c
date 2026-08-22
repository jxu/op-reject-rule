#include <stdio.h>
#include <stdint.h>

#define M 83456729
#define N 34
#define L 18 // count rad classes
#define HASHTABLE_BITS 26
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
// Fits in under 20 lines, which is pretty compact
uint64_t keys[HASHTABLE_SIZE]; // auto-init to 0
uint32_t values[HASHTABLE_SIZE]; 

// multiplicative hash
size_t hash_key(uint64_t key)
{
    return (key * 0x9E3779B97F4A7C15ULL) >> (64 - HASHTABLE_BITS);
}

void table_insert(uint64_t key, uint32_t val)
{
    size_t idx;

    // linear probe until we hit our key or empty key 0
    for (idx = hash_key(key); 
         keys[idx] != key && keys[idx] != 0;
         idx = (idx + 1) % HASHTABLE_SIZE) 
        ;
        
    keys[idx] = key;
    values[idx] = val;
}

uint32_t table_get(uint64_t key)
{
    // linear probe for our key until we hit empty key
    for (size_t idx = hash_key(key); 
         keys[idx] != 0;
         idx = (idx + 1) % HASHTABLE_SIZE)
    {
        if (keys[idx] == key)
            return values[idx];
    }

    return EMPTY_VAL;
}

int extract_count(uint64_t bits, int i)
{
    return (bits >> (3*i)) & 7;
}

// Store rad class i and DP bit-pack in one key.
// In theory, it is possible to really compress the key into a 32-bit int:
// Given these rad_freq at n = 34:
// (5, 3, 2, 4, 1, 2, 1, 1, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1)
// and also storing 33 values of i,
// In mixed-radix representation, this requires exactly
// 33 * (5+1) * (4+1)^2 * (3+1) * (2+1)^3 * (1+1)^11 = 1094860800 values
// So 31 bits. But I don't think it's worth doing so I just give 3 bits per
// rad and have lots of space left over.
uint64_t pack_key(int i, uint64_t bits)
{
    return ((uint64_t)i << 56) | bits;
}

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a % b); // compiler optimizes tail-call
}

uint64_t f(uint64_t seen, int i, int depth)
{   
    // even-odd optimization
    // the full path using 2 through N (even) must be
    // even-odd-...-even, so all prefix paths must be too
    if (depth % 2 != rad_repr[i] % 2)
        return 0;

    uint32_t cached = table_get(pack_key(i, seen));

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

    table_insert(pack_key(i, seen), res);
    return res;
}

int main()
{
    // temp array that maps rad to count
    int rad_count[N+1] = {0};

    for (int i = 2; i <= N; i++) 
        rad_count[rad[i]]++;

    // extract unique rad classes
    int l = 0;
    for (int r = 0; r <= N; r++) // goes through rad values in order
    {   
        if (rad_count[r] > 0)
        {
            rad_repr[l] = r;
            rad_freq[l] = rad_count[r];
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

    // Bit-pack rad freqs into 3 bits each
    uint64_t full = 0;
    for (int i = 0; i < L; i++)
        full |= (uint64_t)(rad_freq[i]) << (3 * i);

    uint64_t res = 0;
    for (int i = 0; i < L; i++)
        res = (res + rad_freq[i] * f(full, i, N)) % M;

    printf("%lu\n", res);
}