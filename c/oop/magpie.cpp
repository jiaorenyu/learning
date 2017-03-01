#include "magpie.h"

Magpie::Magpie(const std::string& name) {
    this->name = name;
}

void Magpie::sound() {
    std::cout << this->name << " sound!" << std::endl;
}

