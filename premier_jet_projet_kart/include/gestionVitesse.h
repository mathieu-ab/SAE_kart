#ifndef GESTIONVITESSE_H
#define GESTIONVITESSE_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "CAN_ADC.h"
#include "Timer2.h"
#include "PID.h"
#include "USART.h"

class gestionVitesse
{
public:
    gestionVitesse(int *_nbtour, uint32_t *_cptPF);
    void lierPotToVitN(CAN_ADC::ADC_Channel channel);
    void lierPotToVitE(CAN_ADC::ADC_Channel channel);
    void lierPotToVitS(CAN_ADC::ADC_Channel channel);
    void get_string(char *buffer);
    float get_vitesse();

    void regulation(int consigneV); // a faire plus tard !!!
    void limitateur(int limiteV);   // a faire plus tard !!!

private:
    const float PWM_MAX = 1600.0;              // valeur max de la PWM timer 1
    const float PWM_MIN = 0.0;                // valeur min de la PWM timer 1
    const float ADC_MAX = 1023.0;             // valeur max de l'adc
    const float tourRoueM = 0.83;             // circonférence de la roue en metre
    const uint8_t impRoue = 32;               // nombre d'impulsion de la roue crantée
    const float periodeEchantillonageS = 0.01; // période déchantillonage en seconde pour régulation vitesse
    const float K_P = 12;                      // Gain proportionnel 6
    const float K_I = 0.5;                      // Gain intégral 2
    const float K_D = 5;                     // Gain dérivé 1

    CAN_ADC &adc = CAN_ADC::getInstance();
    Timer2 &time = Timer2::getInstance();
    USART &serial = USART::getInstance();
    PID monPID;

    int nbtourBuff = 0;
    int nbImp = 0;
    int *nbTour;
    uint32_t *cptPF;
    float vitessekmh = 0;
    double tempsPre = 0;
};

#endif // GESTIONVITESSE_H