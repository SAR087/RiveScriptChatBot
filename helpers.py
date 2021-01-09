from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory("./scripts")
bot.sort_replies()


def reply(text: str) -> str:
    res = bot.reply("localuser", text)
    return res if res != "[ERR: No Reply Matched]" else None


if __name__ == "__main__":
    while True:
        print(reply(input()))
