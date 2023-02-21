class TelemetryDiagnosticControls:
    DIAGNOSTIC_CHANNEL_CONNECTION_STRING = "*111#"

    def __init__(self, client=None):
        self.diagnosticMessageResult = ""
        self.diagnosticInfo = ""
        self.telemetryClient = client or TelemetryClient()
        self.diagnostic_message_result = "test"

    def check_transmission(self):
        self._reconnect()
        self._send_and_receive()

    def _send_and_receive(self):
        self.diagnosticMessageResult = self.telemetryClient.receive()
        return self.diagnosticMessageResult

    def _reconnect(self):
        self.telemetryClient.disconnect()
        self.telemetryClient.connect(self.DIAGNOSTIC_CHANNEL_CONNECTION_STRING)

class TelemetryClient:
    DIAGNOSTIC_MESSAGE = ""
