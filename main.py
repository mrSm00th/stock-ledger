from event_replay import replay_events
from command_input import read_user_command, parse_command
from dispatch_command import dispatch_command


def main():

    file_name = "\stock-ledger\events.log"

    replay_results = replay_events(file_name)

    if not replay_results["error"]:

        inventory = replay_results["state"]

        while True:

            try:

                user_input = read_user_command()
                parsed = parse_command(user_input)

                dispatch_command(state=inventory, parsed_cmd=parsed)

            except ValueError as e:
                print(str(e))
                continue

    else:

        print(replay_results["message"])


if __name__ == "__main__":
    main()
