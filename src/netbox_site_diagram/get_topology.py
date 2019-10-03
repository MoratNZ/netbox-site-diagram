#!/usr/bin/env python3

import argparse
from enbox.lib.config import load as loadConfig
import enbox.lib.netboxapi
from pprint import pprint


def main():
    args = _getArgs()

    config = loadConfig(args.configFile)

    api = enbox.lib.netboxapi.init(config)

    device = api.dcim.devices.get(name=args.device)
    deviceInterfaces = api.dcim.interfaces.filter(device_id=device.id)


if __name__ == "__main__":
    main()
