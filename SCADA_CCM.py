# Importando bibliotecas e módulos necessários.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSlider
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import serial


#                                 CONFIGURAÇÕES INICIAIS
# Porta de comunicação com o motor de passo.
PortaSerial_SM = "COM21"
Ser_SM = serial.Serial(PortaSerial_SM, 115200)
# Porta de comunicação com o motor BLDC.
PortaSerial_BLDC = "COM22"
Ser_BLDC = serial.Serial(PortaSerial_BLDC, 115200)
# Variável assistente para o espelhamento horizontal de elementos repetidos (de motor de passo para BLDC).
x_displacement = 1020 

# Stylesheets usados na configuração visual de certos elementos.
stylesheet_window = """
    TelaPrincipalCCM {
        border-image: url("Factory_floor.jpeg"); 
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
        font-style: italic;
"""
stylesheet_small_label = """
        background-color: yellow;
        border: 1px solid black; 
        font-size: 25px;
        alignment: center;
"""
stylesheet_enable_and_dir_button_and_ES_sin = """
        background-color: white;
        border: 5px solid black; 
        border-radius: 50px;
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
stylesheet_ES = """
        background-color: red;
        border: 1px solid black; 
        font-size: 30px;
        font-weight: bold;
        color: yellow;
        alignment: center;
"""
stylesheet_ES_button = """
        background-color: white;
        border: 5px solid black; 
        border-radius: 90px;
"""
#                                       SCADA
# Criação da classe tela principal com seus devidos elementos (desenvolvimento visual da SCADA).
class TelaPrincipalCCM(QMainWindow):
    # Tela.
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 35, 1920, 995)
        self.setWindowTitle("MEA - Centro de Controle de Motor - Motor de Passo e BLDC")
        self.setWindowIcon(QIcon('DC_motor.png'))
        self.setStyleSheet(stylesheet_window)
        self.InicializarElementos()

    # Elementos da tela.
    def InicializarElementos(self):
    # MOTOR DE PASSO.
        # Imagem e título do motor de passo.
        self.message_motor_SM = QPushButton('STEPPER MOTOR', self)
        self.message_motor_SM.setGeometry(200, 10, 500, 100)
        self.message_motor_SM.setStyleSheet(stylesheet_big_label)
        self.message_motor_SM.setIcon(QIcon('Stepper_motor.png'))
        self.message_motor_SM.setIconSize(QSize(75,75))
        # Título do comando ENABLE.
        self.message_enable_SM = QLabel('Enable/Disable', self)
        self.message_enable_SM.setAlignment(Qt.AlignCenter)
        self.message_enable_SM.resize(250, 50)
        self.message_enable_SM.setStyleSheet(stylesheet_small_label)
        self.message_enable_SM.move(325, 125)
        # Criando um elemento botão para ligar e desligar o motor.
        self.But_Toggle_Motor_SM = QPushButton(parent=self)
        self.But_Toggle_Motor_SM.setIcon(QIcon('OFF_button.png'))
        self.But_Toggle_Motor_SM.setIconSize(QSize(100, 100))
        self.But_Toggle_Motor_SM.setStyleSheet(stylesheet_enable_and_dir_button_and_ES_sin)
        self.But_Toggle_Motor_SM.setMinimumHeight(100)
        self.But_Toggle_Motor_SM.setMinimumWidth(100)
        self.But_Toggle_Motor_SM.move(400, 185)
        # Definir que o botão é do tipo toggle, ou seja, podemos clicar e ele mantém seu valor.
        self.But_Toggle_Motor_SM.setCheckable(True)
        # Definindo que quando o botão for clicado vamos rodar a função ToggleMotor.
        self.But_Toggle_Motor_SM.clicked.connect(self.ToggleMotor_SM)

        # Título do comando DIR.
        self.message_dir_SM = QLabel('Rotation Direction', self)
        self.message_dir_SM.setAlignment(Qt.AlignCenter)
        self.message_dir_SM.resize(250, 50)
        self.message_dir_SM.setStyleSheet(stylesheet_small_label)
        self.message_dir_SM.move(325, 300)
        # Criando um elemento botão para mudar sentido de rotação do motor.
        self.But_Dir_Motor_SM = QPushButton(parent=self)
        self.But_Dir_Motor_SM.setIcon(QIcon('DIR_0_button.png'))
        self.But_Dir_Motor_SM.setIconSize(QSize(100, 100))
        self.But_Dir_Motor_SM.setStyleSheet(stylesheet_enable_and_dir_button_and_ES_sin)
        self.But_Dir_Motor_SM.setMinimumHeight(100)
        self.But_Dir_Motor_SM.setMinimumWidth(100)
        self.But_Dir_Motor_SM.move(400, 360)

        self.But_Dir_Motor_SM.setCheckable(True)
        self.But_Dir_Motor_SM.clicked.connect(self.ChangeRotMotor_SM)

        # Título do comando SPEED.
        self.message_speed_SM = QLabel('Rotation Speed', self)
        self.message_speed_SM.setAlignment(Qt.AlignCenter)
        self.message_speed_SM.resize(250, 50)
        self.message_speed_SM.setStyleSheet(stylesheet_small_label)
        self.message_speed_SM.move(325, 515)
        # Criando um elemento slider que controla a velocidade do motor.
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
        # Rótulo 1 do slider.
        self.label_speed1_SM = QLabel('MIN.', self)
        self.label_speed1_SM.setAlignment(Qt.AlignCenter)
        self.label_speed1_SM.resize(75, 100)
        self.label_speed1_SM.setStyleSheet(stylesheet_label1_slider)
        self.label_speed1_SM.move(125, 600)
        # Rótulo 2 do slider.
        self.label_speed2_SM = QLabel('MAX.', self)
        self.label_speed2_SM.setAlignment(Qt.AlignCenter)
        self.label_speed2_SM.resize(75, 100)
        self.label_speed2_SM.setStyleSheet(stylesheet_label2_slider)
        self.label_speed2_SM.move(700, 600)
        # Definindo que quando o slider mudar de valor vamos rodar a função SendSerial.
        self.Sli_Speed_Motor_SM.valueChanged.connect(self.SendSerial_SM)
    
    # BLDC (realiza-se o espelhamento).
        # Imagem e título do motor BLDC.
        self.message_motor_BLDC = QPushButton('BLDC MOTOR', self)
        self.message_motor_BLDC.setGeometry(200 + x_displacement, 10, 500, 100) # Espelhamento horizontal de elementos repetidos.
        self.message_motor_BLDC.setStyleSheet(stylesheet_big_label)
        self.message_motor_BLDC.setIcon(QIcon('BLDC_motor.png'))
        self.message_motor_BLDC.setIconSize(QSize(75,75))
        # Título do comando ENABLE.
        self.message_enable_BLDC = QLabel('Enable/Disable', self)
        self.message_enable_BLDC.setAlignment(Qt.AlignCenter)
        self.message_enable_BLDC.resize(250, 50)
        self.message_enable_BLDC.setStyleSheet(stylesheet_small_label)
        self.message_enable_BLDC.move(325 + x_displacement, 125)

        self.But_Toggle_Motor_BLDC = QPushButton(parent=self)
        self.But_Toggle_Motor_BLDC.setIcon(QIcon('OFF_button.png'))
        self.But_Toggle_Motor_BLDC.setIconSize(QSize(100, 100))
        self.But_Toggle_Motor_BLDC.setStyleSheet(stylesheet_enable_and_dir_button_and_ES_sin)
        self.But_Toggle_Motor_BLDC.setMinimumHeight(100)
        self.But_Toggle_Motor_BLDC.setMinimumWidth(100)
        self.But_Toggle_Motor_BLDC.move(400 + x_displacement, 185)

        self.But_Toggle_Motor_BLDC.setCheckable(True)
        self.But_Toggle_Motor_BLDC.clicked.connect(self.ToggleMotor_BLDC)

        # Título do comando DIR.
        self.message_dir_BLDC = QLabel('Rotation Direction', self)
        self.message_dir_BLDC.setAlignment(Qt.AlignCenter)
        self.message_dir_BLDC.resize(250, 50)
        self.message_dir_BLDC.setStyleSheet(stylesheet_small_label)
        self.message_dir_BLDC.move(325 + x_displacement, 300)

        self.But_Dir_Motor_BLDC = QPushButton(parent=self)
        self.But_Dir_Motor_BLDC.setIcon(QIcon('DIR_0_button.png'))
        self.But_Dir_Motor_BLDC.setIconSize(QSize(100, 100))
        self.But_Dir_Motor_BLDC.setStyleSheet(stylesheet_enable_and_dir_button_and_ES_sin)
        self.But_Dir_Motor_BLDC.setMinimumHeight(100)
        self.But_Dir_Motor_BLDC.setMinimumWidth(100)
        self.But_Dir_Motor_BLDC.move(400 + x_displacement, 360)
        
        self.But_Dir_Motor_BLDC.setCheckable(True)
        self.But_Dir_Motor_BLDC.clicked.connect(self.ChangeRotMotor_BLDC)

        # Título do comando SPEED.
        self.message_speed_BLDC = QLabel('Rotation Speed', self)
        self.message_speed_BLDC.setAlignment(Qt.AlignCenter)
        self.message_speed_BLDC.resize(250, 50)
        self.message_speed_BLDC.setStyleSheet(stylesheet_small_label)
        self.message_speed_BLDC.move(325 + x_displacement, 515)
        
        self.Sli_Speed_Motor_BLDC = QSlider(parent=self) 
        self.Sli_Speed_Motor_BLDC.setOrientation(Qt.Horizontal) 
        self.Sli_Speed_Motor_BLDC.setGeometry(QRect(50, 50, 500, 100)) 
        self.Sli_Speed_Motor_BLDC.setStyleSheet(stylesheet_speed_slider)        
        self.Sli_Speed_Motor_BLDC.setMinimum(0)
        self.Sli_Speed_Motor_BLDC.setMaximum(9)
        self.Sli_Speed_Motor_BLDC.setValue(0)
        self.Sli_Speed_Motor_BLDC.setTickPosition(QSlider.TicksBelow)
        self.Sli_Speed_Motor_BLDC.setTickInterval(1)
        self.Sli_Speed_Motor_BLDC.move(200 + x_displacement, 600)
        # Rótulo 1 do slider.
        self.label_speed1_BLDC = QLabel('MIN.', self)
        self.label_speed1_BLDC.setAlignment(Qt.AlignCenter)
        self.label_speed1_BLDC.resize(75, 100)
        self.label_speed1_BLDC.setStyleSheet(stylesheet_label1_slider)
        self.label_speed1_BLDC.move(125 + x_displacement, 600)
        # Rótulo 2 do slider.
        self.label_speed2_BLDC = QLabel('MAX.', self)
        self.label_speed2_BLDC.setAlignment(Qt.AlignCenter)
        self.label_speed2_BLDC.resize(75, 100)
        self.label_speed2_BLDC.setStyleSheet(stylesheet_label2_slider)
        self.label_speed2_BLDC.move(700 + x_displacement, 600)
        
        self.Sli_Speed_Motor_BLDC.valueChanged.connect(self.SendSerial_BLDC)

    # BOTÃO DE EMERGÊNCIA.
        # Título do comando EMERGENCY STOP (ES).
        self.message_ES = QLabel('EMERGENCY STOP', self)
        self.message_ES.setAlignment(Qt.AlignCenter)
        self.message_ES.resize(300, 80)
        self.message_ES.setStyleSheet(stylesheet_ES)
        self.message_ES.move(810, 700)
        # Criando a imagem de um sinalizador para emergência.
        self.Sin_ES_image = QPushButton(parent=self)
        self.Sin_ES_image.setIcon(QIcon('OFF_ES_light.png'))
        self.Sin_ES_image.setIconSize(QSize(120,120))
        self.Sin_ES_image.setStyleSheet(stylesheet_enable_and_dir_button_and_ES_sin)
        self.Sin_ES_image.setMinimumHeight(120)
        self.Sin_ES_image.setMinimumWidth(120)
        self.Sin_ES_image.move(1100, 825)
        # Criando um elemento botão para cessar a rotação dos motores.
        self.But_ES = QPushButton(parent=self)
        self.But_ES.setIcon(QIcon('ES_button.png'))
        self.But_ES.setIconSize(QSize(200, 200))
        self.But_ES.setStyleSheet(stylesheet_ES_button)
        self.But_ES.setMinimumHeight(200)
        self.But_ES.setMinimumWidth(200)
        self.But_ES.move(860, 785)
        
        self.But_ES.setCheckable(True)
        self.But_ES.clicked.connect(self.EmergencyState)

# Criação das funções necessárias para o funcionamento da SCADA (desenvolvimento funcional da SCADA).
# Comandos para a realização de cada função são transmitidos seguindo o protocolo estabelecido no 
# código C, carregado nas placas NUCLEO. 
    # MOTOR DE PASSO.
    # Liga/desliga motor.
    def ToggleMotor_SM(self, Clicado):
        if Clicado:
            command = "A"
            Ser_SM.write(b"A") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Toggle_Motor_SM.setIcon(QIcon('ON_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "a"
            Ser_SM.write(b"a") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Toggle_Motor_SM.setIcon(QIcon('OFF_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))

    # Muda sentido de rotação do motor.
    def ChangeRotMotor_SM(self, Clicado):
        if Clicado:
            command = "D"
            Ser_SM.write(b"D") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Dir_Motor_SM.setIcon(QIcon('DIR_0_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "d"
            Ser_SM.write(b"d") 
            speed = bytes(str(int(self.Sli_Speed_Motor_SM.value())), "utf-8")
            self.But_Dir_Motor_SM.setIcon(QIcon('DIR_1_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
    # Controla velocidade de rotação do motor.
    def SendSerial_SM(self, value):
        Ser_SM.write(bytes(str(int(value)), "utf-8"))

    # BLDC.
    def ToggleMotor_BLDC(self, Clicado):
        if Clicado:
            command = "A"
            Ser_BLDC.write(b"A") 
            speed = bytes(str(int(self.Sli_Speed_Motor_BLDC.value())), "utf-8")
            self.But_Toggle_Motor_BLDC.setIcon(QIcon('ON_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "a"
            Ser_BLDC.write(b"a") 
            speed = bytes(str(int(self.Sli_Speed_Motor_BLDC.value())), "utf-8")
            self.But_Toggle_Motor_BLDC.setIcon(QIcon('OFF_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))

    def ChangeRotMotor_BLDC(self, Clicado):
        if Clicado:
            command = "D"
            Ser_BLDC.write(b"D") 
            speed = bytes(str(int(self.Sli_Speed_Motor_BLDC.value())), "utf-8")
            self.But_Dir_Motor_BLDC.setIcon(QIcon('DIR_0_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
        else:
            command = "d"
            Ser_BLDC.write(b"d") 
            speed = bytes(str(int(self.Sli_Speed_Motor_BLDC.value())), "utf-8")
            self.But_Dir_Motor_BLDC.setIcon(QIcon('DIR_1_button.png'))
            print("Command: {0}\n\rSpeed: {1}". format(command, speed))
    
    def SendSerial_BLDC(self, value):
        Ser_BLDC.write(bytes(str(int(value)), "utf-8"))
    
    # BOTÃO DE EMERGÊNCIA.
    # Cessa a rotação dos motores.
    def EmergencyState(self, Clicado):
        if Clicado:
            command = "a"
            Ser_SM.write(b"a")
            Ser_BLDC.write(b"a") 
            self.Sin_ES_image.setIcon(QIcon('ON_ES_light.png'))
            self.But_Toggle_Motor_SM.setIcon(QIcon('OFF_button.png'))
            self.But_Toggle_Motor_BLDC.setIcon(QIcon('OFF_button.png'))
            print("Command: {}". format(command))
            # Bloqueia o comando ENABLE nos motores enquanto o botão de emergência estiver acionado (botões 
            # ENABLE não conseguem acionar os motores e não mudam de valor).
            self.But_Toggle_Motor_SM.blockSignals(True)
            self.But_Toggle_Motor_BLDC.blockSignals(True)
        else:
            self.Sin_ES_image.setIcon(QIcon('OFF_ES_light.png'))
            self.But_Toggle_Motor_SM.blockSignals(False)
            self.But_Toggle_Motor_BLDC.blockSignals(False)

# Parte que inicia a tela conforme o que é descrito no __init__.
app = QApplication(sys.argv)
window = TelaPrincipalCCM()
window.show()
app.exec()