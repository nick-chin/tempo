print("hello world")
with open("log.log","w") as f:
    f.write("test log entry")
f.close()