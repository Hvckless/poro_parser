import shlex

some = 'hello world "god tell me some reason" "they we are"'
cmd_components:list[str] = shlex.split(some)

command = cmd_components[0]
arguments = cmd_components[1:]

print(command)
print(arguments)


kinggod:list[str] = []

print(len(kinggod))