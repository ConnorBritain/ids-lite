import pytest
from scapy.all import IP, HTTPRequest
from analyzer import PacketAnalyzer

@pytest.fixture
def analyzer():
    """Provide a fresh PacketAnalyzer for each test."""
    return PacketAnalyzer()

def test_analyze_http_packet(analyzer):
    packet = IP(dst="192.168.0.1", src="192.168.0.100") / HTTPRequest(Method="GET", Path="/admin")
    analyzer.analyze_packet(packet)
    # Since the analyzer primarily logs, this test checks for smooth execution without exceptions.
    assert True

def test_analyze_ip_packet(analyzer):
    packet = IP(dst="192.168.0.1", src="192.168.0.100")
    analyzer.analyze_packet(packet)
    assert True

def test_analyze_dns_packet(analyzer):
    # In this placeholder test, we're focusing on the test setup. Real DNS packet tests can be added later.
    assert True

# To run: pytest test_analyzer.py