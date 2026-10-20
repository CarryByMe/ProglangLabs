#include <iostream>
#include <fstream>

namespace output {
    void print(const std::string& msg) {
        std::cout << msg << '\n';
    }
}

namespace file {
    void print(const std::string& msg) {
        std::ofstream f("output.txt");
        f << msg << '\n';
    }
}

int main() {
    output::print("aaa");
    file::print("aaa");

}
