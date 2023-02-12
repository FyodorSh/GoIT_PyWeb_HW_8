import re

from models import Quote
import connect


def main():
    quotes = Quote.objects()

    while True:
        quote_list = []
        command = input('Enter "<command>: <value>": ')

        try:
            command_list = command.split(":")
            command_name = command_list[0]

            if command_name == "name":
                for q in quotes:
                    if q.author.fullname == command_list[1].strip():
                        quote_list.append(re.sub("[“|”]", "", q.quote))
            elif command_name == "tag":
                for q in quotes:
                    if command_list[1].strip() in q.tags:
                        quote_list.append(re.sub("[“|”]", "", q.quote))
            elif command_name == "tags":
                tag_list = command_list[1].split(",")

                for q in quotes:
                    for t in tag_list:
                        if t in q.tags:
                            quote_list.append(re.sub("[“|”]", "", q.quote))
                            break
            elif command_name == "exit":
                break
            else:
                raise ValueError

            if quote_list:
                print(quote_list)

        except IndexError:
            print('You entered the wrong command')
        except ValueError:
            print('You entered the wrong command')


if __name__ == "__main__":
    main()
