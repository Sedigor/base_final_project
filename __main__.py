from Bot import Bot


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            bot.display_help()
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
