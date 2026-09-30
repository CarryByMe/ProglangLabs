#include <iostream>

int main() {
    int a = 5;
    double b = 2.5;

    decltype(a + b) c; 

    c = a + b;
    std::cout << c;
}