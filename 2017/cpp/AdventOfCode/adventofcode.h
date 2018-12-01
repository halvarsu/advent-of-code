#ifndef ADVENTOFCODE_H
#define ADVENTOFCODE_H

#include <string>
#include <fstream>
#include <vector>

class AdventOfCode
{
public:
    AdventOfCode(std::string filename);
    AdventOfCode();
    ~AdventOfCode();
    virtual void solve(int part);
    virtual void part1();
    virtual void part2();

    std::ifstream file();

protected:
    std::ifstream m_file;
    std::string m_filename;
};

#endif // ADVENTOFCODE_H
