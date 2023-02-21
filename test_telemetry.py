import unittest

from telemetry import TelemetryDiagnosticControls

class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_check_transmission_should_send_a_diagnostic_message_and_receive_a_response(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient())
        controls.check_transmission()
        self.assertEqual("test", controls.diagnostic_message_result)

class MockTelemetryClient:
    def __init__(self):
        self.online_status = False
        self.diagnostic_message_result = ""
        self.diagnostic_channel_connection_string = ""

    def connect(self, diagnostic_channel_connection_string):
        self.diagnostic_channel_connection_string = diagnostic_channel_connection_string
        self.online_status = True

    def disconnect(self):
        self.online_status = False

    def receive(self):
        return self.diagnostic_message_result