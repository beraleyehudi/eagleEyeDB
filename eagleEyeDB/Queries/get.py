from Agent import Agent
from EagleEyeDAl import dal_get
class Get:
    @staticmethod
    def get_all_agents():
        agents = list()
        for i in dal_get("agents", "*"):
            agents.append(Agent(i["codeName"], i["realName"],i["location"], i["status"], i["missionsCompleted"]))

        return agents
