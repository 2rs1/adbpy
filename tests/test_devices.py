from adbpy.devices import parse_device_string, parse_forward_string


def test_parse_device():
    input = "1ccb04bb\tdevice\n"
    expected = {"1ccb04bb": {"device": None, "device_status": "device",
                             "model": None, "product": None, "usb": None}}
    assert parse_device_string(input) == expected

    input = "1ccb04bb\tdevice\n950a8ad5\tunauthorized\n"
    expected = {"1ccb04bb": {"device": None, "device_status": "device", "model": None, "product": None, "usb": None},
                "950a8ad5": {"device": None, "device_status": "unauthorized", "model": None, "product": None, "usb": None}}
    assert parse_device_string(input) == expected

    input = ""
    expected = {}
    assert parse_device_string(input) == expected

    input = "1ccb04bb\tdevice\n950a8ad5\tunauthorized\n1234567\toffline\n"
    expected = {"1ccb04bb": {"device": None, "device_status": "device", "model": None, "product": None, "usb": None},
                "950a8ad5": {"device": None, "device_status": "unauthorized", "model": None, "product": None, "usb": None},
                "1234567": {"device": None, "device_status": "offline", "model": None, "product": None, "usb": None}}
    assert parse_device_string(input) == expected


def test_parse_forward():
    input = "1ccb04bb\ntcp:4\ntcp:2"
    expected = {"1ccb04bb": {"local_port": "4", "remote_port": "2"}}
    assert parse_forward_string(input) == expected

    input = "1ccb04bb\ntcp:4\ntcp:2\n950a8ad5\ntcp:4\ntcp:3\n1234567\ntcp:4\ntcp:5"
    expected = {"1ccb04bb": {"local_port": "4", "remote_port": "2"},
                "950a8ad5": {"local_port": "4", "remote_port": "3"},
                "1234567": {"local_port": "4", "remote_port": "5"}}
    assert parse_forward_string(input) == expected
