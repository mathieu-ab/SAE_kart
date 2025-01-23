#ifndef TIMER2_H
#define TIMER2_H

#include <avr/io.h>
#include <avr/interrupt.h>

class Timer2
{
public:
    // Méthode statique pour accéder à l'instance unique
    static Timer2 &getInstance(uint32_t *_cptPF = nullptr)
    {
        static Timer2 instance(_cptPF); // Instance unique
        return instance;
    }

    float get_timeS();
    float get_timeMS();
    
    // Suppression des constructeurs de copie et de l'opérateur d'affectation
    Timer2(const Timer2 &) = delete;
    Timer2 &operator=(const Timer2 &) = delete;

private:
    Timer2(uint32_t *_cptPF);

    uint32_t *cptPF;
    double frequenceTimer2 = (F_CPU) / (2.0 * 1024.0 * (1.0 + 255.0));
    double frequenceTimer2Div2 = frequenceTimer2 / 2.0;
};

#endif // TIMER2_H