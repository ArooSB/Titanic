from load_data import load_data

all_data = load_data()
print(all_data.keys())


def print_help():
    """List of commands"""
    print("Welcome to the Ships CLI!")
    print("Enter 'help' to view available commands.")
    print("Available commands:")
    print("  help")
    print("  show_countries")
    print("  top_countries <num>")
    print("  exit")


def show_countries(data):
    """ list of all the countries, No duplicates."""
    countries = {ship.get('COUNTRY', 'Unknown') for ship in data}
    for country in sorted(countries):
        print(country)


def top_countries(data, num):
    """top countries with the highest number of ships."""
    country_count = {}
    for ship in data:
        country = ship.get('COUNTRY', 'Unknown')
        country_count[country] = country_count.get(country, 0) + 1

    sorted_countries = sorted(country_count.items(), key=lambda item: item[1],
                              reverse=True)
    for country, count in sorted_countries[:num]:
        print(f"{country}: {count}")


def load_and_validate_data():
    try:
        all_data = load_data()
        if not all_data or 'data' not in all_data:
            print("INFO: No data loaded. Please check the data source.")
            return None
        return all_data['data']
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def process_user_commands(data):
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if user_input == "help":
            print_help()
        elif user_input == "show_countries":
            show_countries(data)
        elif user_input.startswith("top_countries"):
            try:
                parts = user_input.split()
                num = int(parts[1]) if len(parts) > 1 else 5
                top_countries(data, num)
            except ValueError:
                print(
                    "INFO: Invalid command format. Use 'top_countries <num>'.")
            except Exception as e:
                print(f"Error: {str(e)}")
        elif user_input == "exit":
            break
        else:
            print(
                "Invalid command. Use 'help' to see the list of available "
                "commands.")


def main():
    data = load_and_validate_data()
    if data is not None:
        process_user_commands(data)


if __name__ == "__main__":
    main()

