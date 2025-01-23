#ifndef TIMER0_H
#define TIMER0_H

#include <avr/io.h>

class Timer0
{
public:
    // Méthode statique pour accéder à l'instance unique
    static Timer0 &getInstance()
    {
        static Timer0 instance; // Instance unique
        return instance;
    }
    // Suppression des constructeurs de copie et de l'opérateur d'affectation
    Timer0(const Timer0 &) = delete;
    Timer0 &operator=(const Timer0 &) = delete;

private:
    Timer0();
};

#endif // TIMER0_H
