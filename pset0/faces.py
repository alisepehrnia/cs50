def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    inp = input("Enter your chat: ")
    print(convert(inp))

main()