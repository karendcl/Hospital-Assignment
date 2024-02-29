import numpy as np
from scipy.optimize import linear_sum_assignment
import random

class Patient:
    def __init__(self, index, status, bed_assigned=None):
        self.index = index
        self.status = status
        self.bed_assigned = bed_assigned
        self.is_cured = False
        self.is_dead = False

    def __str__(self):
        return f"Patient {self.index} with status {self.status} and bed {self.bed_assigned.typee}" if self.bed_assigned is not 'None' else f"Patient {self.index} with status {self.status} and bed not assigned"

    def interact(self):
        if self.bed_assigned is None:
            return
        if self.status == 'critical' and self.bed_assigned.typee == 'ICU':
            self.is_cured = random.random() < 0.6
        elif self.status == 'critical' and self.bed_assigned.typee == 'common':
            self.is_cured = random.random() < 0.4
        elif self.status == 'grave' and self.bed_assigned.typee == 'ICU':
            self.is_cured = random.random() < 0.8
        elif self.status == 'grave' and self.bed_assigned.typee == 'common':
            self.is_cured = random.random() < 0.7
        elif self.status == 'regular' and self.bed_assigned.typee == 'common':
            self.is_cured = random.random() < 0.9
        elif self.status == 'regular' and self.bed_assigned.typee == 'ICU':
            self.is_cured = True


class Beds:
    def __init__(self, index, typee):
        self.index = index
        self.typee = typee

    def __str__(self):
        return f"Bed {self.index} of type {self.typee}"

class ICU_Bed(Beds):
    def __init__(self, index):
        super().__init__(index, "ICU")

class Common_Bed(Beds):
    def __init__(self, index):
        super().__init__(index, "common")

def initialize(n_icu_beds, n_common_beds, n_patients=40):
    n_critical_patients = n_patients // 4
    n_grave_patients = n_patients // 4
    n_regular_patients = n_patients - n_critical_patients - n_grave_patients

    patients = []
    for i in range(n_grave_patients):
        patients.append(Patient(i, "grave"))
    for i in range(n_grave_patients, n_grave_patients + n_critical_patients):
        patients.append(Patient(i, "critical"))
    for i in range(n_grave_patients + n_critical_patients, n_patients):
        patients.append(Patient(i, "regular"))

    beds = []
    for i in range(n_icu_beds):
        beds.append(ICU_Bed(i))
    for i in range(n_icu_beds, n_icu_beds + n_common_beds):
        beds.append(Common_Bed(i))

    costs = np.zeros((n_patients, n_icu_beds + n_common_beds))

    #priority orders, costs should be assigned according to the priority
    #critical patients in ICU
    #critical patients in common
    #grave patients in ICU
    #grave patients in common
    #regular patients in common
    #regular patients in ICU

    for i in patients:
        for j in beds:
            if i.status == 'critical' and j.typee == 'ICU':
                costs[i.index][j.index] = 1
            elif i.status == 'grave' and j.typee == 'ICU':
                costs[i.index][j.index] = 20
            elif i.status == 'regular' and j.typee == 'ICU':
                costs[i.index][j.index] = 100
            elif i.status == 'critical' and j.typee == 'common':
                costs[i.index][j.index] = 2
            elif i.status == 'grave' and j.typee == 'common':
                costs[i.index][j.index] = 10
            elif i.status == 'regular' and j.typee == 'common':
                costs[i.index][j.index] = 90

    return patients,beds, costs


def assign(patients, beds, costs):

    row_ind, col_ind = linear_sum_assignment(costs)
    for i in range(len(row_ind)):
        patients[row_ind[i]].bed_assigned = beds[col_ind[i]]

def initial_assign():
    n_icu_beds = 6
    n_common_beds = 20
    patients, beds, costs = initialize(n_icu_beds, n_common_beds)
    for i in range(len(patients)):
        print(patients[i])
    for i in range(len(beds)):
        print(beds[i])
    assign(patients, beds, costs)
    for i in range(len(patients)):
        print(patients[i])














