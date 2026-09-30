#include <iostream>
#include <vector>


typedef std::vector<int> vi;

int main() {
    vi numbers = {10, 20, 30, 40, 50};


    for (int x : numbers) {
        std::cout << x << " ";
    }
}