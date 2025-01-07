#include "Timer1.h"

Timer1::Timer1()
{
  // configurer les MLI des deux ventilateur
  DDRB |= (1 << PB1);
  DDRB |= (1 << PB2);
  TCCR1A = 0;
  TCCR1B = 0;
  // timer1 en mode 14
  TCCR1B |= (1 << WGM13) | (1 << WGM12);
  TCCR1A |= (1 << WGM11);
  // valeur du prédiviseur
  TCCR1B |= (1 << CS10);
  ICR1 = 1600;
  // générer le signal MLI sur la broche OC1A ou OC1B (bits COM1xx dans le registre TCCR1A)
  TCCR1A |= (1 << COM1A1);
  TCCR1A |= (1 << COM1B1);
  OCR1B = 0;
  OCR1A = 0;
}