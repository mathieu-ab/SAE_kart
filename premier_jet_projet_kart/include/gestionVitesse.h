#ifndef GESTIONVITESSE_H
#define GESTIONVITESSE_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

#include "CAN_ADC.h"

class gestionVitesse {
public:
    gestionVitesse(CAN_ADC *_adc, int *_nbtour);
    void lierPotToVit(CAN_ADC::ADC_Channel channel);
    void regulation(int consigneV,long nbtour);
    void get_string(char *buffer);
    
 
private:
    float PWM_MAX = 1600.0;
    float ADC_MAX = 1023.0;
    CAN_ADC *adc;
    int *nbTour;
};

#endif // GESTIONVITESSE_H

