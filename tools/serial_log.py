#!/usr/bin/env python3
"""Open a serial port and mirror output to console + log file.

Examples:
  python tools/serial_log.py
  python tools/serial_log.py --port COM12 --baud 115200
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

try:
    import serial
except ImportError:
    print("Missing dependency: pyserial. Install with: python -m pip install pyserial", file=sys.stderr)
    raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read serial data and write logs")
    parser.add_argument("--port", default="COM12", help="Serial port, e.g. COM12")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
    parser.add_argument("--timeout", type=float, default=0.2, help="Read timeout in seconds")
    parser.add_argument("--log-dir", default="log", help="Directory for log files")
    parser.add_argument(
        "--max-seconds",
        type=float,
        default=0.0,
        help="Auto-stop after N seconds (0 disables)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = log_dir / f"serial_{args.port.replace(':', '_')}_{stamp}.log"

    print(f"Opening {args.port} @ {args.baud}")
    print(f"Writing log: {log_path}")
    if args.max_seconds > 0:
        print(f"Max runtime: {args.max_seconds} seconds")

    try:
        ser = serial.Serial(args.port, args.baud, timeout=args.timeout)
    except Exception as exc:
        print(f"Failed to open serial port: {exc}", file=sys.stderr)
        return 1

    with ser, log_path.open("a", encoding="utf-8", newline="") as log_file:
        started = time.monotonic()
        log_file.write(f"# Started {datetime.now().isoformat()}\\n")
        log_file.flush()
        try:
            while True:
                if args.max_seconds > 0 and (time.monotonic() - started) >= args.max_seconds:
                    print("Stopping logger (max runtime reached)...")
                    break
                data = ser.readline()
                if not data:
                    continue
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                line = data.decode("utf-8", errors="replace").rstrip("\\r\\n")
                out = f"[{ts}] {line}"
                print(out)
                log_file.write(out + "\\n")
                log_file.flush()
        except KeyboardInterrupt:
            print("Stopping logger...")
        finally:
            log_file.write(f"# Stopped {datetime.now().isoformat()}\\n")
            log_file.flush()
            time.sleep(0.05)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
