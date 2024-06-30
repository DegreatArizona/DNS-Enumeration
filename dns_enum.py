import dns.resolver

def dns_enum(domain):
    try:
        # Initialize a DNS resolver
        resolver = dns.resolver.Resolver()
        
        # Query for A records (IPv4 addresses)
        a_records = resolver.resolve(domain, 'A')
        print(f"A records for {domain}:")
        for record in a_records:
            print(record)

        # Query for AAAA records (IPv6 addresses)
        aaaa_records = resolver.resolve(domain, 'AAAA')
        print(f"\nAAAA records for {domain}:")
        for record in aaaa_records:
            print(record)

        # Query for MX records (mail exchange servers)
        mx_records = resolver.resolve(domain, 'MX')
        print(f"\nMX records for {domain}:")
        for record in mx_records:
            print(record)

        # Query for NS records (name servers)
        ns_records = resolver.resolve(domain, 'NS')
        print(f"\nNS records for {domain}:")
        for record in ns_records:
            print(record)

        # Query for TXT records (text records)
        txt_records = resolver.resolve(domain, 'TXT')
        print(f"\nTXT records for {domain}:")
        for record in txt_records:
            print(record)

    except dns.resolver.NoAnswer:
        print(f"No DNS records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"DNS domain '{domain}' does not exist")

def enumerate_subdomains(domain):
    subdomains = [
        'www', 'mail', 'ftp', 'test', 'admin', 'blog', 'dev', 'webmail', 'ns1', 'ns2',
        'smtp', 'secure', 'server', 'ns', 'vpn', 'm', 'shop', 'smtp', 'imap', 'pop3'
    ]
    print(f"\nEnumerating subdomains for {domain}:")
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            a_records = dns.resolver.resolve(subdomain, 'A')
            print(f"\nA records for {subdomain}:")
            for record in a_records:
                print(record)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"No A records found for {subdomain}")

if __name__ == "__main__":
    domain = input("Enter domain name to perform DNS enumeration: ").strip()
    dns_enum(domain)
    enumerate_subdomains(domain)
