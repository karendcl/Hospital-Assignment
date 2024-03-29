import numpy as np
from scipy.optimize import linear_sum_assignment
import random


class Patient:
    def __init__(self, index, status,age_group, bed_assigned=None):
        self.index = index
        self.status = status
        self.bed_assigned = bed_assigned
        self.is_cured = False
        self.is_dead = False
        self.age_group = age_group

    def __str__(self):
        return f'{self.status} {self.age_group}'

    def interact(self):
        if self.bed_assigned is None:
            return
        x = random.random()

        if self.status == 'critical' and self.bed_assigned.typee == 'ICU':
            if x <= 0.3:
                self.is_cured = True
            elif 0.3 < x <= 0.5:
                self.is_dead = True
            elif 0.5 < x <= 0.8:
                self.status = 'grave'
            elif 0.8 < x <= 0.9:
                self.status = 'regular'

        elif self.status == 'critical' and self.bed_assigned.typee == 'common':
            if x <= 0.1:
                self.is_cured = True
            elif 0.1 < x <= 0.6:
                self.is_dead = True
            elif 0.6 < x <= 0.8:
                self.status = 'grave'
            elif 0.8 < x <= 0.9:
                self.status = 'regular'

        elif self.status == 'grave' and self.bed_assigned.typee == 'ICU':
            if x <= 0.5:
                self.is_cured = True
            elif 0.5 < x <= 0.6:
                self.is_dead = True
            elif 0.6 < x <= 0.7:
                self.status = 'critical'
            elif 0.7 < x <= 0.9:
                self.status = 'regular'

        elif self.status == 'grave' and self.bed_assigned.typee == 'common':
            if x <= 0.2:
                self.is_cured = True
            elif 0.2 < x <= 0.5:
                self.is_dead = True
            elif 0.5 < x <= 0.7:
                self.status = 'critical'
            elif 0.7 < x <= 0.9:
                self.status = 'regular'

        elif self.status == 'regular' and self.bed_assigned.typee == 'common':
            if x <= 0.4:
                self.is_cured = True
            elif 0.4 < x <= 0.5:
                self.is_dead = True
            elif 0.5 < x <= 0.7:
                self.status = 'critical'
            elif 0.7 < x <= 0.9:
                self.status = 'grave'
        elif self.status == 'regular' and self.bed_assigned.typee == 'ICU':
            if x <= 0.7:
                self.is_cured = True
            elif 0.7 < x <= 0.75:
                self.is_dead = True
            elif 0.75 < x <= 0.8:
                self.status = 'critical'
            elif 0.8 < x <= 0.9:
                self.status = 'grave'


class Beds:
    def __init__(self, index, typee):
        self.index = index
        self.typee = typee

    def __str__(self):
        return f"Bed type {self.typee}"

class ICU_Bed(Beds):
    def __init__(self, index):
        super().__init__(index, "ICU")

class Common_Bed(Beds):
    def __init__(self, index):
        super().__init__(index, "common")










