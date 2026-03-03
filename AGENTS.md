# AGENTS.md

## Project-Specific Agent Profile

- A7670E modem library instructions: [`agents_a7076e.md`](agents_a7076e.md)

## Implementation Log Usage

Before and after each task, update `IMPLEMENTATION_LOG.md`.

Required flow:
- Create a timestamped entry title: `YYYY-MM-DD HH:MM:SS +/-TZ - Task Title`.
- Fill `Planned Steps` before changing files.
- Before any code/doc change, create a stage snapshot and record `stage_id` and `stage_path` in the same log entry.
- After implementation, fill `Changes Made`, `Automated Tests Run`, `Result`, and `Artifacts`.
- Run a validation test after each implementation step and record command/result immediately.
- Put only blockers/assumptions in `Notes`.
- If no test is run, explicitly state why.

## Mandatory Validation Workflow

For every code change, follow this sequence. A change is not complete unless all steps pass.

1. Run a simple serial ping setup test (`PING` -> `PONG`) to verify serial path and device responsiveness.
2. Create an archive snapshot of the files being changed.
3. Write or update an automated test case that verifies the changed behavior.
4. Run automated tests locally and confirm they pass.
5. Build and upload firmware to the target device on `COM12`.
6. Start serial test console validation that:
   - Resets the device,
   - Captures serial output to a log file,
   - Analyzes the log,
   - Reports pass/fail for test automation.

## Feature Testability Rule

For every new feature request, define and implement an automation path before closing the task.

Required for each feature:
- Add or update automation tooling under `tools/` so the feature can be verified non-interactively.
- Add a dedicated firmware serial test command with predictable naming: `test_<feature_name>`.
- Ensure `help` output documents the new serial command.
- Run the serial command at least once during validation and record command plus outcome.

## Self-Test Placement Convention

For readability, keep firmware self-test function implementations at the end of each source file.

Required format:
- `// ====================================================================================================`
- `// Self Tests`
- `// ====================================================================================================`
- Place all `run_*selftest` implementations under that divider.

## Stage Archiving Workflow

Use `tools/stage_archive.ps1` to keep restore points before code changes.

Mandatory gate:
- Do not edit code/docs until a snapshot is created for the exact files to be modified.
- Record `SNAPSHOT_OK stage=<stage_id>` and `stage_path=...` in `IMPLEMENTATION_LOG.md` before proceeding.

Git tracking rule:
- Keep generated stage archive contents out of git.
- Enforce root-level ignore for `archives/` in `.gitignore`.
- Only placeholder keep-files are allowed: `archives/.gitkeep`, `archives/stages/.gitkeep`.

## Required Commands

### 1) Serial ping setup test
- `python tools/serial_ping.py --port COM12 --baud 115200 --timeout 8`

### 2) Archive snapshot
- `powershell -ExecutionPolicy Bypass -File tools/stage_archive.ps1 -Action snapshot -Label "<change_label>" -Paths <path1>,<path2>`

If `-Paths` parsing fails in shell:
- `powershell -ExecutionPolicy Bypass -Command "& { .\tools\stage_archive.ps1 -Action snapshot -Label 'before_<change_name>' -Paths @('path1','path2') }"`

### 3) List snapshots
- `powershell -ExecutionPolicy Bypass -File tools/stage_archive.ps1 -Action list`

### 4) Restore snapshot
- `powershell -ExecutionPolicy Bypass -File tools/stage_archive.ps1 -Action restore -Stage "<stage_id>"`
- Dry run: `powershell -ExecutionPolicy Bypass -File tools/stage_archive.ps1 -Action restore -Stage "<stage_id>" -DryRun`

### 5) Automated test case + run
- Add/update tests under `test/`.
- Example: `pio test -e release`

### 6) Build and upload
- `pio run -e release -t upload --upload-port COM12`

### 7) Serial test console execution
- `python tools/serial_log.py --port COM12 --baud 115200 --max-seconds 60`

## Completion Criteria

A task is complete only if all of the following are true:
- Implementation log entry is complete and correctly structured.
- Archive snapshot exists for the changed files.
- Automated test case exists and passes.
- Firmware upload to device succeeds.
- Serial session runs with reset and log capture.
- Log analysis reports success for expected behavior.
