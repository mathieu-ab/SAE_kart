#ifndef CAN_ADC_H
#define CAN_ADC_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

class CAN_ADC
{
public:
    // Méthode statique pour accéder à l'instance unique
    static CAN_ADC &getInstance()
    {
        static CAN_ADC instance; // Instance unique
        return instance;
    }

    // Définir une énumération pour les canaux ADC
    enum ADC_Channel
    {
        ADC0 = 0b000,
        ADC1 = 0b001,
        ADC2 = 0b010,
        ADC3 = 0b011,
        ADC4 = 0b100,
        ADC5 = 0b101,
        ADC6 = 0b110,
        ADC7 = 0b111
    };

    uint16_t read(ADC_Channel channel);                 // Utiliser le type enum pour le paramètre
    void get_string(char *buffer, ADC_Channel channel); // renvoie une chaine de caractère de la tension et de la valeur de l'adc
    double get_tension(ADC_Channel channel);

    // Suppression des constructeurs de copie et de l'opérateur d'affectation
    CAN_ADC(const CAN_ADC &) = delete;
    CAN_ADC &operator=(const CAN_ADC &) = delete;

private:
    CAN_ADC();
    const float tension_Ref = 5.0;
    const uint16_t adcResolution = 1023;
};

#endif // CAN_ADC_H
