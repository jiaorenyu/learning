
#include <iostream>

#include "bird.h"
#include "eagle.h"
#include "magpie.h"

static Bird *bird; 

using namespace std;
int main() {
    Eagle eagle("eagle");
    Magpie magpie("eagle");
    
    bird = new Eagle("eagle");
    bird->sound();
    bird = new Magpie("magpie");
    bird->sound();

    return 0;
}
