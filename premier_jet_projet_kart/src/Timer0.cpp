#include "Timer0.h"

Timer0::Timer0()
{
  DDRD &= ~(1 << PD4); // pin en entrée
  PORTD |= (1 << PD4); // activation de la pull up interne
  TCCR0A = 0;          // reset registre
  TCCR0B = 0;          /// reset registre

  TCCR0A |= (1 << WGM01);              // mode 3 CTC pour timer 0
  TCCR0B |= (1 << CS00)|(1 << CS01) | (1 << CS02); // mode de clock externe sur front montant du pin T0$

  OCR0A = 31;             // definition du nombre d'impulsion avant interruption
  TIMSK0 = (1 << OCIE0A); // activation de l'interruption de comparaison
  TCNT0 = 0;              // initialisation de la valeur du timer0
}