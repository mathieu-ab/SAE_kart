#ifndef TIMER1_H
#define TIMER1_H

#include <avr/io.h>

class Timer1
{
public:
    // Méthode statique pour accéder à l'instance unique
    static Timer1 &getInstance()
    {
        static Timer1 instance; // Instance unique
        return instance;
    }
    // Suppression des constructeurs de copie et de l'opérateur d'affectation
    Timer1(const Timer1 &) = delete;
    Timer1 &operator=(const Timer1 &) = delete;

private:
    Timer1();
};

#endif // TIMER1_H