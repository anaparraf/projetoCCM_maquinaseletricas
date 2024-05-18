from serial.tools import list_ports
serial_ports = list_ports.comports()
for port, desc, _ in sorted(serial_ports):
    print("{}: {}\n".format(port, desc))

