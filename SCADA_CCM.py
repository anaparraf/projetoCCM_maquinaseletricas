# Imports necessários para
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSlider
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial

## Insira aqui a porta COM encontrada no programa anterior
PortaSerial_SM = "COM13"
Ser_SM = serial.Serial(PortaSerial_SM, 115200)
"""
Classe Principal Onde serão desenvolvidas as atividades do CCM
"""

stylesheet_window = """
    TelaPrincipalCCM {
        background-image: url("Factory_floor.jpeg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
stylesheet_big_label = """
        background-color: black;
        border: 1px solid white; 
        font-size: 50px;
        color: white;
        alignment: center;
"""
stylesheet_small_label = """
        background-color: yellow;
        border: 1px solid black; 
        font-size: 25px;
        alignment: center;
"""
stylesheet_enable_and_dir_button = """
        background-color: white;
        border: 5px solid black; 
        border-radius: 50px;
        alignment: center;
"""
stylesheet_speed_slider = """
        background-color: white;
        border-top: 2px solid black;
        border-bottom: 2px solid black;
"""
stylesheet_label1_slider = """
        background-color: white;
        border-top: 2px solid black;
        border-left: 2px solid black;
        border-bottom: 2px solid black; 
        font-size: 25px;
        alignment: center;
"""
stylesheet_label2_slider = """
        background-color: white;
        border-top: 2px solid black;
        border-right: 2px solid black;
        border-bottom: 2px solid black; 
        font-size: 25px;
        alignment: center;
"""

class TelaPrincipalCCM(QMainWindow):
    def __init__(self):
        super().__init__()
        # Definindo as dimensões da tela principal
        self.setGeometry(0, 35, 1920, 995)
        # Definindo qual o título que aparecerá em nossa tela
        self.setWindowTitle("MEA - Centro de Controle de Motor - Motor de Passo e BLDC")
        self.setWindowIcon(QIcon('DC_motor.png'))
        # Função que irá inicializar os widgets na tela
        self.setStyleSheet(stylesheet_window)
        self.InicializarElementos()

    def InicializarElementos(self):
    # MOTOR DE PASSO.
        # Imagem do motor de passo.
        self.stepper_motor_image = QLabel(self)
        self.pixmap = QPixmap('Stepper_motor.png')
        self.pixmap_scaled = self.pixmap.scaled(100,100)
        self.stepper_motor_image.setPixmap(self.pixmap_scaled)
        self.stepper_motor_image.resize(self.pixmap_scaled.width(),self.pixmap_scaled.height())
        self.stepper_motor_image.move(50, 10)
        # Título do motor.
        self.message_motor_SM = QLabel('STEPPER MOTOR', self)
        self.message_motor_SM.setAlignment(Qt.AlignCenter)
        self.message_motor_SM.resize(500, 100)
        self.message_motor_SM.setStyleSheet(stylesheet_big_label)
        self.message_motor_SM.move(200, 10)

        # Título do comando ENABLE.
        self.message_enable_SM = QLabel('ENABLE/DISABLE', self)
        self.message_enable_SM.setAlignment(Qt.AlignCenter)
        self.message_enable_SM.resize(250, 50)
        self.message_enable_SM.setStyleSheet(stylesheet_small_label)
        self.message_enable_SM.move(325, 125)
        ## Criando um elemento Botão para ligar e desligar o motor
        self.But_Toggle_Motor_SM = QPushButton(parent=self)
        self.But_Toggle_Motor_SM.setIcon(QIcon('OFF_button.png'))
        self.But_Toggle_Motor_SM.setIconSize(QSize(100, 100))
        self.But_Toggle_Motor_SM.setStyleSheet(stylesheet_enable_and_dir_button)
        self.But_Toggle_Motor_SM.setMinimumHeight(100)
        self.But_Toggle_Motor_SM.setMinimumWidth(100)
        self.But_Toggle_Motor_SM.move(400, 185)
        # Definir que o botão é do tipo Toggle, ou seja, podemos clicar e ele mantém seu valor
        self.But_Toggle_Motor_SM.setCheckable(True)
        # Definindo que quando o botão for clicado vamos rodar a função ToggleMotor
        self.But_Toggle_Motor_SM.clicked.connect(self.ToggleMotor_SM)

        # Título do comando DIR.
        self.message_dir_SM = QLabel('CHANGE DIR.', self)
        self.message_dir_SM.setAlignment(Qt.AlignCenter)
        self.message_dir_SM.resize(250, 50)
        self.message_dir_SM.setStyleSheet(stylesheet_small_label)
        self.message_dir_SM.move(325, 300)
        ## Criando um elemento Botão para mudar sentido de rotação do motor.
        self.But_Dir_Motor_SM = QPushButton(parent=self)
        self.But_Dir_Motor_SM.setIcon(QIcon('DIR_0_button.png'))
        self.But_Dir_Motor_SM.setIconSize(QSize(100, 100))
        self.But_Dir_Motor_SM.setStyleSheet(stylesheet_enable_and_dir_button)
        self.But_Dir_Motor_SM.setMinimumHeight(100)
        self.But_Dir_Motor_SM.setMinimumWidth(100)
        self.But_Dir_Motor_SM.move(400, 360)
        # Definir que o botão é do tipo Toggle, ou seja, podemos clicar e ele mantém seu valor
        self.But_Dir_Motor_SM.setCheckable(True)
        # Definindo que quando o botão for clicado vamos rodar a função ChangeRotMotor
        self.But_Dir_Motor_SM.clicked.connect(self.ChangeRotMotor_SM)

        # Título do comando SPEED.
        self.message_speed_SM = QLabel('CHANGE SPEED', self)
        self.message_speed_SM.setAlignment(Qt.AlignCenter)
        self.message_speed_SM.resize(250, 50)
        self.message_speed_SM.setStyleSheet(stylesheet_small_label)
        self.message_speed_SM.move(325, 515)
        ## Criando um elemento Slider que controla a velocidade do motor
        self.Sli_Speed_Motor_SM = QSlider(parent=self) 
        self.Sli_Speed_Motor_SM.setOrientation(Qt.Horizontal) 
        self.Sli_Speed_Motor_SM.setGeometry(QRect(50, 50, 500, 100)) 
        self.Sli_Speed_Motor_SM.setStyleSheet(stylesheet_speed_slider)        
        self.Sli_Speed_Motor_SM.setMinimum(0)
        self.Sli_Speed_Motor_SM.setMaximum(9)
        self.Sli_Speed_Motor_SM.setValue(0)
        self.Sli_Speed_Motor_SM.setTickPosition(QSlider.TicksBelow)
        self.Sli_Speed_Motor_SM.setTickInterval(1)
        self.Sli_Speed_Motor_SM.move(200, 600)
        # Rótulo do slider 1.
        self.label_speed1_SM = QLabel('MIN.', self)
        self.label_speed1_SM.setAlignment(Qt.AlignCenter)
        self.label_speed1_SM.resize(75, 100)
        self.label_speed1_SM.setStyleSheet(stylesheet_label1_slider)
        self.label_speed1_SM.move(125, 600)
        # Rótulo do slider 2.
        self.label_speed2_SM = QLabel('MAX.', self)
        self.label_speed2_SM.setAlignment(Qt.AlignCenter)
        self.label_speed2_SM.resize(75, 100)
        self.label_speed2_SM.setStyleSheet(stylesheet_label2_slider)
        self.label_speed2_SM.move(700, 600)
        # Definindo que quando o slider mudar de valor vamos rodar a função SendSerial
        self.Sli_Speed_Motor_SM.valueChanged.connect(self.SendSerial_SM)

    def ToggleMotor_SM(self, Clicado):
        if Clicado:
            command = "A"
            Ser_SM.write(b"A") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Toggle_Motor_SM.setIcon(QIcon('ON_button.png'))
            Ser_SM.write(speed)
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "a"
            Ser_SM.write(b"a") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Toggle_Motor_SM.setIcon(QIcon('OFF_button.png'))
            Ser_SM.write(speed)
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))

    def ChangeRotMotor_SM(self, Clicado):
        if Clicado:
            command = "D"
            Ser_SM.write(b"D") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Dir_Motor_SM.setIcon(QIcon('DIR_0_button.png'))
            Ser_SM.write(speed)
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "d"
            Ser_SM.write(b"d") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Dir_Motor_SM.setIcon(QIcon('DIR_1_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
    
    def SendSerial_SM(self, value):
        Ser_SM.write(bytes(str(int(value)), "utf-8"))


# Parte que inicia a tela conforme o que é descrito no __init__
app = QApplication(sys.argv)
window = TelaPrincipalCCM()
window.show()
app.exec()