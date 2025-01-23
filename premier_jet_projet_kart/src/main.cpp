#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>

#include "USART.h"
#include "Timer0.h"
#include "Timer1.h"
#include "Timer2.h"
#include "CAN_ADC.h"
#include "pompe.h"
#include "gestionVitesse.h"

#define BAUD_RATE 9600                               // baud rate de la liaison serie
#define UBRR_VALUE ((F_CPU / (8UL * BAUD_RATE)) - 1) // Mode double vitesse

enum Etat_MAE
{
  Mode_normal,
  Mode_regulateur,
  Mode_limitateur,
  Mode_eco,
  Mode_sport,
  TEST
};

Etat_MAE Etat = TEST;
int nb_tour = 0;
uint32_t cptPF = 0;
int valeurRegu;

USART &serial = USART::getInstance(UBRR_VALUE);
Timer0 &compteur = Timer0::getInstance();
Timer1 &MLI = Timer1::getInstance();
Timer2 &time = Timer2::getInstance(&cptPF);
CAN_ADC &adc = CAN_ADC::getInstance();

pompe maPompe;
gestionVitesse maVitesse(&nb_tour, &cptPF);

void changementEtat();

// interruption pour la comparaison des impulsions de la roue crantée
ISR(TIMER0_COMPA_vect)
{
  TCNT0 = 0;
  nb_tour++;
}

ISR(TIMER2_OVF_vect)
{
  cptPF++;
}

int main(void)
{
  char buffer[100];
  double tempsPre = 0;
  float temps = 0;
  DDRD &= ~(1 << PD5); // pin en entrée
  PORTD |= (1 << PD5); // activation de la pull up interne

  sei();
  while (1)
  {
    switch (Etat)
    {
    case Mode_normal:
      changementEtat();
      temps = time.get_timeS() - tempsPre;
      if (temps >= 5)
      {
        float vit = maVitesse.get_vitesse();
        tempsPre = time.get_timeS();
        serial.putsln("mode normal");
        serial.printFloat(vit);
      }
      maVitesse.lierPotToVitN(CAN_ADC::ADC1);
      // maPompe.regulation(100);

      break;

    case Mode_limitateur:
      changementEtat();
      temps = time.get_timeS() - tempsPre;
      if (temps >= 5)
      {
        float vit = maVitesse.get_vitesse();
        tempsPre = time.get_timeS();
        serial.putsln("mode limitateur");
        serial.printFloat(vit);
      }
      maVitesse.limitateur(10);
      // maPompe.regulation(100);
      break;

    case Mode_regulateur:
      changementEtat();
      maVitesse.regulation(valeurRegu);
      temps = time.get_timeS() - tempsPre;
      if (temps >= 0.5)
      {
        float vit = maVitesse.get_vitesse();
        tempsPre = time.get_timeS();
        serial.putsln("mode regulateur");
        serial.printInt(valeurRegu);
        serial.printFloat(vit);
      }
      if(bit_is_set(PIND,PD5)){
        Etat = Mode_normal;
      }
      // maPompe.regulation(100);
      break;

    case Mode_eco:
      changementEtat();
      temps = time.get_timeS() - tempsPre;
      if (temps >= 0.5)
      {
        float vit = maVitesse.get_vitesse();
        tempsPre = time.get_timeS();
        serial.putsln("mode eco");
        serial.printFloat(vit);
      }
       maVitesse.lierPotToVitE(CAN_ADC::ADC1);
      // maPompe.regulation(100);
      break;

    case Mode_sport:
      changementEtat();
      temps = time.get_timeS() - tempsPre;
      if (temps >= 0.5)
      {
        float vit = maVitesse.get_vitesse();
        tempsPre = time.get_timeS();
        serial.putsln("mode sport");
        serial.printFloat(vit);
      }
      maVitesse.lierPotToVitS(CAN_ADC::ADC1);
      // maPompe.regulation(100);
      break;

    case TEST:
      changementEtat();
      serial.putsln("mode TEST");
      /*temps = time.get_timeS() - tempsPre;
      maVitesse.get_vitesse();
      if (temps >= 0.5)
      {
        tempsPre = time.get_timeS();
        maVitesse.get_string(buffer);
        serial.putsln(buffer);
        //maPompe.get_String(buffer, 100);
        //serial.putsln(buffer);
        //adc.get_string(buffer, CAN_ADC::ADC0);
        //serial.putsln(buffer);
        //maPompe.get_stringR(buffer, CAN_ADC::ADC1);
        //serial.putsln(buffer);
      }*/
      // maPompe.regulation(100);
      maVitesse.regulation(10);
      // maVitesse.lierPotToVit(CAN_ADC::ADC1);
      break;

    default:
      break;
    }
  }
  return 0;
}

void changementEtat()
{
  char bufferReceive = 0;
  if (bit_is_set(UCSR0A, RXC0))
  {
    bufferReceive = serial.Receive();

    if (bufferReceive == 'r')
    {
      valeurRegu = maVitesse.get_vitesse();
      Etat = Mode_regulateur;
    }
    else if (bufferReceive == 'l')
    {
      Etat = Mode_limitateur;
    }
    else if (bufferReceive == 'c')
    {
      Etat = Mode_normal;
    }
    else if (bufferReceive == 'e')
    {
      Etat = Mode_eco;
    }
    else if (bufferReceive == 's')
    {
      Etat = Mode_sport;
    }
    else if (bufferReceive == 'n')
    {
      valeurRegu = serial.receiveNumb();
    }
  }
}