#include "USART.h"

USART::USART(unsigned int UBRR_VALUE)
{
    UBRR0H = (uint8_t)(UBRR_VALUE >> 8);
    UBRR0L = (uint8_t)UBRR_VALUE;
    UCSR0A |= (1 << U2X0);                  // Active le mode double vitesse pour 115200 baud ou plus
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);   // Activation du récepteur et du transmetteur
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00); // Configuration du format de trame : 8 bits de données, 1 bit de stop
}

// Transmission via USART
void USART::Transmit(unsigned char data)
{
    while (!(UCSR0A & (1 << UDRE0)))
        ;        // Attendre que le buffer de transmission soit vide
    UDR0 = data; // Charger les données à envoyer dans le buffer
}


// Fonction pour envoyer une chaîne de caractères via USART
void USART::puts(const char *str)
{
    while (*str)
    {                   // Tant que le caractère pointé par str n'est pas nul
        Transmit(*str); // Transmettre le caractère
        str++;          // Passer au caractère suivant
    }
}

// Fonction pour envoyer une chaîne de caractères suivie d'un saut de ligne via USART
void USART::putsln(const char *str)
{
    puts(str);      // Envoyer la chaîne de caractères
    Transmit('\n'); // Envoyer un saut de ligne
    Transmit('\r'); // Envoyer un retour chariot
}

unsigned char USART::Receive(void)
{
    /* Attente des données à recevoir */
    while (!(UCSR0A & (1 << RXC0)))
        ;
    /* Récupération et renvoi des données reçues */
    return UDR0;
}

int USART::receiveNumb()
{
   char buffer0[4]={0,0,0,0};
    int i = 0;
 while (1)
      {
       char bufferReceive = Receive();
       if(bufferReceive == 'f') break;
       buffer0[i] = bufferReceive;
       i++;
      }
      return atoi(buffer0);
}

void USART::printInt(int _nb)
{
    char buffer[10];
    itoa(_nb, buffer, 10);
    putsln(buffer);
}

void USART::printFloat(float _nb)
{
    char buffer[10];
    dtostrf(_nb,6,3,buffer);
    putsln(buffer);
}