msg = input(">>> ")
words = msg.split(" ")
emojis = {
    ":)": "😃",
    ":(": "😢",
    "<3": "💜"
}

y = ""
x = "  "
for z in words:
   y += emojis.get(z, z) + x

print(y)
