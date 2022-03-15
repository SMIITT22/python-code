class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")
        return

smitsApplication = RailwayForm()
smitsApplication.name = "smit"
smitsApplication.train = "lucago"
smitsApplication.printData()
