#include "Timer2.h"

Timer2::Timer2(uint32_t *_cptPF)
{
    cptPF = _cptPF;

    // Configuration du Timer2
    TCCR2A = 0;                                        // Mode normal
    TCCR2B = 0;                                        // Reset
    TCCR2B |= (1 << CS20) | (1 << CS21) | (1 << CS22); // Diviseur d'horloge 1024

    TIMSK2 = (1 << TOIE2); // Activation des interruptions de débordement
    TCNT2 = 0;             // Initialisation du compteur
}

float Timer2::get_timeS()
{
    uint8_t cptPFa = TCNT2;
    cli(); // Désactiver temporairement les interruptions
    uint32_t cpt = (*cptPF << 8) | (cptPFa);
    sei(); // Réactiver les interruptions
    return (((double)cpt / (frequenceTimer2Div2)) / 1000.0);
}

float Timer2::get_timeMS()
{
    uint8_t cptPFa = TCNT2;
    cli(); // Désactiver temporairement les interruptions
    uint32_t cpt = (*cptPF << 8) | (cptPFa);
    sei(); // Réactiver les interruptions
    return ((double)cpt / (frequenceTimer2Div2));
}
