from Person import Patient, Beds, ICU_Bed, Common_Bed
import numpy as np
from scipy.optimize import linear_sum_assignment
import queue

class Day_Statisitcs:
    def __init__(self, day):
        self.day = day
        self.initial_critical_patients = 0
        self.initial_grave_patients = 0
        self.initial_regular_patients = 0

        self.final_critical_patients = 0
        self.final_grave_patients = 0
        self.final_regular_patients = 0

        self.critical_patients_cured = 0
        self.grave_patients_cured = 0
        self.regular_patients_cured = 0

        self.critical_patients_died = 0
        self.grave_patients_died = 0
        self.regular_patients_died = 0

        self.assignments = ''

    def __str__(self):

        return (f"\n---------------------\nDay {self.day} \n"
                f" Critical: {self.initial_critical_patients} -> {self.final_critical_patients} \n"
                f"- Grave: {self.initial_grave_patients} -> {self.final_grave_patients} \n"
                f"- Regular: {self.initial_regular_patients} -> {self.final_regular_patients}"
                f"- Critical Patients Cured: {self.critical_patients_cured} \n"
                f"- Grave Patients Cured: {self.grave_patients_cured} \n"
                f"- Regular Patients Cured: {self.regular_patients_cured} \n"
                f"- Critical Patients Died: {self.critical_patients_died} \n"
                f"- Grave Patients Died: {self.grave_patients_died} \n"
                f"- Regular Patients Died: {self.regular_patients_died} \n"
                f"- Assignments: {self.assignments}")







class Simulation:
    def __init__(self, n_icu_beds, n_common_beds, n_patients=40):
        self.n_icu_beds = n_icu_beds
        self.n_common_beds = n_common_beds
        self.n_patients = n_patients
        self.patients = []
        self.beds = []
        self.costs = np.zeros((n_patients, n_icu_beds + n_common_beds))
        self.simulate()


    def initialize(self):
        n_critical_patients = self.n_patients // 4
        n_grave_patients = self.n_patients // 4
        n_regular_patients = self.n_patients - n_critical_patients - n_grave_patients

        for i in range(n_grave_patients):
            self.patients.append(Patient(i, "grave"))
        for i in range(n_grave_patients, n_grave_patients + n_critical_patients):
            self.patients.append(Patient(i, "critical"))
        for i in range(n_grave_patients + n_critical_patients, self.n_patients):
            self.patients.append(Patient(i, "regular"))

        for i in range(self.n_icu_beds):
            self.beds.append(ICU_Bed(i))
        for i in range(self.n_icu_beds, self.n_icu_beds + self.n_common_beds):
            self.beds.append(Common_Bed(i))


    def set_costs_matrix(self):
        self.costs = np.zeros((len(self.patients), self.n_icu_beds + self.n_common_beds))
        for i, p in enumerate(self.patients):
            for j, n in enumerate(self.beds):
                self.costs[i, j] = self.calculate_cost(p, n)

    def calculate_cost(self, patient, bed):
        if patient.status == "critical" and bed.typee == "ICU":
            return 0
        elif patient.status == "critical" and bed.typee == "common":
            return 1
        elif patient.status == "grave" and bed.typee == "ICU":
            return 2
        elif patient.status == "grave" and bed.typee == "common":
            return 3
        elif patient.status == "regular" and bed.typee == "common":
            return 4
        elif patient.status == "regular" and bed.typee == "ICU":
            return 5

    def assign_beds(self):
        row_ind, col_ind = linear_sum_assignment(self.costs)
        for i in range(len(row_ind)):
            self.patients[row_ind[i]].bed_assigned = self.beds[col_ind[i]]


    def add_new_patients(self):
        new_critical_patients = np.random.poisson(0.1)
        new_grave_patients = np.random.poisson(0.1)
        new_regular_patients = np.random.poisson(0.1)

        for i in range(new_critical_patients):
            self.patients.append(Patient(self.n_patients, "critical"))
            self.n_patients += 1
        for i in range(new_grave_patients):
            self.patients.append(Patient(self.n_patients, "grave"))
            self.n_patients += 1
        for i in range(new_regular_patients):
            self.patients.append(Patient(self.n_patients, "regular"))
            self.n_patients += 1

    def simulate(self):
        self.initialize()
        for k in range(30):
            stats = Day_Statisitcs(k)
            stats.initial_critical_patients = sum([1 for i in self.patients if i.status == "critical"])
            stats.initial_grave_patients = sum([1 for i in self.patients if i.status == "grave"])
            stats.initial_regular_patients = sum([1 for i in self.patients if i.status == "regular"])

            self.set_costs_matrix()
            self.assign_beds()

            crit_icu = 0
            crit_common = 0
            grave_icu = 0
            grave_common = 0
            reg_icu = 0
            reg_common = 0
            for i in self.patients:
                if i.status == "critical":
                    if i.bed_assigned is not None and i.bed_assigned.typee == "ICU":
                        crit_icu += 1
                    elif i.bed_assigned is not None and i.bed_assigned.typee == "common":
                        crit_common += 1
                elif i.status == "grave":
                    if i.bed_assigned is not None and i.bed_assigned.typee == "ICU":
                        grave_icu += 1
                    elif i.bed_assigned is not None and i.bed_assigned.typee == "common":
                        grave_common += 1
                elif i.status == "regular":
                    if i.bed_assigned is not None and i.bed_assigned.typee == "ICU":
                        reg_icu += 1
                    elif i.bed_assigned is not None and i.bed_assigned.typee == "common":
                        reg_common += 1


            stats.assignments = f"Critical: ICU: {crit_icu}, Common: {crit_common} \nGrave: ICU: {grave_icu}, Common: {grave_common} \nRegular: ICU: {reg_icu}, Common: {reg_common}"


            new_p = []
            for i in self.patients:
                i.interact()
                if i.is_cured:
                    self.n_patients -= 1
                    status = f'{i.status}_patients_cured'
                    stats.__dict__[status] += 1
                elif i.is_dead:
                    self.n_patients -= 1
                    status = f'{i.status}_patients_died'
                    stats.__dict__[status] += 1
                else:
                    new_p.append(i)

            self.patients = new_p

            self.add_new_patients()

            stats.final_critical_patients = sum([1 for i in self.patients if i.status == "critical"])
            stats.final_grave_patients = sum([1 for i in self.patients if i.status == "grave"])
            stats.final_regular_patients = sum([1 for i in self.patients if i.status == "regular"])



            print(stats)



sim = Simulation(5, 10)