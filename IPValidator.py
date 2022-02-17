class IPaddress:
    def verifyIP(self,IP) -> str:
        if 2 <= IP.count(":") <=7 and all(self.vIPv6(i) for i in IP.split(":")):
            return "IPV6"
        if IP.count(".") == 3 and all(self.vIPv4(i) for i in IP.split(".")):
            return "IPV4"
        return "Invalid IP address"

    def vIPv6(self,ip)->bool:
        if len(ip) > 3:
            return False
        try:
            if ip == "" or int(ip,16) >=0 and ip[0] != '-':
                return True
            else:
                return False
        except Exception as e:
            print(e)
    def vIPv4(self,ip)->bool:
        if 0 <= int(ip) <=255 and str(int(ip)) == ip:
            return True
        else:
            return False

def IPCheck(IP)->None:
    a = IPaddress()
    print(a.verifyIP(IP))

if __name__ == '__main__':
    IP = input("Enter the IP address to validate: ")
    IPCheck(IP)
