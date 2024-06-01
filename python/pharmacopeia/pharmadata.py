class Drug:
    def __init__(self, name, drug_type, uses, data, controlled, classuk, classpers, sold, drug_brand):
        self.name = name
        self.type = drug_type
        self.uses = uses
        self.data = data
        self.controlled = controlled
        self.brand = drug_brand
        self.sold = sold

        if self.controlled == True:
            self.controlled = "it is a controlled substance"
        elif self.controlled == False:
            self.controlled = "it is not a controlled substance"
        else:
            self.controlled = "it is unknown whether it is controlled"

        self.classuk = classuk
        self.classpers = classpers

    def list(self):
        print(f"{self.name} is {self.type}, Mostly used for {self.uses}, {self.controlled} and is therefore {self.classuk} in the UK.")
        print(f"I rated it {self.classpers} on the Danger Scale.")

        if self.sold != "Null":
            print(f"It is sold under {self.brand}.")
        else:
            print("It is not sold.")

        print(f"{self.data}")

Morphine = Drug("Morphine", "Opiate", "chronic pain and recreation", "Around 70% of Opium-Poppy produced Morphine is used to synthesise other Opioids, such as Hydromorphone and Oxymorphone. \nMost of Illict Morphine is used to synthesise Diamorphine, commonly known as Heroin.\nMorphine is addictive and prone to abuse. When the dosage is stopped suddenly, patients may experience withdrawal symptoms.", True, "Class A", "A2[b]-rx", "Yes", "MST, Zomorph, Sevredol, Morphgesic, MXL, and Oramorph")
Diacetylmorphine = Drug("Diacetylmorphine", "Semi-synthetic Opioid derived from Morphine", "recreationally but in the UK it is used for end of life pain management", "it is highly addictive and very prone to abuse. \nAn overdose may produce respiratory depression and can be reversed by Naloxone (Narcan) \nin recent years, illicit Opioids are being cut ith Fentanyl, Heroin being commonly cut.\nIt is often injected intravenously, leading to blood-bourne diseases, but some Heroin users insufflate or smoke Heroin.", True, "Class A", "A1[a]-rxp", "Yes", "Diamorphine and Heroin")
Amphetamine = Drug("Amphetamine", "Phenethylamine/Amphetamine based Stimulant and Euphoriant", "to treat ADHD, Narcolepsy and Obesity. Some people use it recreationally or as a 'Smart Drug'", "Amphetamine increases Dopamine and Norepinephrine in the brain. At the recommended doses, it enduces Euphoria, increased sex drive, and increased wakefulness.\nIt produces physical effects such as: resistance to fatigue, improved reaction time and stronger muscles.\nLarger doses of Amphetamine may result in rapid Muscle breakdown and impaired cognitive function.\nVery high doses produce psychosis.\nAmphetamine is addictive and a risk in long-term use. Although, at therapeutic doses this appears to be unlikely.", True, "Class B", "B2[a]-rx", "Yes", "Adderall")
Methylphenidate = Drug("Methylphenidate", "Phenidate/Ritalinic acid based Stimulant", "treat ADHD, and in rare cases, Narcolepsy. Some people use it recreationally or as a cognitive enhancer ('Smart Drug')", "It the primary ADHD medication in the UK and it works in the same way as Adderall (Amphetamine) by increasing Dopamine and Norepinephrine.\nWhen used recreationally, it is taken orally, insufflated, or injected. This can lead to overdoses, combatted with Benzodiazepines.", True, "Class B", "B3[b]-rx", "Yes", "Ritalin, Concerta")

def run(name):
    if name == Morphine.name:
        Morphine.list()
    elif name == Diacetylmorphine.name:
        Diacetylmorphine.list()
    elif name == Amphetamine.name:
        Amphetamine.list()
    elif name == Methylphenidate.name:
        Methylphenidate.list()

name_drugs = [Morphine.name,
              Diacetylmorphine.name,
              Amphetamine.name,
              Methylphenidate.name]