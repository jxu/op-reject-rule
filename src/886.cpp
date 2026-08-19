#include <iostream>
#include <cstdint>
#include <vector>
#include <numeric>
#include <unordered_map>
#include <format>
#include <bit>

using namespace std;

const std::vector<int> rad_lookup = {
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 19, 
    10, 21, 22, 23, 6, 5, 26, 3, 14, 29,
    30, 31, 2, 33, 34
};

const int n = 34;

std::vector<int> rad;
std::unordered_map<int, std::vector<int>> rad_dict;
std::vector<int> rad_freq;
std::vector<int> rad_bitcount;
std::vector<int> rad_shift;
std::vector<std::vector<bool>> cp;

std::size_t L = 0;



vector<unordered_map<int, int>> dp;

int extract_count(int bits, int i)
{
    return (bits >> rad_shift[i]) & ((1 << rad_bitcount[i]) - 1);
}

int f(int seen, int i)
{
    if (dp[i].contains(seen))
    {
        return dp[i][seen];
    }

    if (seen == (1 << rad_shift[i]))
        return 1;

    int new_seen = seen - (1 << rad_shift[i]);

    int res = 0;

    for (int j = 0; j < L; ++j)
    {
        int count_j = extract_count(seen, j);
        if (cp[i][j] == 1 && count_j > 0)
        {
            res += count_j * f(new_seen, j);
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
        rad.push_back(key);                // v[0]
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

    rad_bitcount.reserve(L);
    for (int freq : rad_freq) {
        rad_bitcount.push_back(std::bit_width((unsigned int)freq));
    }

    rad_shift = std::vector<int> (L, 0);
    int current_shift = 0;
    for (std::size_t i = 0; i < L; ++i) {
        rad_shift[i] = current_shift;
        current_shift += rad_bitcount[i];
    }

    int full = 0;
    for (int i = 0; i < L; i++)
    {
        full |= (rad_freq[i]) << (rad_shift[i]);
    }

    int res = 0;
    for (int i = 0; i < L; i++)
    {
        int z = f(full, i);
        std::cout << i << " " << z << endl;
        res += rad_freq[i] * z;
    }

    std::cout << res << endl;


}