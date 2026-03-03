# AGENTS.md (Codex Agent Instructions)

## Project goal

Implement a complete Arduino C++ driver library for the SIMCom A7670E / A76xx Series modem, covering all AT command functionality described in:

- `A76XX_Series_AT_Command_Manual_V1.09.pdf` (source-of-truth specification)

The library must provide:

- Constant definitions + enums for all command names, modes, option constants, and error codes used across the manual.
- Struct-based return types for every high-level API function (no "naked String" returns from public APIs).
- Blocking AT functions that wait for correct responses (`OK`/`ERROR`/`+CME`/`+CMS` and any documented intermediate prompts) with a timeout.
- Even though it is blocking, all wait loops must be cooperative: call `yield()` and/or `delay(0)` regularly to support multitasking (ESP32/ESP8266, WiFi stack, RTOS, etc.).
- A universal executor so any AT command can be issued by enum, plus typed convenience wrappers for every command in the PDF.

## Repository layout

Use this library structure (Arduino library style):

```text
/src
  A7670E.h
  A7670E.cpp
  A7670E_Commands.h          // all enums/consts for commands and shared constants
  A7670E_Types.h             // all public structs/enums returned by APIs
  A7670E_Parsers.cpp/.h      // parsers for responses and URCs
/examples
  BasicAT/BasicAT.ino
  GNSS/GNSS.ino
  Network/Network.ino
  HTTP/HTTP.ino
  MQTT/MQTT.ino
/docs
  command-coverage.md        // checklist of every AT command and wrapper status
  notes.md
/spec
  A76XX_Series_AT_Command_Manual_V1.09.pdf
```

If the PDF is not already in `/spec`, add it there and treat it as immutable. The PDF is the authoritative reference.

## Non-negotiable behavior requirements

### Blocking calls must still multitask

All blocking loops (reading UART, waiting for a prompt, waiting for a final result) MUST:

- call `yield()` at least every ~10ms (configurable)
- optionally call `delay(0)` as a scheduler hint
- avoid long unbroken tight loops

Implement this once in the core IO layer and ensure every function uses it.

### Robust AT response handling

The core response engine must correctly handle:

- Command echo (optional on/off)
- Intermediate lines (e.g., `+CSQ: ...`)
- Final lines:
- `OK`
- `ERROR`
- `+CME ERROR: <code>`
- `+CMS ERROR: <code>`
- URCs arriving asynchronously during a command response:
- Provide a hook/callback for URCs
- Do not let URCs break the state machine for a command response

### Timeouts

Every blocking operation must accept a timeout (ms) and return a structured timeout result (`final = TIMEOUT`).

### Memory constraints

- Prefer fixed-size buffers for line capture, with a configurable max number of lines.
- Do not store unbounded raw logs in RAM by default.
- Avoid heap fragmentation where possible; Arduino `String` is allowed but keep usage disciplined.

## Public API design rules

### "One function does the whole thing" for typed helpers

For high-level wrappers (especially GNSS/network), do not require user code like:

```cpp
auto r = modem.getCEREG();
auto v = modem.parseCREGLike(r);
```

Instead provide a single call:

```cpp
A7670E::RegStatus s = modem.getCEREG();
```

Internally you can still separate transport + parsing, but the public API should return the parsed struct directly.

### Universal executor stays available

In addition to typed wrappers, keep:

- `execRaw("AT+...")`
- `exec(AtCommandId cmd, args, timeout)`

This guarantees full manual coverage even if a typed wrapper lags.

### Struct return types

Every wrapper returns a struct containing at least:

- `ok` boolean
- `final` enum (`OK`, `ERROR`, `CME_ERROR`, `CMS_ERROR`, `TIMEOUT`)
- `errorCode` (for CME/CMS), if applicable
- parsed fields (command-specific)

Example pattern:

- `GnssFix { ok, final, errorCode, valid, lat, lon, ... }`
- `HttpActionResult { ok, final, errorCode, method, status, dataLen }`

## Implementation workflow (spec-driven)

### Step 1 - Build a command inventory from the PDF

Create `/docs/command-coverage.md` with a table listing every AT command in the manual:

- Command name (e.g., `AT+CGNSSPWR`)
- Chapter/page reference
- Modes supported (test `=?`, read `?`, write `=`, exec)
- Wrapper function planned (name/signature)
- Parser implemented (Y/N)
- Example responses and URCs

This file is the tracking backbone. It must reach 100% coverage.

### Step 2 - Define constants and enums

In `A7670E_Commands.h` and `A7670E_Types.h`:

- `enum class AtCommandId` for every command in the PDF
- Enums for documented option sets (e.g., registration modes, GNSS output modes, PDP types, auth types, TLS versions, MQTT QoS, etc.)
- Error code enums where the manual defines them
- String mapping in PROGMEM (`commandToFlashString(AtCommandId)`)

### Step 3 - Implement the AT engine

In `A7670E.cpp`:

- UART transport via `Stream&`
- `execRaw()` and `exec()` blocking with timeout
- line reader supporting CRLF normalization
- final result detector
- cooperative yield inside loops
- optional debug stream
- URC handler callback

### Step 4 - Implement typed wrappers per manual section

Implement section by section:

- Basic AT, device info
- SIM, PIN, phonebook (if present)
- SMS
- Network registration + signal
- PDP + data session
- TCP/UDP sockets
- HTTP(S)
- MQTT(S)
- GNSS
- Filesystem + FTP/FTPS (if present)
- BLE/BT (if present)
- Any remaining modules in the manual

Each wrapper should:

- call `exec()`/`execRaw()`
- wait for the required prompt/response pattern
- parse into a struct
- return struct with `ok`/`final`/`errorCode`

### Step 5 - Examples compile-clean

Each example sketch should compile on at least:

- AVR (Uno/Nano) where feasible (note memory limits)
- ESP32 (recommended baseline)

Use `HardwareSerial` in examples (no board-specific pin assumptions).

## Parsing rules

- Parsers must be defensive: fields may be empty, quoted, or absent depending on mode.
- Prefer predictable tokenization over regex.
- Always document which response format you implemented in a comment above the parser, including a sample line from the manual.

## Testing / validation expectations

Minimum validation for each wrapper:

- Unit-level: parser tests where possible (if a lightweight test framework is used) OR compile-time parser self-check with hardcoded sample strings.
- Integration: example sketch demonstrates usage.

Add a smoke test sketch `examples/BasicAT/BasicAT.ino` that:

- checks AT
- turns echo off
- reads SIM status
- reads signal
- reads registration
- prints results

## Coding conventions

- Use `enum class` everywhere (no unscoped enums).
- Keep API names consistent:
- `getXxx()` returns parsed struct
- `setXxx(...)` returns result struct
- `startXxx()`/`stopXxx()` for sessions
- Avoid breaking changes to the public API once examples are written.
- Prefer `constexpr` for constants.
- Store command strings in PROGMEM using `F()`.

## Definition of "done"

This project is complete only when:

- `/docs/command-coverage.md` lists every AT command in the PDF and each has:
- a corresponding `AtCommandId`
- a mapped command string
- at least a raw-call path via `exec(AtCommandId, ...)`
- a typed wrapper implemented or a documented reason why it cannot be meaningfully wrapped (rare)
- All examples compile
- Core executor is cooperative (`yield()`/`delay(0)`) and stable under URCs

## If you must choose priorities

If time/space constraints force prioritization, do it in this order:

- AT engine correctness + cooperative scheduling
- Full command inventory + enum coverage
- GNSS + PDP + sockets
- HTTP + MQTT
- SMS + filesystem + BLE/BT

But the target remains full PDF coverage.

## Notes for the agent

- Treat the PDF as the single source of truth; do not invent commands or formats.
- If the manual shows multiple firmware variants, implement the most common one and add fallbacks (`execRaw()` with alternate command name) where appropriate.
- Keep a changelog in `/docs/notes.md` describing any ambiguities and how you resolved them.
