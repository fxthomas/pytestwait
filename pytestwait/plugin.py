# coding: utf-8

import os

def pytest_cmdline_main(config):
    if config.getoption("--wait"):
        capman = config.pluginmanager.getplugin("capturemanager")
        capman.suspend_global_capture(in_=True)
        print("Current PID: %d" % os.getpid())
        print("Press ENTER...")
        raw_input()
    return None  # Use the default behavior


def pytest_addoption(parser):
    """Called by pytest to prepare the list of available command-line args"""
    parser.addoption("--wait", action="store_true", help="display pid and wait before starting tests")