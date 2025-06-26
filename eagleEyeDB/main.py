from Agent import Agent
from StatusType import StatusType
import Queries
from Queries.add import Add
from Queries.get import Get

agent1 = Agent("falafel", "elazar", "jerusalem", StatusType.active.value, "54")

if __name__ == "__main__":
    # Queries.add.Add.add_agent(agent1)
    agents = Queries.get.Get.get_all_agents()
    for i in agents:
        print(i)

