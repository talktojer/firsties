first_name = "joe"
last_name = "smith"

full_name = f"{first_name} {last_name}"

message = f"Hello, {first_name.title()} . Are you related to Fred {last_name.title()}?"

print(full_name.title())
print(message)

famous_person = "   Bill Gates   "
quote = "Noone will ever need more than 640k of memory"
message = f"{famous_person.strip()}:\n\t{quote}"

print(message)
