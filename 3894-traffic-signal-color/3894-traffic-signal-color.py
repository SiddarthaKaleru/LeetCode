class Solution(object):
    def trafficSignal(self, timer):
        if 30 < timer <= 90:
            return "Red"
        elif timer == 30:
            return "Orange"
        elif timer == 0:
            return "Green"
        else:
            return "Invalid"