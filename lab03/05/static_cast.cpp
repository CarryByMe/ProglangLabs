#include <iostream>
#include <algorithm>

int main() {
    long long x = 1LL << 40;
    double d = 1.2e12;
    
    std::cout << std::max(x, static_cast<long long>(d)) << std::endl;

}    