#ifndef USART_H
#define USART_H

#include <avr/io.h>

class USART {
public:
    USART(unsigned int UBRR_VALUE);
    void puts(const char *str);
    void putsln(const char *str);
    unsigned char Receive(void);
private:
    void Transmit(unsigned char data);
};

#endif // USART_H
