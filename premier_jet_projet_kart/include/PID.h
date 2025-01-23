#ifndef PID_H
#define PID_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

#include "Timer2.h"

class PID
{
public:
    PID(float _P, float _I, float _D, float _periodeEchantillonageS, float _sortieMax, float _sortieMin);
    int calculerCommande(float vitesse_cible, float vitesse_mesuree);

private:
    Timer2 &time = Timer2::getInstance();
     float Kp, Ki, Kd;
     float erreurPre = 0;
     float sommeErreurs = 0;
     float tempsPre = 0;
     float periodeEchantillonage;
     int sortieMin, sortieMax;           // Limites de la sortie PID
};

#endif // PID_H
