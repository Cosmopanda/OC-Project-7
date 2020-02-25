class Place:
    """docstring for Place."""

    def __init__(self, data):
        super(Place, self).__init__()
        self.address = data["formatted_address"]
        self.latitude = data["geometry"]["location"]["lat"]
        self.longitude = data["geometry"]["location"]["lng"]
        self.name = data["name"]
