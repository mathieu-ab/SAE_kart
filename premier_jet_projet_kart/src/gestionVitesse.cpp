#include "gestionVitesse.h"

gestionVitesse::gestionVitesse(CAN_ADC *_adc, int *_nbtour): adc(_adc)
{
    nbTour = _nbtour; 
}

void gestionVitesse::lierPotToVit(CAN_ADC::ADC_Channel channel)
{
    OCR1A = (PWM_MAX * adc->read(channel)) / (ADC_MAX);
}

void gestionVitesse::regulation(int consigneV, long nbtour)
{
}

void gestionVitesse::get_string(char *buffer)
{
    sprintf(buffer,"nb tour from class : %d", *nbTour);
    if(*nbTour == 10){
        *nbTour = 0;
    }
}
