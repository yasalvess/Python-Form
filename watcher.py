import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher:
    def __init__(self, path, callback):
        self.path = path
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_modified = lambda event: callback(event.src_path)
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

process = None

def restart_app(script_path):
    global process
    if process:
        process.terminate()
        process.wait()  # Esperar o processo anterior terminar

    process = subprocess.Popen(['python', script_path])

if __name__ == "__main__":
    script_path = "main.py"
    restart_app(script_path)

    watcher = Watcher(".", lambda _: restart_app(script_path))
    watcher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()
