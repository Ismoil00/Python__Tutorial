class MissedPrayers:
    def __init__(self, prayers):
        try:
            self.fajr = prayers["fajr"]
            self.zuhr = prayers["zuhr"]
            self.asr = prayers["asr"]
            self.maghrib = prayers["maghrib"]
            self.ishaa = prayers["ishaa"]
        except TypeError:
            print("Please, while creating a Class Instance pass dictionaries only!!!")

    def show_me_missed_prayers(self):
        print(f"\nHere are your missed prayers:\n- Fajr {self.fajr};\n- Zuhr {self.zuhr};\n- Asr {self.asr};\n- Maghrib {self.maghrib};\n- Ishaa {self.ishaa};")
    
    def I_prayed(self, prayer, rakaat):
        try:
            if (prayer == "fajr"):
                self.fajr -= rakaat
            elif (prayer == "zuhr"):
                self.zuhr -= rakaat
            elif (prayer == "asr"):
                self.asr -= rakaat
            elif (prayer == "maghrib"):
                self.maghrib -= rakaat
            elif (prayer == "ishaa"):
                self.ishaa -= rakaat
            print(f"\nYou prayed {prayer} for {rakaat} rakaats and here is the list of still left missed prayers:")
            self.show_me_missed_prayers()
        except TypeError:
            print("Please make sure you are passing the right formats of parameters")

Ismoil = MissedPrayers({"fajr": 3, "zuhr": 1, "asr": 2, "maghrib": 0, "ishaa": 0})
Ismoil.show_me_missed_prayers()
Ismoil.I_prayed("fajr", 2)