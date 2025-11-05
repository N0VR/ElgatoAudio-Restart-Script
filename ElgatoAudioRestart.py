import psutil
import subprocess
import time

killed = 0
answer = "elgatoaudio"

print("Restarting ElgatoAudio")
time.sleep(0.3)

for p in psutil.process_iter(['pid', 'name']):
    if p.info['name'] and answer in p.info['name'].lower():
        try:
            print("\n")
            print(f"Killing {p.info['name']} with PID {p.info['pid']}")
            time.sleep(0.5)
            p.terminate()
            p.wait(timeout=3)
            killed += 1
        except psutil.NoSuchProcess:
            print(f"Process {p.info['pid']} already exited.")
        except psutil.AccessDenied:
            print(f"No permission to terminate {p.info['pid']}.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if killed == 0:
    print(f"No processes found matching {answer}")
else:
    print("\n")
    print(f"Done! Killed {killed} processes.")
    time.sleep(0.5)

print("\n")
print("Opening Elgato Audio")
try:
    subprocess.Popen([r"C:\Program Files\Elgato\Volume Controller\ElgatoAudioControlServer.exe"])
except FileNotFoundError:
    print("Process not found")
except PermissionError:
    print("Access denied. Try running script as admin")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n")
print("Restart Successful.")
time.sleep(0.5)
