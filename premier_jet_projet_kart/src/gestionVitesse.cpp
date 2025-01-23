#include "gestionVitesse.h"

gestionVitesse::gestionVitesse(int *_nbtour, uint32_t *_cptPF) : monPID(K_P, K_I, K_D, periodeEchantillonageS, PWM_MAX, PWM_MIN)
{
    cptPF = _cptPF;
    nbTour = _nbtour;
}

void gestionVitesse::lierPotToVitN(CAN_ADC::ADC_Channel channel)
{
    OCR1A = (PWM_MAX * adc.read(channel)) / (ADC_MAX);
}

void gestionVitesse::lierPotToVitE(CAN_ADC::ADC_Channel channel)
{
    OCR1A = (PWM_MAX * (adc.read(channel)*adc.read(channel))) / ((ADC_MAX)*(ADC_MAX));
}

void gestionVitesse::lierPotToVitS(CAN_ADC::ADC_Channel channel)
{
    OCR1A = PWM_MAX * sin(2.0 * M_PI * 0.00025 * (float)ADC_MAX);
}

void gestionVitesse::get_string(char *buffer)
{
    float temps = time.get_timeS();
    char buffer0[20];
    char buffer1[35];
    char buffer2[20];
    sprintf(buffer1, "nb tour from class : %d nb imp : %d", nbtourBuff, nbImp);
    dtostrf(vitessekmh, 6, 3, buffer0);
    dtostrf(temps, 6, 3, buffer2);
    sprintf(buffer, "%35s vitesse du kart :%-7s km/h temps entre les impulsions : %7s", buffer1, buffer0, buffer2);
}

float gestionVitesse::get_vitesse()
{
    float temps = time.get_timeS() - tempsPre;
    if (temps >= 0.2)
    {
        tempsPre = time.get_timeS();

        nbImp = TCNT0;
        TCNT0 = 0;
        nbtourBuff = *nbTour;
        *nbTour = 0;

        float distImp = (tourRoueM * ((float)nbImp)) / (float)impRoue;
        vitessekmh = ((distImp + (float)(nbtourBuff)*tourRoueM) / temps) * 3.6;
    }
    return vitessekmh;
}

void gestionVitesse::regulation(int consigneV)
{
    float vitesse = get_vitesse();
    int16_t PWM_COMMANDE = monPID.calculerCommande(consigneV, vitesse);
    if(PWM_COMMANDE == -1){
        return;
    }
    else if (PWM_COMMANDE == 0)
    {
        serial.puts("cmd1: ");
        serial.printFloat((float)PWM_COMMANDE);
        serial.puts("vit1 : ");
        serial.printFloat(vitesse);
        OCR1A = PWM_COMMANDE;
        TCCR1A &= ~(1 << COM1A1);
        DDRB &= ~(1 << PB1);
    }
    else if (PWM_COMMANDE > 0) // pour ne pas prendre en compte -1 quand fréquence d'echantillonage pas respectée
    {
        serial.puts("                    cmd2: ");
        serial.printFloat((float)PWM_COMMANDE);
        serial.puts("                   vit2 : ");
        serial.printFloat(vitessekmh);
        TCCR1A |= (1 << COM1A1);
        DDRB |= (1 << PB1);
        OCR1A = PWM_COMMANDE;
    }
}

void gestionVitesse::limitateur(int limiteV)
{
    float vitesse = get_vitesse();
    if (vitesse > limiteV)
    {
        OCR1A = PWM_MIN;
    }
    else
    {
        lierPotToVitN(CAN_ADC::ADC1);
    }
}