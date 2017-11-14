import re

device_regex = re.compile(r'(\w+)\t(device|offline|unauthorized)')
forward_regex = re.compile(
    r'^(?P<device_id>\w+)?\s+tcp:(?P<local_port>\d+)?\s+tcp:(?P<remote_port>\d+)')


def parse_device_list(device_list):
    return device_regex.findall(device_list)


def parse_forward_list(forwarded_list):
    _forwarded_devices = {}
    for device in re.finditer(forward_regex, forwarded_list):
        _forwarded_devices[device.pop('device_id')] = device
    return _forwarded_devices
