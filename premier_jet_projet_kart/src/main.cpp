#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "USART.h"
#include "Timer0.h"
#include "Timer1.h"
#include "CAN_ADC.h"
#include "pompe.h"
#include "gestionVitesse.h"


#define BAUD_RATE 500000                             // baud rate de la liaison serie
#define UBRR_VALUE ((F_CPU / (8UL * BAUD_RATE)) - 1) // Mode double vitesse

void nb_tourFCT();

int nb_tour = 0;
volatile int flag_USART = 0;
volatile int flag_TIMER0 = 0;

USART serial(UBRR_VALUE);
Timer0 compteur;
Timer1 MLI;
CAN_ADC adc;
pompe maPompe(&adc);
gestionVitesse maVitesse(&adc, &nb_tour);

// Interruption pour la réception sur USART0
ISR(USART_RX_vect)
{
  flag_USART = 1;
}
// interruption pour la comparaison des impulsions de la roue crantée
ISR(TIMER0_COMPA_vect)
{
  TCNT0 = 0;
  nb_tour++;
}

int main(void)
{
  sei();
  char buffer[100];
  while (1)
  {
    maVitesse.get_string(buffer);
    serial.putsln(buffer);
    maVitesse.lierPotToVit(CAN_ADC::ADC0);
    maPompe.get_String(buffer, 100);
    serial.putsln(buffer);
    maPompe.regulation(100);
    nb_tourFCT();
    adc.get_string(buffer, CAN_ADC::ADC0);
    serial.putsln(buffer);
    maPompe.get_stringR(buffer, CAN_ADC::ADC1);
    serial.putsln(buffer);
    _delay_ms(10);
  }
}

void nb_tourFCT()
{
  char buffer[20];
  sprintf(buffer, "nombre de tour :  %d", nb_tour);
  serial.putsln(buffer);
}