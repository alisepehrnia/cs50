def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    inp = input("Enter your chat: ")
    converted = convert(inp)
    print(converted)

main()