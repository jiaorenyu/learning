#ifndef __MAGPIE_INCLUDE__
#define __MAGPIE_INCLUDE__

#include "bird.h"

class Magpie: public Bird {
public:
    Magpie(const std::string& name) ;
    
    virtual void sound();   
private:
    std::string name;
};

#endif
