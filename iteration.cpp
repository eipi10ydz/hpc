#include <iostream>
#include <random>
#include <algorithm>
#include <tuple>
#include <vector>
#include <iterator>
#include <limits>
#include <cstdlib>

using Iterator = std::vector<std::tuple<unsigned, unsigned, unsigned>>::iterator;
using Item = std::tuple<unsigned, unsigned, unsigned>;
const unsigned MAX = std::numeric_limits<unsigned>::max();

std::ostream& operator<<(std::ostream &os, const Item &t)
{
    os << std::get<0>(t) << " " << std::get<1>(t) << " " << std::get<2>(t) << std::endl;
    return os;
}


bool updatePn(Iterator beg, Iterator end)
{
    bool res = true;
    std::sort(beg, end, [](const Item &a, const Item &b){ return std::get<2>(a) < std::get<2>(b) || ((std::get<2>(a) == std::get<2>(b)) && std::get<0>(a) < std::get<0>(b)); });
    auto tempBeg = beg, tempEnd = beg;
    while (tempBeg != end)
    {
        //std::tie(tempBeg, tempEnd) = std::equal_range(beg, end, std::get<2>(*tempBeg), [](const Item &a, const Item &b){ return std::get<2>(a) < std::get<2>(b); });
        for (auto it = tempBeg; it != end && (std::get<2>(*it) == std::get<2>(*tempBeg)); ++it)
            tempEnd = it;
        ++tempEnd;
        auto min = std::min(std::get<2>(*tempBeg), std::get<0>(*tempBeg));
        for (auto it = tempBeg; it != tempEnd; ++it)
        {   
            if (min < std::get<1>(*it))
            {
                res = false;
                std::get<1>(*it) = min;
            }
        }
        tempBeg = tempEnd;
    }
    return res;
}

bool updatePc(Iterator beg, Iterator end)
{
    bool res = true;
    std::sort(beg, end, [](const Item &a, const Item &b){ return std::get<0>(a) < std::get<0>(b) || ((std::get<0>(a) == std::get<0>(b)) && std::get<1>(a) < std::get<1>(b)); });
    auto tempBeg = beg, tempEnd = end;
    while (tempBeg != end)
    {
        //std::tie(tempBeg, tempEnd) = std::equal_range(beg, end, std::get<0>(*tempBeg), [](const Item &a, const Item &b){ return std::get<0>(a) < std::get<0>(b); });
        for (auto it = tempBeg; it != end && (std::get<0>(*it) == std::get<0>(*tempBeg)); ++it)
            tempEnd = it;
        ++tempEnd;
        auto min = std::get<1>(*tempBeg);
        for (auto it = tempBeg; it != tempEnd; ++it)
        {
            if (min < std::get<0>(*it))
            {
                res = false;
                std::get<0>(*it) = min;
            }
        }
        tempBeg = tempEnd;
    }
    return res;
}

void generate_vector(std::vector<Item> &v, unsigned cnt)
{
    std::default_random_engine e;
    std::uniform_int_distribution<unsigned> u(0, MAX);
    unsigned left = u(e);
    unsigned right = u(e);
    for (unsigned i = 0; i <= cnt; ++i)
    {
        v.push_back(std::make_tuple(left, MAX, right));
        v.push_back(std::make_tuple(right, MAX, left));
        left = right;
        right = u(e);
    }
}

int main(int argc, char **argv)
{
    unsigned cnt = 0;
    if (argc > 1)
        cnt = atoi(argv[1]);
    std::vector<Item> v;// = {{1, MAX, 3}, {2, MAX, 3}, {3, MAX, 1}, {3, MAX, 2}, {2, MAX, 4}, {4, MAX, 2}};
    generate_vector(v, cnt);
    //for (auto i : v)
    //    std::cout << i << std::endl;
    //std::cout << updatePn(v.begin(), v.end()) << std::endl;
    //for (auto i : v)
    //    std::cout << i << std::endl;
    //std::cout << updatePc(v.begin(), v.end()) << std::endl;
    //for (auto i : v)
    //    std::cout << i << std::endl;
    //std::copy(v.begin(), v.end(), std::ostream_iterator<Item>(std::cout, " "));
    //std::cout << std::endl;
    //std::cout << updatePn(v.begin(), v.end()) << std::endl;
    //std::cout << updatePc(v.begin(), v.end()) << std::endl;
    int count = 1;
    while (!(updatePn(v.begin(), v.end()) && updatePc(v.begin(), v.end())))
        std::cout << "Iteration #" << count++ << std::endl;
    //for (auto i : v)
    //    std::cout << i << std::endl;
}
