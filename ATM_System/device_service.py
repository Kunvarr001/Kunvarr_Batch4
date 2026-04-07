from device_locked_exception import DeviceLockedException
from network_connection_exception import NetworkConnectionException
from device_not_found_exception import DeviceNotFoundException
from device_handle import DeviceHandle
from device_record import DeviceRecord

class DeviceService:

    def get_device_handle(self) -> DeviceHandle:
        return DeviceHandle(is_valid=True)

    def retrieve_device_record(self, handle: DeviceHandle) -> DeviceRecord:
        return DeviceRecord(status="ACTIVE", wifi_status="CONNECTED")

    def ensure_device_available(self, handle: DeviceHandle):
        if not handle or not handle.is_valid:
            raise DeviceNotFoundException()

    def ensure_device_active(self, record: DeviceRecord):
        if record.status == "SUSPENDED":
            raise DeviceLockedException()

    def ensure_network_connected(self, record: DeviceRecord):
        if record.wifi_status != "CONNECTED":
            raise NetworkConnectionException()