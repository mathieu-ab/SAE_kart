#include "CAN_ADC.h"

CAN_ADC::CAN_ADC()
{
    // Configurer la tension de référence à AVCC avec un condensateur de découplage sur AREF
    ADMUX |= (1 << REFS0);  // AVCC est la tension de référence
    ADMUX &= ~(1 << REFS1); // Suite à un masquage, le bit REFS1 est à 0

    // Configurer le prescaler à 128 pour l'horloge du CAN
    ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);    // Prescaler de 128
    ADCSRB &= ~(1 << ADTS0) & ~(1 << ADTS1) & ~(1 << ADTS2); // Sélection du mode de démarrage libre

    // Activer le convertisseur analogique-numérique (CAN)
    ADCSRA |= (1 << ADEN); // Activer le CAN
}

uint16_t CAN_ADC::read(ADC_Channel channel)
{
    // Sélectionner la broche (MUX2:0)
    ADMUX = (ADMUX & 0xF8) | (channel & 0x07); // Garder les bits REFS, MUX3 et ADLAR intactes et mettre à jour MUX(0:2) (inutile peut etre supp)
    // Démarrer la conversion
    ADCSRA |= (1 << ADSC);
    // Attendre la fin de la conversion (ADSC devient 0)
    while (ADCSRA & (1 << ADSC))
        ;
    // Retourner la valeur (10 bits)
    return ADC;
}

void CAN_ADC::get_string(char *buffer, ADC_Channel channel)
{
    char buffer0[10]; // variable tampon

    uint16_t adcValue = read(channel);
    double tension = get_tension(channel);
    dtostrf(tension, 6, 3, buffer0);                                                                             // convertion de la valeur float en caractère
    sprintf(buffer, "valeur de l'ADC%d : %d, tension sur l'ADC%d : %5s V", channel, adcValue, channel, buffer0); // mise en forme de la chaine de caractère
}

double CAN_ADC::get_tension(ADC_Channel channel)
{
    uint16_t adcValue = read(channel); // lecture de la valeur du channel ADC
    double tension = (adcValue * tension_Ref) / 1023.0;
    return tension;
}