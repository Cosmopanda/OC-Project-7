#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com


class Place:
    """docstring for Place."""

    def __init__(self, data):
        super(Place, self).__init__()
        self.address = data["formatted_address"]
        self.latitude = data["geometry"]["location"]["lat"]
        self.longitude = data["geometry"]["location"]["lng"]
        self.name = data["name"]
