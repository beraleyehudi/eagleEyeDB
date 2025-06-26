class Agent:
    def __init__(self, code_name, real_name, location, status, missions_completed):
        self.id = None
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return f"""code name = {self.code_name}
        real name = {self.real_name}
        location = {self.location}
        status = {self.status}
        missions completed = {self.missions_completed}
        """