#include "mbed.h"
// pinos placa IHM07M1 - Usa para PWM
PwmOut IN_1 (PA_8);
PwmOut IN_2 (PA_9);
PwmOut IN_3 (PA_10);
// pinos placa IHM07M1 ENABLE
DigitalOut EN_1 (PC_10); 
DigitalOut EN_2 (PC_11);
DigitalOut EN_3 (PC_12);

// InterruptIn botao(USER_BUTTON); //botão de usuário
// AnalogIn pot(PB_1); //potênciometro

// bool liga = 0;  //variável booleana que altera 
// void liga_desliga_motor(){  // função que altera a variável 'liga' quando a borda de subida do botão do usuário é acionado
//     liga =! liga;  //inverte 'liga'
// }

bool direcao = 0;
float tempo = 8000;
bool MotorOn = 0;

void aciona(){
    if (MotorOn == 1){
    if (direcao ==0){
    //---------- momento 1-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(0); // Braço 3 (C)
        // in - chave 
        IN_1.write(1); 
        IN_2.write(0); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 2-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(0); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(1); 
        IN_2.write(0); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 3-------------
        // enable do braço
        EN_1.write(0); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(1); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 4-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(0); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(1); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 5-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(0); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(0); 
        IN_3.write(1); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 6-------------
        // enable do braço
        EN_1.write(0); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(0); 
        IN_3.write(1); 

        wait_us(tempo); // espera tempo em micro segundos
    }
    if (direcao ==1){
        //---------- momento 6-------------
        // enable do braço
        EN_1.write(0); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(0); 
        IN_3.write(1); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 5-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(0); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(0); 
        IN_3.write(1); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 4-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(0); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(1); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 3-------------
        // enable do braço
        EN_1.write(0); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(1); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
        //---------- momento 2-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(0); // Braço 2 (B)
        EN_3.write(1); // Braço 3 (C)
        // in - chave 
        IN_1.write(1); 
        IN_2.write(0); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
    //---------- momento 1-------------
        // enable do braço
        EN_1.write(1); // Braço 1 (A)
        EN_2.write(1); // Braço 2 (B)
        EN_3.write(0); // Braço 3 (C)
        // in - chave 
        IN_1.write(1); 
        IN_2.write(0); 
        IN_3.write(0); 

        wait_us(tempo); // espera tempo em micro segundos
    }}
    if (MotorOn==0){
        EN_1.write(0); // Braço 1 (A)
        EN_2.write(0); // Braço 2 (B)
        EN_3.write(0); // Braço 3 (C)
        // in - chave 
        IN_1.write(0); 
        IN_2.write(0); 
        IN_3.write(0); 
    }
}

Serial ser(USBTX, USBRX);

char leitura;

void callback(){leitura = ser.getc();}
int main() {

    ser.baud(115200);
    ser.attach(&callback);

    // botao.rise(&liga_desliga_motor); //aciona função 'liga_desliga_motor' na borda de subida
    // float v_potenciometro; // Cria a variável ‘v_potenciometro’ que corresponde ao valor atual lido no potenciômetro

    // configurações iniciais
    EN_1.write(0); // Braço 1 (A)
    EN_2.write(0); // Braço 2 (B)
    EN_3.write(0); // Braço 3 (C)
    IN_1.period_ms(1); // PWM = 1 ms
    IN_2.period_ms(1); // PWM = 1 ms
    IN_3.period_ms(1); // PWM = 1 ms
    IN_1.write(0); // PWM com valor 0%
    IN_2.write(0); // PWM com valor 0%
    IN_3.write(0); // PWM com valor 0%


    while (1) {

        aciona();

        // if (ser.readable()) {
        //     leitura = ser.getc();
            switch(leitura){

                case 'A': MotorOn = 1; break;
                
                case 'a': MotorOn = 0; break;

                case 'D': direcao =0; break; // horario
                
                case 'd': direcao =1; break;  // anti horario
                
                case '0': tempo = 5000; break;
                
                case '1': tempo = 6000; break; 

                case '2': tempo = 7000; break; 

                case '3': tempo = 8000; break; 
                
                case '4': tempo = 9000; break; 

                case '5': tempo = 10000; break; 

                case '6': tempo = 11000; break; 

                case '7': tempo = 12000; break; 

                case '8': tempo = 13000; break; 

                case '9': tempo = 14000; break;                   
            }
}
}
