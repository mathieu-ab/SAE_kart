#ifndef POMPE_H
#define POMPE_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

#include "CAN_ADC.h"

class pompe
{
public:
    pompe(CAN_ADC *_adc);
    void regulation(int consigneT);
    uint16_t calcul_commande(uint16_t consigne, uint16_t mesure);
    double temperatureMoteur();
    void get_String(char *buffer, uint16_t consigne);
    void get_stringR(char *buffer, CAN_ADC::ADC_Channel channel);
    double get_resistancePara(double _tension);

private:
    float PWM_MAX = 1600.0; // Valeur maximale pour le timer en 8 bits
    float K_P = 9;          // Gain proportionnel (à ajuster expérimentalement)
    float K_D = 0.2;        // Gain dérivé (à ajuster expérimentalement)
    uint32_t rPara = 2200;
    const int resistance_table[8] = {356, 498, 722, 1000, 1334, 1722, 2166, 2624};
    const int temperature_table[8] = {-40, 0, 50, 100, 150, 200, 250, 300};
    CAN_ADC *adc;
    int16_t erreur_precedente = 0; // Stockage de l'erreur précédente
};

#endif // POMPE_H