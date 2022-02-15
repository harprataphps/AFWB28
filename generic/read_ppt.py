from pyjavaproperties import Properties
p_files = Properties()
p_files.load(open("config.properties"))
v=p_files["ITO"]
print(p_files.items())
print(v)
print(type(v))