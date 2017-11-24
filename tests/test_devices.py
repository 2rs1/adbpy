from adbpy.devices import parse_device_string


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
    expected =  {"1ccb04bb": {"device": None, "device_status": "device", "model": None, "product": None, "usb": None},
        "950a8ad5": {"device": None, "device_status": "unauthorized", "model": None, "product": None, "usb": None},
        "1234567": {"device": None, "device_status": "offline", "model": None, "product": None, "usb": None}}
    assert parse_device_string(input) == expected
