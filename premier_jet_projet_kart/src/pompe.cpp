#include "pompe.h"

pompe::pompe(CAN_ADC *_adc) : adc(_adc)
{
}

void pompe::regulation(int consigneT)
{
    double temperature = temperatureMoteur();
    uint16_t PWM_COMMANDE = calcul_commande(consigneT, temperature);
    if (PWM_COMMANDE == 0)
    {
        TCCR1A &= ~(1 << COM1B1);
        DDRB &= ~(1 << PB2);
        OCR1B = PWM_COMMANDE;
    }
    else
    {
        TCCR1A |= (1 << COM1B1);
        DDRB |= (1 << PB2);
        OCR1B = PWM_COMMANDE;
    }
}

uint16_t pompe::calcul_commande(uint16_t consigne, uint16_t mesure)
{
    int16_t erreur = mesure - consigne;

    // Partie proportionnelle
    int16_t commande_P = K_P * erreur;

    // Partie dérivée
    int16_t variation_erreur = erreur - erreur_precedente;
    int16_t commande_D = K_D * variation_erreur;

    // Mise à jour de l'erreur précédente
    erreur_precedente = erreur;

    // Somme des commandes P et D
    int16_t commande = commande_P + commande_D;

    // Saturation de la commande
    if (commande < 0)
        commande = 0;
    if (commande > PWM_MAX)
        commande = PWM_MAX;

    return (uint16_t)commande;
}

double pompe::temperatureMoteur()
{
    double tension = adc->get_tension(CAN_ADC::ADC1);
    double r = get_resistancePara(tension);

    for (uint8_t i = 0; i < 8 - 1; i++)
    {
        if (r >= resistance_table[i] && r <= resistance_table[i + 1])
        {
            // Interpolation linéaire
            float t1 = temperature_table[i];
            float t2 = temperature_table[i + 1];
            float r1 = resistance_table[i];
            float r2 = resistance_table[i + 1];
            return t1 + (r - r1) * (t2 - t1) / (r2 - r1);
        }
    }
    return -1;
}

void pompe::get_String(char *buffer, uint16_t consigne)
{
    char tBuffer[50];
    double temperature = temperatureMoteur();
    uint16_t commande = calcul_commande(consigne, temperature);
    dtostrf(temperature, 6, 3, tBuffer);
    sprintf(buffer, "temperature moteur : %5s °C, valeur de la commande : %d", tBuffer, commande);
}

void pompe::get_stringR(char *buffer, CAN_ADC::ADC_Channel channel)
{
    char buffer0[15];
    char buffer1[60];

    double tension = adc->get_tension(channel);
    double resistance = get_resistancePara(tension);
    dtostrf(resistance, 5, 2, buffer0);
    adc->get_string(buffer1, channel);
    sprintf(buffer, "%-52s, Valeur de la thermistance sur ADC%d : %-5s ohms", buffer1, channel, buffer0);
}

double pompe::get_resistancePara(double _tension)
{
    return _tension * rPara / (5 - _tension);
}