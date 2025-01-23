#include "PID.h"

PID::PID(float _P, float _I, float _D, float _periodeEchantillonageS, float _sortieMax, float _sortieMin)
{
    Kp = _P;
    Ki = _I;
    Kd = _D;
    periodeEchantillonage = _periodeEchantillonageS;
    sortieMax = _sortieMax;
    sortieMin = _sortieMin;
}

int PID::calculerCommande(float consigne, float mesure)
{
    double tempsActuel = time.get_timeS();
    float dt = (tempsActuel - tempsPre);

    // Vérifier si la période d'échantillonnage est respectée
    if (dt < periodeEchantillonage)
    {
        return -1; // Indique qu'aucun calcul n'a été effectué
    }

    tempsPre = tempsActuel;
    // Calculer les erreurs
    float erreur = consigne - mesure;
    float derivee = (erreur - erreurPre) / dt;
    sommeErreurs += erreur * dt;

    // Anti-windup : Limiter l'accumulation de somme_erreurs si sortie est saturée
    /*if ((sommeErreurs < sortieMax) && (sommeErreurs > sortieMin))
    {
        sommeErreurs += erreur * dt;
    }*/

    /*sommeErreurs =+ (Ki * erreur * dt);
    if(sommeErreurs> sortieMax) sommeErreurs= sortieMax;
    else if(sommeErreurs< sortieMin) sommeErreurs= sortieMin;*/

    // Calculer la sortie du PID
    float sortie = Kp * erreur + Ki * sommeErreurs + Kd * derivee;

    // Limiter la sortie entre les bornes
    if (sortie < sortieMin)
        sortie = sortieMin;
    if (sortie > sortieMax)
        sortie = sortieMax;

    erreurPre = erreur;
    return (int)sortie;
}