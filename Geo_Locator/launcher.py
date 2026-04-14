from settings_reader import SettingsReader
from user_entry_handler import UserEntryHandler
from geo_lookup_coordinator import GeoLookupCoordinator

def main():
    config = SettingsReader().fetch()
    user_input = UserEntryHandler().capture()

    coordinator = GeoLookupCoordinator(config)
    coordinator.process(user_input)

if __name__ == "__main__":
    main()