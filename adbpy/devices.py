import re

device_regex = re.compile(r'(?P<device_id>\w+)\s+(?P<device_status>device|offline|unauthorized)\s+?(usb:(?P<usb>[a-zA-Z0-9\-\.]+)\s+product:(?P<product>\w+)\s+model:(?P<model>\w+)\s+device:(?P<device>\w+))?')
forward_regex = re.compile(r'(?P<device_id>\w+)?\s+tcp:(?P<local_port>\d+)?\s+tcp:(?P<remote_port>\d+)')


def parse_string(string, regex):
    _devices = {}
    for device in re.finditer(regex, string):
        group_dict = device.groupdict()
        device_id = group_dict.pop('device_id')
        _devices[device_id] = group_dict
    return _devices


def parse_forward_string(forwarded_string):
    return parse_string(forwarded_string, forward_regex)


def parse_device_string(device_string):
    return parse_string(device_string, device_regex)
