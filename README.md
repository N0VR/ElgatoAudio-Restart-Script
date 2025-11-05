# ElgatoAudioRestart Script

## Overview

This script automatically restarts the Elgato Audio Control service by locating its running process, terminating it safely, and then relaunching the executable. It is designed as a quick fix for situations where the Elgato audio service hangs, becomes unresponsive, or fails to initialize devices properly.

## Features

- Detects the Elgato Audio Control process automatically
- Safely terminates all matching process instances
- Restarts the application without requiring a system reboot
- Provides clear status output throughout the restart process

## How it Works

1. Searches running processes for any that contain `elgatoaudio` in the name  
2. Terminates the matching processes cleanly  
3. Waits briefly to ensure shutdown is complete  
4. Restarts the Elgato Audio Control executable

## How to Run

- Windows OS
- Python 3.9 or later
- Psutil (Install)

**Run the script:**
```bash
python ElgatoAudioRestart.py
```

## What I Learned

- How to identify and manage system processes programmatically using `psutil`
- How to safely terminate processes while handling exceptions such as access denial or missing processes
- How to automate repetitive system troubleshooting tasks to save time and improve workflow reliability
- How to launch external applications from Python using `subprocess.Popen`
- The importance of adding delays and checks to ensure smooth process shutdown and restart behavior

This small script taught me how to think about system behavior, not just code behavior — a key concept in systems scripting and automation.

## Planned Improvements

- Add validation and fallback handling to detect if the restart fails and re-attempt it
- Log each restart action to a file for tracking reliability over time
- Add an optional system tray or notification message when the restart is complete
- Convert script to a .exe to allow non-technical users to run it easily
- Add OS safety checks to prevent accidental killing of critical processes

## Project Status

- On Hiatus While I work on my other Scripts

