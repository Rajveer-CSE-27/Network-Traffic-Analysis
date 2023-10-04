import socket

def get_domain_name(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        return domain_name[0]
    except socket.herror:
        return "Unable to resolve domain for the provided IP address"

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    domain_name = get_domain_name(ip_address)
    print(f"Domain name for {ip_address} is: {domain_name}")
