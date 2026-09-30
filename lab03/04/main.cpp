#include <iostream>

int main(){
    bool x = true, y = false;
    auto a = x & y;
    std::cout << typeid(a).name() << std::endl;
    std::cout << a<< std::endl;
    auto b = x && y;
    std::cout << typeid(b).name() << std::endl;
    std::cout << b << std::endl;

    
 
    
}