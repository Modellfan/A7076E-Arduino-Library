#!/usr/bin/env python3
"""Simple serial ping test: send PING and expect PONG."""

from __future__ import annotations

import argparse
import sys
import time

try:
    import serial
except ImportError:
    print("Missing dependency: pyserial. Install with: python -m pip install pyserial", file=sys.stderr)
    raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serial ping setup test")
    parser.add_argument("--port", default="COM12", help="Serial port (default: COM12)")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")
    parser.add_argument("--timeout", type=float, default=8.0, help="Overall timeout in seconds")
    parser.add_argument("--boot-wait", type=float, default=1.5, help="Wait time after opening serial")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    deadline = time.monotonic() + args.timeout

    print(f"Opening {args.port} @ {args.baud}")
    try:
        with serial.Serial(args.port, args.baud, timeout=0.2) as ser:
            time.sleep(args.boot_wait)
            ser.reset_input_buffer()
            ser.write(b"PING\r\n")
            ser.flush()
            print("Sent: PING")

            while time.monotonic() < deadline:
                raw = ser.readline()
                if not raw:
                    continue
                line = raw.decode("utf-8", errors="replace").strip()
                if not line:
                    continue
                print(f"Recv: {line}")
                if line == "PONG":
                    print("PING_TEST_PASS")
                    return 0

            print("PING_TEST_FAIL timeout waiting for PONG", file=sys.stderr)
            return 2
    except Exception as exc:
        print(f"PING_TEST_FAIL serial error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
