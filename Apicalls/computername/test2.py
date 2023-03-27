import psutil

for proc in psutil.process_iter(['pid', 'name', 'exe']):
    proc.memory_maps()[0].path