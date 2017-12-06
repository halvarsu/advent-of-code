#ifndef DAY5_H
#define DAY5_H

#include "adventofcode.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <memory>


class Day5
{
public:
    Day5(std::string filename);
    ~Day5();
    void solve(int part);
    void part1();
    void part2();
    std::vector<int> &get_input();

private:
    std::string m_filename;
    std::vector<int> m_inputData;
};

#endif // DAY5_H
