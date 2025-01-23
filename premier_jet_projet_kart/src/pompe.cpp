#include "pompe.h"

pompe::pompe() : monPID(K_P, 0, K_D, periodeEchantillonageS, PWM_MAX, PWM_MIN)
{
}

void pompe::regulation(int consigneT)
{
    double temperature = temperatureMoteur();
    int PWM_COMMANDE = monPID.calculerCommande(-consigneT, -temperature);

    if (PWM_COMMANDE == 0)
    {
        /*serial.puts("cmd1: ");
        serial.printFloat((float)PWM_COMMANDE);
        serial.puts("vit1 : ");
        serial.printFloat(temperature);*/
        TCCR1A &= ~(1 << COM1B1);
        DDRB &= ~(1 << PB2);
        OCR1B = PWM_COMMANDE;
    }
    else if (PWM_COMMANDE > 0) // pour ne pas prendre en compte -1 quand fréquence d'echantillonage pas respectée
    {
        serial.puts("cmd1: ");
        serial.printFloat((float)PWM_COMMANDE);
        serial.puts("vit1 : ");
        serial.printFloat(temperature);
        TCCR1A |= (1 << COM1B1);
        DDRB |= (1 << PB2);
        OCR1B = PWM_COMMANDE;
    }
}

double pompe::temperatureMoteur()
{
    double tension = adc.get_tension(CAN_ADC::ADC0);
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
    dtostrf(temperature, 6, 3, tBuffer);
    sprintf(buffer, "temperature moteur : %5s °C, valeur de la commande : %d", tBuffer, OCR1B);
}

void pompe::get_stringR(char *buffer, CAN_ADC::ADC_Channel channel)
{
    char buffer0[15];
    char buffer1[60];

    double tension = adc.get_tension(channel);
    double resistance = get_resistancePara(tension);
    dtostrf(resistance, 5, 2, buffer0);
    adc.get_string(buffer1, channel);
    sprintf(buffer, "%-52s, Valeur de la thermistance sur ADC%d : %-5s ohms", buffer1, channel, buffer0);
}

double pompe::get_resistancePara(double _tension)
{
    return _tension * rPara / (5 - _tension);
}