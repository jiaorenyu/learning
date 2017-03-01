#include "eagle.h"

Eagle::Eagle(const std::string & name) {
    this->name = name;
}

void Eagle::sound() {
    std::cout << this->name <<" sound!" << std::endl;
}
