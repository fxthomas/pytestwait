# coding: utf-8

import os

def pytest_cmdline_main(config):
    capman = config.pluginmanager.getplugin("capturemanager")
    capman.suspend_global_capture(in_=True)
    print("Current PID: %d" % os.getpid())
    print("Press ENTER...")
    raw_input()
    return None  # Use the default behavior
