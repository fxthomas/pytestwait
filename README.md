This is a simple pytest plugin that displays the PID and waits for a key
before starting the test run. I find this useful in combination with an
external debugger (gdb/Visual Studio), in order to make it easier to debug
issues in compiled (.pyd/.so) modules.

# Usage

Simply add the `--wait` option to the pytest command-line:

```bash
pytest --wait test/test_abc.py
```