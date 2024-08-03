import uuid

leet = uuid.UUID('13371337-1337-1337-1337-133713371337')
print(str(uuid.uuid5(leet,'admin123')))
