'''this module for python hacking tools'''
import socket
import IPy

ports = []


def port_scanner_80():
    '''this fucntion is used to scan a purticular port and ip
       '''
    ip_address = input("[+] Enter your target IP : ")
    port = 80
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))
        print('[+] port 80 is opened')

    except:
        print('[-] port is closed')


def get_banner(s):
    s.recv(1024).decode('utf-8')


def port_scanner(ip_address, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip_address, port))

        try:
            banner = get_banner(sock)
            print('[+] port ' + str(port) + ':' + str(banner))
        except:
            print('[+] port ' + str(port) + ' is open')
            ports.append("port " + str(port))

    except:
        print('[-] port ' + str(port) + ' is closed')


ip_address = input("[+] Enter your target IP : ")
start_port = int(input("enter your start to check ports : "))
end_port = int(input("Enter your end to check ports : "))


def check_ip(ip_address):
    try:
        IPy.IP(ip_address)
        return (ip_address)
    except ValueError:
        return socket.gethostbyname(ip_address)


def range_port_scanner():
    ip = check_ip(ip_address)
    for i in range(start_port, end_port + 1):
        port_scanner(ip, i)


range_port_scanner()
print(ports)
