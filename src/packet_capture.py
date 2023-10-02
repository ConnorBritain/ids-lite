import scapy.all as scapy
from scapy.layers import http
import datetime
import loguru

# Logger configuration
loguru.logger.add("logs/packet_capture_{time}.log")


class PacketCapture:
    def __init__(self, interface="eth0", packet_count=0):
        """
        Initialize packet capture parameters.

        Args:
            interface (str): Network interface to capture packets from.
            packet_count (int): Number of packets to capture; 0 captures indefinitely.
        """
        self.interface = interface
        self.packet_count = packet_count

    def _packet_callback(self, packet):
        """
        Callback function executed for every captured packet.

        Args:
            packet (scapy.Packet): Captured packet instance.
        """
        self._log_packet_details(packet)
        self._log_http_request(packet)

    def _log_packet_details(self, packet):
        """Log basic details of a packet."""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{timestamp}] - {packet.summary()}"
        loguru.logger.info(log_msg)

    def _log_http_request(self, packet):
        """Extract and log details of any HTTP request in the packet."""
        if packet.haslayer(http.HTTPRequest):
            http_layer = packet.getlayer(http.HTTPRequest)
            http_info = f"{packet[http_layer].Method} {packet[http_layer].Host}{packet[http_layer].Path}"
            loguru.logger.info(f"HTTP Request: {http_info}")

    def start_capture(self):
        """Initiate the packet capture process."""
        try:
            print(f"Starting packet capture on interface: {self.interface}")
            scapy.sniff(iface=self.interface, count=self.packet_count, prn=self._packet_callback, store=False)
        except Exception as e:
            loguru.logger.error(f"Error during packet capture: {e}")
            print(f"Error encountered. Check logs for details.")

if __name__ == "__main__":
    try:
        capturer = PacketCapture(interface="eth0", packet_count=0)
        capturer.start_capture()
    except KeyboardInterrupt:
        print("\nPacket capture stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
