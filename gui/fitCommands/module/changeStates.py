import wx

import gui.mainFrame
from gui import globalEvents as GE
from gui.fitCommands.calcCommands.module.localChangeStates import CalcChangeLocalModuleStatesCommand
from gui.fitCommands.helpers import InternalCommandHistory
from service.fit import Fit


class GuiChangeModuleStatesCommand(wx.Command):

    def __init__(self, fitID, mainPosition, positions, click):
        wx.Command.__init__(self, True, 'Change Module States')
        self.internalHistory = InternalCommandHistory()
        self.fitID = fitID
        self.mainPosition = mainPosition
        self.positions = positions
        self.click = click

    def Do(self):
        cmd = CalcChangeLocalModuleStatesCommand(
            fitID=self.fitID,
            mainPosition=self.mainPosition,
            positions=self.positions,
            click=self.click)
        if self.internalHistory.submit(cmd):
            Fit.getInstance().recalc(self.fitID)
            wx.PostEvent(gui.mainFrame.MainFrame.getInstance(), GE.FitChanged(fitID=self.fitID))
            return True
        return False

    def Undo(self):
        success = self.internalHistory.undoAll()
        Fit.getInstance().recalc(self.fitID)
        wx.PostEvent(gui.mainFrame.MainFrame.getInstance(), GE.FitChanged(fitID=self.fitID))
        return success