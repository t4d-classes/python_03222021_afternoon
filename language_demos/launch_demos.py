import subprocess

# result = subprocess.run("where chkdsk12.exe")

# print(result)


p = subprocess.Popen(
    "where chkdsk12.exe",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)

# for line in p.stdout.readlines():
#     print(str(line, "UTF-8"))

retval = p.wait()
print(retval)
