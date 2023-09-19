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
    
    def I_prayed(self, prayer, times):
        try:
            if (prayer == "fajr"):
                self.fajr -= times
            elif (prayer == "zuhr"):
                self.zuhr -= times
            elif (prayer == "asr"):
                self.asr -= times
            elif (prayer == "maghrib"):
                self.maghrib -= times
            elif (prayer == "ishaa"):
                self.ishaa -= times
            print(f"\nYou prayed {prayer} for {times*2} rakaats 😊 and here is the list of still left missed prayers:")
            self.show_me_missed_prayers()
        except TypeError:
            print("Please make sure you are passing the right formats of parameters")
    
    def I_missed_again(self, prayer, times):
        try:
            if (prayer == "fajr"):
                self.fajr += times
            elif (prayer == "zuhr"):
                self.zuhr += times
            elif (prayer == "asr"):
                self.asr += times
            elif (prayer == "maghrib"):
                self.maghrib += times
            elif (prayer == "ishaa"):
                self.ishaa += times
            print(f"\nYou missed again {prayer} for {times*2} rakaats 😒 and here is the list of missed prayers:")
            self.show_me_missed_prayers()
        except TypeError:
            print("Please make sure you are passing the right formats of parameters")

Ismoil = MissedPrayers({"fajr": 3, "zuhr": 1, "asr": 2, "maghrib": 0, "ishaa": 0})
Ismoil.show_me_missed_prayers()
Ismoil.I_prayed("fajr", 2)
Ismoil.I_missed_again("fajr", 5)