# Implements a script which prints basic information about your OS to console.

import psutil

wo = raw_input("What statistics do you need: mem or CPU?")

if wo == "mem":
    print("virtual total: ", psutil.virtual_memory().total,
          "virtual used: ", psutil.virtual_memory().used,
          "virtual free: ", psutil.virtual_memory().free,
          "virtual shared: ", "No shared attribute",
          "swap total: ", psutil.swap_memory().total,
          "swap used: ", psutil.swap_memory().used,
          "swap free: ", psutil.swap_memory().free)
if wo == "CPU":
    print("system.cpu.idle: ", psutil.cpu_times().idle,
          "system.cpu.user: ", psutil.cpu_times().user,
          "system.cpu.iowait: ", "no info available info",
          "system.cpu.stolen: ", "no info available info",
          "system.cpu.system: ", psutil.cpu_times().system)

if wo != "mem" and wo != "CPU":
    print("Error input data")
