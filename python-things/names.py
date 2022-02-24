names = ['sydney', 'morgan', 'jeremy', 'amber']
message_sydney = f"{names[0].title()} is my daughter"
message_morgan = f"{names[1].upper()} is my other daugher"
message_wife = f"I would like for {names[3].title()} to do dirty things."
print(f"{message_sydney}\n")
print(f"{message_morgan}\n")
print(f"{message_wife} but she wont, so\n")
names[3] = 'your mom'
message_mom = f"I would like for {names[3].title()} to do dirty things."
print(f"{message_mom}\n")
