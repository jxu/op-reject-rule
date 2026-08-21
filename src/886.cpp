#include <iostream>
#include <cstdint>
#include <vector>
#include <numeric>
#include "flat_hash_map.hpp" // more efficient than unordered_map

using namespace std;

// special: primes > N/2 get special rad 1 that is coprime to all
const vector<int> rad = {
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 1, 
    10, 21, 22, 1, 6, 5, 26, 3, 14, 1,
    30, 1, 2, 33, 34
};

const uint64_t M = 83456729;
const int n = 34;

std::vector<int> rad_repr;
std::unordered_map<int, std::vector<uint64_t>> rad_dict;
std::vector<int> rad_freq;
std::vector<std::vector<bool>> cp;

int L = 0; // count rad equivalence classes

vector<ska::flat_hash_map<uint64_t, uint64_t>> dp;

int extract_count(uint64_t bits, int i)
{
    return (bits >> (3*i)) & 7;
}

uint64_t f(uint64_t seen, int i, int depth)
{   
    // even-odd optimization
    // the full path using 2 through n (even) must be
    // even-odd-...-even, so all prefix paths must be too
    if (depth % 2 != rad_repr[i] % 2)
        return 0;

    auto it = dp[i].find(seen);
    if (it != dp[i].end())
        return it->second;

    if (seen == (1ull << (3*i)))
        return 1;

    uint64_t new_seen = seen - (1ull << (3*i));
    uint64_t res = 0;

    for (int j = 0; j < L; ++j)
    {
        int count_j = extract_count(new_seen, j);
        if (cp[i][j] == 1 && count_j > 0)
            res = (res + count_j * f(new_seen, j, depth-1)) % M;
    }

    dp[i][seen] = res;
    return res;
}

int main()
{
    for (int i = 2; i <= n; ++i) 
        rad_dict[rad[i]].push_back(i);

    for (const auto& [key, group] : rad_dict) 
    {
        rad_repr.push_back(key);                
        rad_freq.push_back(group.size());  // len(v)
    }

    L = rad_repr.size();

    // reserve space for hash tables
    dp.resize(L);

    for (int i = 0; i < L; i++)
        dp[i].reserve(1 << 22);

    cp = vector<vector<bool>>(L, vector<bool>(L, false));
    for (int i = 0; i < L; ++i) 
    {
        for (int j = 0; j < L; ++j) 
        {
            cp[i][j] = (std::gcd(rad_repr[i], rad_repr[j]) == 1);
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

    std::cout << res << endl;
}