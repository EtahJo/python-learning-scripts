#!/usr/bin/env python3

import os
import sys


def pending_reboot():
    """
    return true if computer is pendinf reboot
    """
    return os.path.exists('/run/reboot-required')


def main():
    if pending_reboot():
        print("Computer pending reboot")
        sys.exit(1)
    if disk_full():
        sys.exit(1)
    print("Everythin is OK!")
    sys.exit(0)


main()
