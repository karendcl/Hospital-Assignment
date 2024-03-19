from Person import Patient, Beds, ICU_Bed, Common_Bed
import numpy as np
from scipy.optimize import linear_sum_assignment
import queue
import random


simulat = []
class Day_Statistics:
    def __init__(self, day):
        self.day = day
        self.initial_critical_patients = 0
        self.initial_grave_patients = 0
        self.initial_regular_patients = 0

        self.new_critical_patients = 0
        self.new_grave_patients = 0
        self.new_regular_patients = 0

        self.final_critical_patients = 0
        self.final_grave_patients = 0
        self.final_regular_patients = 0

        self.critical_patients_cured = 0
        self.grave_patients_cured = 0
        self.regular_patients_cured = 0

        self.critical_patients_died = 0
        self.grave_patients_died = 0
        self.regular_patients_died = 0

        self.critical_to_grave = 0
        self.critical_to_regular = 0
        self.grave_to_critical = 0
        self.grave_to_regular = 0
        self.regular_to_critical = 0
        self.regular_to_grave = 0

        self.critical_ICU = 0
        self.critical_common = 0
        self.critical_none = 0
        self.grave_ICU = 0
        self.grave_common = 0
        self.grave_none = 0
        self.regular_ICU = 0
        self.regular_common = 0
        self.regular_none = 0

        self.assignments = []

    def __str__(self):

        return (f"\n---------------------\nDay {self.day} \n"
                f"- Critical: {self.initial_critical_patients} -> {self.final_critical_patients} \n"
                f"- Grave: {self.initial_grave_patients} -> {self.final_grave_patients} \n"
                f"- Regular: {self.initial_regular_patients} -> {self.final_regular_patients} \n"
                f"- New Patients: \n"
                f"- Critical: {self.new_critical_patients} \n"
                f"- Grave: {self.new_grave_patients} \n"
                f"- Regular: {self.new_regular_patients} \n"
                f"- Critical Patients Cured: {self.critical_patients_cured} \n"
                f"- Grave Patients Cured: {self.grave_patients_cured} \n"
                f"- Regular Patients Cured: {self.regular_patients_cured} \n"
                f"- Critical Patients Died: {self.critical_patients_died} \n"
                f"- Grave Patients Died: {self.grave_patients_died} \n"
                f"- Regular Patients Died: {self.regular_patients_died} \n"
                f"- Evolutions:\n"
                f"- Critical to Grave: {self.critical_to_grave} \n"
                f"- Critical to Regular: {self.critical_to_regular} \n"
                f"- Grave to Critical: {self.grave_to_critical} \n"
                f"- Grave to Regular: {self.grave_to_regular} \n"
                f"- Regular to Critical: {self.regular_to_critical} \n"
                f"- Regular to Grave: {self.regular_to_grave} \n"
                f"- Assignments: \n"
                f"- Critical: ICU: {self.critical_ICU}, Common: {self.critical_common}, None: {self.critical_none} \n"
                f"- Grave: ICU: {self.grave_ICU}, Common: {self.grave_common}, None: {self.grave_none} \n"
                f"- Regular: ICU: {self.regular_ICU}, Common: {self.regular_common}, None: {self.regular_none} \n"
                f"- Assignments: \n"
                # f"{'\n'.join(self.assignments)} \n"
                f"---------------------\n")


class Simulation:
    def __init__(self, n_icu_beds, n_common_beds, n_patients=40):
        self.n_icu_beds = n_icu_beds
        self.n_common_beds = n_common_beds
        self.n_patients = n_patients
        self.patients = []
        self.beds = []
        self.daily_stats = []
        self.costs = np.zeros((n_patients, n_icu_beds + n_common_beds))
        self.simulate()

    def generate_patient(self, index):
        age = np.random.choice(["young_adult", "adult", "senior"], p=[0.3, 0.4, 0.3])
        status = np.random.choice(["grave", "critical", "regular"], p=[0.3, 0.2, 0.5])
        return Patient(index, status, age)

    def initialize(self):
        pat = [self.generate_patient(i) for i in range(self.n_patients)]
        self.patients = pat

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

        if patient.age_group == 'senior' and patient.status == "critical" and bed.typee == "ICU":
            return 1
        elif patient.age_group == 'senior' and patient.status == "critical" and bed.typee == "common":
            return 4
        elif patient.age_group == 'senior' and patient.status == "grave" and bed.typee == "ICU":
            return 7
        elif patient.age_group == 'senior' and patient.status == "grave" and bed.typee == "common":
            return 10
        elif patient.age_group == 'senior' and patient.status == "regular" and bed.typee == "ICU":
            return 16
        elif patient.age_group == 'senior' and patient.status == "regular" and bed.typee == "common":
            return 13

        elif patient.age_group == 'adult' and patient.status == "critical" and bed.typee == "ICU":
            return 2
        elif patient.age_group == 'adult' and patient.status == "critical" and bed.typee == "common":
            return 5
        elif patient.age_group == 'adult' and patient.status == "grave" and bed.typee == "ICU":
            return 8
        elif patient.age_group == 'adult' and patient.status == "grave" and bed.typee == "common":
            return 11
        elif patient.age_group == 'adult' and patient.status == "regular" and bed.typee == "ICU":
            return 17
        elif patient.age_group == 'adult' and patient.status == "regular" and bed.typee == "common":
            return 14

        elif patient.age_group == 'young_adult' and patient.status == "critical" and bed.typee == "ICU":
            return 3
        elif patient.age_group == 'young_adult' and patient.status == "critical" and bed.typee == "common":
            return 6
        elif patient.age_group == 'young_adult' and patient.status == "grave" and bed.typee == "ICU":
            return 9
        elif patient.age_group == 'young_adult' and patient.status == "grave" and bed.typee == "common":
            return 12
        elif patient.age_group == 'young_adult' and patient.status == "regular" and bed.typee == "ICU":
            return 18
        elif patient.age_group == 'young_adult' and patient.status == "regular" and bed.typee == "common":
            return 15



    def assign_beds(self):

        assignments = []
        row_ind, col_ind = linear_sum_assignment(self.costs)
        for i in range(len(row_ind)):
            self.patients[row_ind[i]].bed_assigned = self.beds[col_ind[i]]
            assignments.append( f'{str(self.patients[row_ind[i]])} -> {str(self.beds[col_ind[i]])}')

        #set to None the ones not assigned
        for i in range(len(self.patients)):
            if i not in row_ind:
                self.patients[i].bed_assigned = None

        return assignments



    def add_new_patients(self):
        new_p = random.randint(0, 20)
        new_critical_patients = 0
        new_grave_patients = 0
        new_regular_patients = 0

        for i in range(new_p):
            np = self.generate_patient(self.n_patients)
            self.patients.append(np)
            self.n_patients += 1
            if np.status == "critical":
                new_critical_patients += 1
            elif np.status == "grave":
                new_grave_patients += 1
            else:
                new_regular_patients += 1

        return new_critical_patients, new_grave_patients, new_regular_patients


    def simulate(self):
        self.initialize()
        for k in range(30):
            stats = Day_Statistics(k)
            stats.initial_critical_patients = sum([1 for i in self.patients if i.status == "critical"])
            stats.initial_grave_patients = sum([1 for i in self.patients if i.status == "grave"])
            stats.initial_regular_patients = sum([1 for i in self.patients if i.status == "regular"])

            self.set_costs_matrix()
            assignm = self.assign_beds()
            stats.assignments = assignm

            for i in self.patients:
                stat = i.status
                bed = 'none' if i.bed_assigned is None else i.bed_assigned.typee
                var = f'{stat}_{bed}'
                stats.__dict__[var] += 1
                

            new_p = []
            for i in self.patients:
                old_status = i.status
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
                    new_status = i.status
                    if old_status != new_status:
                        stats.__dict__[f'{old_status}_to_{new_status}'] += 1

            self.patients = new_p

            new_critical, new_grave, new_regular = self.add_new_patients()
            stats.new_critical_patients = new_critical
            stats.new_grave_patients = new_grave
            stats.new_regular_patients = new_regular

            stats.final_critical_patients = sum([1 for i in self.patients if i.status == "critical"])
            stats.final_grave_patients = sum([1 for i in self.patients if i.status == "grave"])
            stats.final_regular_patients = sum([1 for i in self.patients if i.status == "regular"])

            self.daily_stats.append(stats)


def start_simulation(icu_beds, common_beds):
    global simulat
    try:
        sim = Simulation(icu_beds, common_beds)
        simulat = sim.daily_stats
        return True
    except Exception as e:
        print(e)
        return False

def get_day_statistics(day):
    return [i.__dict__ for i in simulat if i.day == day][0]

def get_deaths():
    return [x.grave_patients_died + x.critical_patients_died + x.regular_patients_died for x in simulat]

def get_cured():
    return [x.grave_patients_cured + x.critical_patients_cured + x.regular_patients_cured for x in simulat]

def get_patients_better():
    return [x.critical_to_grave + x.critical_to_regular + x.grave_to_regular for x in simulat]

def get_patients_worse():
    return [x.grave_to_critical + x.regular_to_critical + x.regular_to_grave for x in simulat]


