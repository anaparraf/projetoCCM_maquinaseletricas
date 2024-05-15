#include 'mbed.h'
#include <stdio.h>
#include <string.h>
Serial ser(USBTX, USBRX); // Saída serial
// Definição I/O
DigitalOut EN_A(D2);
DigitalOut IN1_A(D5);
DigitalOut IN2_A(D4);
DigitalOut EN_B(A4);
DigitalOut IN1_B(A0);
DigitalOut IN2_B(A1); 
InterruptIn liga(USER_BUTTON); // Botão de ligar (botão do usuário)

// Criação de variáveis assistentes
bool onoff = 0; // Variavel booleana que em 0 define o estado desligado e em 1 o ligado
bool dir = 0; // Variavel booleana que em 0 define um sentido de rotação do motor de passo e em 1 o outro sentido
char leitura; // Le o que foi escrito na porta serial
int espera; // Define o tempo em ms entre as fases (vai de 0 a 9 sendo 0 a velocidade máxima e 9 a mínima)
void switch_fase() {
  if (onoff == 0) { // Se onoff for zero, ou seja, o botão do usuário não foi pressionado ou não foi escrito A na entrada serial ou foi escrito a na entrada serial, o motor de passo não liga ou desliga
  }
  if (onoff == 1) { // Se onoff for 1, ou seja, o botão do usuário foi pressionado ou A foi escrito na entrada serial, o motor de passo liga
    if (dir == 1) { // Se dir for 1, o sentido de rotação do motor é  anti-horário
        EN_A = 1;
        IN1_A = 1; 
        IN2_A = 0;
        EN_B = 0;
        IN1_B = 1; 
        IN2_B = 0;
        wait_ms(espera);
        EN_A = 0;
        IN1_A = 0; IN2_A = 1;
        EN_B = 1;
        IN1_B = 1; IN2_B = 0;
        wait_ms(espera);
        EN_A = 1;
        IN1_A = 0; IN2_A = 1;
        EN_B = 0;
        IN1_B = 0; IN2_B = 1;
        wait_ms(espera);
        EN_A = 0;
        IN1_A = 1; IN2_A = 0;
        EN_B = 1;
        IN1_B = 0; IN2_B = 1;
        wait_ms(espera);
      }
    
    if (dir == 0) { // Se dir for 0, o sentido de rotação do motor é  horário
        EN_A = 0;
        IN1_A = 1; IN2_A = 0;
        EN_B = 1;
        IN1_B = 0; IN2_B = 1;
        wait_ms(espera);
        EN_A = 1;
        IN1_A = 0; IN2_A = 1;
        EN_B = 0;
        IN1_B = 0; IN2_B = 1;
        wait_ms(espera);
        EN_A = 0;
        IN1_A = 0; IN2_A = 1;
        EN_B = 1;
        IN1_B = 1; IN2_B = 0;
        wait_ms(espera);
        EN_A = 1;
        IN1_A = 1; 
        IN2_A = 0;
        EN_B = 0;
        IN1_B = 1; 
        IN2_B = 0;
        wait_ms(espera);
      }
    }
}
void EN_ABLE() { onoff = !onoff; } // Muda o valor de onoff se o botão do usuário for acionado (liga/desliga)

void callback(){leitura = ser.getc();}
int main() {
    ser.baud(115200);
    ser.attach(&callback);
    liga.rise(&EN_ABLE); // Chama a função EN_ABLE se o botão do usuário for pressionado
    while (1) {
        switch (leitura){
            case 'A': onoff = 1; break; // Liga o motor
            case 'a': onoff = 0; break; // Desliga o motor
            case 'D': dir = 1; break; // Sentido anti-horário de rotação
            case 'd': dir = 0; break; // Sentido horário de rotação
            case '0': espera = 10; break;// wait_ms (espera) = 10 ms (velocidade máxima)
            case '1': espera = 20; break;// wait_ms (espera) = 20 ms
            case '2': espera = 30; break;// wait_ms (espera) = 30 ms
            case '3': espera = 40; break;// wait_ms (espera) = 40 ms
            case '4': espera = 50; break;// wait_ms (espera) = 50 ms
            case '5': espera = 60; break;// wait_ms (espera) = 60 ms
            case '6': espera = 70; break;// wait_ms (espera) = 70 ms
            case '7': espera = 80; break;// wait_ms (espera) = 80 ms
            case '8': espera = 90; break;// wait_ms (espera) = 90 ms
            case '9': espera = 100; break;// wait_ms (espera) = 100 ms (velocidade mínima)
        }
            switch_fase(); // Chama a função switch_fase
    }
}
