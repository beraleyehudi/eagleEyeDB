import EagleEyeDAl
from EagleEyeDAl import dal_add


class Add:
    @staticmethod
    def add_agent(agent):
        dal_add("agents", "codeName, realName, location, status, missionsCompleted", (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed))

