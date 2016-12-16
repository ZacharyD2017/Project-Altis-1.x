#from toontown.building import DistributedChairmanElevatorAI
from toontown.building import FADoorCodes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
#from toontown.coghq.DistributedBoardOfficeElevatorExtAI import DistributedBoardOfficeElevatorExtAI
from toontown.hood import CogHQAI
#from toontown.suit import DistributedBoardbotBossAI
from toontown.suit import DistributedSuitPlannerAI
from toontown.toonbase import ToontownGlobals


class BoardbotHQAI(CogHQAI.CogHQAI):
    def __init__(self, air):
        """
        CogHQAI.CogHQAI.__init__(
            self, air, ToontownGlobals.BoardbotHQ, ToontownGlobals.BoardbotLobby,
            FADoorCodes.BD_DISGUISE_INCOMPLETE,
            DistributedChairmanElevatorAI.DistributedChairmanElevatorAI,
            DistributedBoardbotBossAI.DistributedBoardbotBossAI)

        """
            
        self.boardOfficeElevators = []
        self.officeBoardingParty = None
        self.suitPlanners = []

        self.startup()

    def startup(self):
        #CogHQAI.CogHQAI.startup(self)
        pass
