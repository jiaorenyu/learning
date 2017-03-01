
#ifndef __EAGLE_INCLUDE__
#define __EAGLE_INCLUDE__

#include "bird.h"

class Eagle : public Bird {
public:
    Eagle(const std::string& name) ;
    
    virtual void sound();   
private:
    std::string name;
};

#endif
