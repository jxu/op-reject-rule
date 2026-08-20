#include <iostream>
#include <cstdint>
#include <vector>
#include <numeric>
#include <unordered_map>

using namespace std;

// special: primes > N/2 get special rad 1 that is coprime to all
const std::vector<int> rad_lookup = {
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 1, 
    10, 21, 22, 1, 6, 5, 26, 3, 14, 1,
    30, 1, 2, 33, 34
};

const long long M = 83456729;
const int n = 34;

std::vector<int> rad;
std::unordered_map<int, std::vector<long long>> rad_dict;
std::vector<int> rad_freq;
std::vector<std::vector<bool>> cp;

long long L = 0;

vector<unordered_map<long long, long long>> dp;

int extract_count(long long bits, int i)
{
    return (bits >> (3*i)) & 7;
}

long long f(long long seen, int i)
{
    if (dp[i].contains(seen))
    {
        return dp[i][seen];
    }

    //if (extract_count(seen, i) == 0)
    //    return 0;

    if (seen == (1ull << (3*i)))
        return 1;

    long long new_seen = seen - (1ull << (3*i));

    long long res = 0;

    for (int j = 0; j < L; ++j)
    {
        int count_j = extract_count(new_seen, j);
        if (cp[i][j] == 1 && count_j > 0)
        {
            res = (res + count_j * f(new_seen, j)) % M;
        }
    }

    dp[i][seen] = res;

    return res;
}

int main()
{


    for (int i = 2; i <= n; ++i) {
        int rad_val = rad_lookup[i];
        rad_dict[rad_val].push_back(i);
    }

    rad_freq.reserve(rad_dict.size());
    rad.reserve(rad_dict.size());

    for (const auto& [key, group] : rad_dict) {

        rad.push_back(key);                
        rad_freq.push_back(group.size());  // len(v)
    }

    L = rad.size();

    dp.resize(L);

    cp = std::vector<std::vector<bool>>(L, std::vector<bool>(L, false));
    for (std::size_t i = 0; i < L; ++i) {
        for (std::size_t j = 0; j < L; ++j) {
            cp[i][j] = (std::gcd(rad[i], rad[j]) == 1);
        }
    }


    long long full = 0;
    for (int i = 0; i < L; i++)
    {
        full |= (long long)(rad_freq[i]) << (3 * i);
    }

    long long res = 0;
    for (int i = 0; i < L; i++)
    {
        long long z = f(full, i);
        std::cout << i << " " << z << endl;
        res = (res + rad_freq[i] * z) % M;
    }

    std::cout << res << endl;
}