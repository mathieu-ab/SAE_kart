#ifndef USART_H
#define USART_H

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>

class USART
{
public:
    // Méthode statique pour accéder à l'instance unique
    static USART &getInstance(unsigned int UBRR_VALUE = 0)
    {
        static USART instance(UBRR_VALUE); // Instance unique
        return instance;
    }

    void puts(const char *str);
    void putsln(const char *str);
    unsigned char Receive(void);
    void Transmit(unsigned char data);
    int receiveNumb();
    void printInt(int _nb);
    void printFloat(float _nb);

    // Suppression des constructeurs de copie et de l'opérateur d'affectation
    USART(const USART &) = delete;
    USART &operator=(const USART &) = delete;

private:
    USART(unsigned int UBRR_VALUE);
};

#endif // USART_H
