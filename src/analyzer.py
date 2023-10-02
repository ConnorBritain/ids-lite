import scapy.all as scapy
from scapy.layers import http
import loguru

SIGNATURES = {
    'http': [
        'GET /admin', 
        'POST /login.php',
        'User-Agent: BadBot',
        'User-Agent: sqlmap',
        '1=1',  # SQL injection
        '; DROP TABLE',  # SQL injection
        '<script>',  # XSS attempt
        'cmd.exe',  # Command execution
        'etc/passwd'  # File inclusion
    ],
    'ip': ['192.168.0.100', '10.0.0.5'],
    'dns': ['maliciousdomain.com']
}

class PacketAnalyzer:
    def __init__(self):
        pass

    def analyze_packet(self, packet):
        if packet.haslayer(http.HTTPRequest):
            self._analyze_http_packet(packet.getlayer(http.HTTPRequest))
        elif packet.haslayer(scapy.IP):
            self._analyze_ip_packet(packet.getlayer(scapy.IP))
        elif packet.haslayer(scapy.DNSQR):
            self._analyze_dns_packet(packet.getlayer(scapy.DNSQR))

    def _analyze_http_packet(self, http_packet):
        for signature in SIGNATURES['http']:
            if signature in str(http_packet):
                loguru.logger.warning(f"Suspicious HTTP signature detected: {signature}")

    def _analyze_ip_packet(self, ip_packet):
        if ip_packet.src in SIGNATURES['ip']:
            loguru.logger.warning(f"Suspicious IP address detected: {ip_packet.src}")

    def _analyze_dns_packet(self, dns_packet):
        if dns_packet.qname in SIGNATURES['dns']:
            loguru.logger.warning(f"Suspicious DNS request detected: {dns_packet.qname}")

if __name__ == "__main__":
    sample_http_packet = scapy.IP(dst="192.168.0.1", src="192.168.0.100") / http.HTTPRequest(Method="GET", Path="/admin")
    analyzer = PacketAnalyzer()
    analyzer.analyze_packet(sample_http_packet)