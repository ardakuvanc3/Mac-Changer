import subprocess
import re

def get_current_mac(interface):
    try:
        result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.STDOUT, universal_newlines=True)
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("MAC adresi bulunamadı.")
            return None
    except subprocess.CalledProcessError:
        print("Arayüz bilgileri alınamadı.")
        return None

def change_mac(interface, new_mac):
    try:
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
    except Exception as e:
        print(f"MAC adresi değiştirilemedi: {e}")

def main():
    interface = input("MAC adresini değiştirmek istediğiniz arayüzü girin (örneğin, eth0 veya wlan0): ")
    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"Mevcut MAC adresi: {current_mac}")
        new_mac = input("Yeni MAC adresini girin (örneğin, 00:11:22:33:44:55): ")
        change_mac(interface, new_mac)
        updated_mac = get_current_mac(interface)
        if updated_mac == new_mac:
            print(f"MAC adresi başarıyla değiştirildi: {updated_mac}")
        else:
            print("MAC adresi değiştirilemedi.")

if __name__ == "__main__":
    main()
