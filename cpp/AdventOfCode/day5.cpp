#include "day5.h"

Day5::Day5(std::string filename)
{
    m_filename = filename;
}

Day5::~Day5()
{
}

void Day5::solve(int part){

    std::cout << "Part 1: ";
    this->part1();
    std::cout << std::endl;

    std::cout << "Part 2: ";
    this->part2();
    std::cout << std::endl;
}

std::vector<int> & Day5::get_input(){
    std::ifstream infile(m_filename);
    std::string line;
    m_inputData.clear();

    for(int i = 0; std::getline(infile, line); i++){
        m_inputData.push_back(stoi(line));
    }
    infile.close();

    return m_inputData;
}

void Day5::part1(){
    std::vector<int> data = get_input();
    int steps = 0;
    int pos = 0;
    int offset;
    while (true) {
        if (pos >= data.size() || pos < 0){
            break;
        }
        offset = data[pos];
        data[pos] += 1;
        pos += offset;
        steps += 1;
    }
    std::cout << steps;
}

void Day5::part2(){
    std::vector<int> data = get_input();
    int steps = 0;
    int pos = 0;
    int offset;
    while (true) {
        if (pos >= data.size() || pos < 0){
            break;
        }
        offset = data[pos];
        if (offset >= 3){
            data[pos] -= 1;
        } else {
            data[pos] += 1;
        }
        pos += offset;
        steps += 1;
    }
    std::cout << steps;
}
