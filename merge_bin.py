# Merges bootloader + partitions + app into a single flashable image.
# Run AFTER a successful `pio run -e esp32dev-4inch` build:
#   python merge_bin.py
# Flash the result at offset 0x0, e.g.:
#   esptool.py --chip esp32 --port COMx write_flash 0x0 LebanonFireEMScombined.bin

import glob
import os
import subprocess
import sys


def main():

    project_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(project_dir, ".pio", "build", "esp32dev-4inch")
    output = os.path.join(project_dir, "LebanonFireEMScombined.bin")

    # Locate the esptool.py shipped with PlatformIO
    candidates = glob.glob(os.path.expanduser(
        os.path.join("~", ".platformio", "packages", "tool-esptoolpy*", "esptool.py")))
    if not candidates:
        sys.exit("esptool.py not found under ~/.platformio/packages/tool-esptoolpy*")
    esptool = sorted(candidates)[-1]

    cmd = [
        sys.executable, esptool,
        "--chip", "esp32",
        "merge_bin",
        "-o", output,
        "--flash_mode", "dio",
        "--flash_freq", "40m",
        "--flash_size", "4MB",
        "0x1000", os.path.join(build_dir, "bootloader.bin"),
        "0x8000", os.path.join(build_dir, "partitions.bin"),
        "0x10000", os.path.join(build_dir, "firmware.bin"),
    ]
    print("Merging flash images ->", output)
    subprocess.check_call(cmd)
    print("Done:", output)


if __name__ == "__main__":
    main()
