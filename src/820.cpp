#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>

int d(int n, int k)
{
    std::vector<int> rems;
    std::unordered_set<int> rems_set;
    std::vector<int> qs;
    int rem = 1;
    int rep_i;

    while (true) 
    {
        int d = rem * 10;
        int q = d / k;

        //std::cout << d << " " << q << " rems";

        for (auto x : rems) 
        {
            //std::cout << x << " ";
        }

        if (rems_set.contains(rem))
        {
            rep_i = std::find(rems.begin(), rems.end(), rem) - rems.begin();
            //std::cout << "rep_i " << rep_i << "\n";
            break;
        }
        //std::cout << "\n";

        rems.push_back(rem);
        rems_set.insert(rem);
        qs.push_back(q);

        rem = d - k * q;

    }

    auto repetend = std::vector<int>(qs.begin() + rep_i, qs.end());

    for (auto x : repetend) {
        //std::cout << x << " ";

    }
    //std::cout << "\n";
    //
    if (k % 1000 == 1) std::cout << k << "\n";

    int idx = (n - 1 - rep_i) % repetend.size();

    return repetend[idx];
}

long long S(int n)
{
    long long s = 0;
    for (int k=1; k<=n; ++k)
        s += d(n, k);

    return s;

}

int main() 
{
    std::cout << S(100000) << std::endl;
    return 0;
}
