#ifndef POMPE_H
#define POMPE_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

#include "CAN_ADC.h"
#include "Timer2.h"
#include "PID.h"
#include "USART.h"

class pompe
{
public:
    pompe();
    void regulation(int consigneT);
    double temperatureMoteur();
    void get_String(char *buffer, uint16_t consigne);
    void get_stringR(char *buffer, CAN_ADC::ADC_Channel channel);
    double get_resistancePara(double _tension);

private:
    const float PWM_MAX = 1600.0; // Valeur maximale de la PWM pour le timer 1
    const float PWM_MIN = 0.0;    // Valeur minimale de la PWM pour le timer 1
    const float K_P = 9.0;        // Gain proportionnel
    const float K_D = 0.2;        // Gain dérivé 
    const float periodeEchantillonageS = 0.1;
    const uint32_t rPara = 2200;
    const int resistance_table[8] = {356, 498, 722, 1000, 1334, 1722, 2166, 2624};
    const int temperature_table[8] = {-40, 0, 50, 100, 150, 200, 250, 300};

    CAN_ADC &adc = CAN_ADC::getInstance();
    USART &serial = USART::getInstance();
    PID monPID;

    // int16_t erreur_precedente = 0; // Stockage de l'erreur précédente
};

#endif // POMPE_H