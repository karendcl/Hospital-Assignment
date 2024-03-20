from typing import List

import numpy as np

from logic import sim


def run_simulation_and_collect_statistics(icu_beds: int = 10, common_beds: int = 40) -> List[sim.Day_Statistics]:
    # Start the simulation
    sim.start_simulation(icu_beds, common_beds)

    # Collect statistics for each day
    day_statistics = [sim.get_day_statistics(day) for day in range(1, 28)]

    return day_statistics


def calculate_statistics(day_statistics):
    # Initialize lists to store each statistic
    initial_critical_patients = []
    initial_grave_patients = []
    initial_regular_patients = []

    new_critical_patients = []
    new_grave_patients = []
    new_regular_patients = []

    final_critical_patients = []
    final_grave_patients = []
    final_regular_patients = []

    critical_patients_cured = []
    grave_patients_cured = []
    regular_patients_cured = []

    critical_patients_died = []
    grave_patients_died = []
    regular_patients_died = []

    critical_to_grave = []
    critical_to_regular = []
    grave_to_critical = []
    grave_to_regular = []
    regular_to_critical = []
    regular_to_grave = []

    critical_ICU = []
    critical_common = []
    critical_none = []
    grave_ICU = []
    grave_common = []
    grave_none = []
    regular_ICU = []
    regular_common = []
    regular_none = []

    # Collect statistics for each day
    for stats in day_statistics:
        initial_critical_patients.append(stats['initial_critical_patients'])
        initial_grave_patients.append(stats['initial_grave_patients'])
        initial_regular_patients.append(stats['initial_regular_patients'])

        new_critical_patients.append(stats['new_critical_patients'])
        new_grave_patients.append(stats['new_grave_patients'])
        new_regular_patients.append(stats['new_regular_patients'])

        final_critical_patients.append(stats['final_critical_patients'])
        final_grave_patients.append(stats['final_grave_patients'])
        final_regular_patients.append(stats['final_regular_patients'])

        critical_patients_cured.append(stats['critical_patients_cured'])
        grave_patients_cured.append(stats['grave_patients_cured'])
        regular_patients_cured.append(stats['regular_patients_cured'])

        critical_patients_died.append(stats['critical_patients_died'])
        grave_patients_died.append(stats['grave_patients_died'])
        regular_patients_died.append(stats['regular_patients_died'])

        critical_to_grave.append(stats['critical_to_grave'])
        critical_to_regular.append(stats['critical_to_regular'])
        grave_to_critical.append(stats['grave_to_critical'])
        grave_to_regular.append(stats['grave_to_regular'])
        regular_to_critical.append(stats['regular_to_critical'])
        regular_to_grave.append(stats['regular_to_grave'])

        critical_ICU.append(stats['critical_ICU'])
        critical_common.append(stats['critical_common'])
        critical_none.append(stats['critical_none'])
        grave_ICU.append(stats['grave_ICU'])
        grave_common.append(stats['grave_common'])
        grave_none.append(stats['grave_none'])
        regular_ICU.append(stats['regular_ICU'])
        regular_common.append(stats['regular_common'])
        regular_none.append(stats['regular_none'])

    # Calculate mean, median and variance for each statistic
    statistics = {
        "initial_critical_patients": {"mean": np.mean(initial_critical_patients),
                                      "median": np.median(initial_critical_patients),
                                      "variance": np.var(initial_critical_patients)},
        "initial_grave_patients": {"mean": np.mean(initial_grave_patients), "median": np.median(initial_grave_patients),
                                   "variance": np.var(initial_grave_patients)},
        "initial_regular_patients": {"mean": np.mean(initial_regular_patients),
                                     "median": np.median(initial_regular_patients),
                                     "variance": np.var(initial_regular_patients)},

        "new_critical_patients": {"mean": np.mean(new_critical_patients), "median": np.median(new_critical_patients),
                                  "variance": np.var(new_critical_patients)},
        "new_grave_patients": {"mean": np.mean(new_grave_patients), "median": np.median(new_grave_patients),
                               "variance": np.var(new_grave_patients)},
        "new_regular_patients": {"mean": np.mean(new_regular_patients), "median": np.median(new_regular_patients),
                                 "variance": np.var(new_regular_patients)},

        "final_critical_patients": {"mean": np.mean(final_critical_patients),
                                    "median": np.median(final_critical_patients),
                                    "variance": np.var(final_critical_patients)},
        "final_grave_patients": {"mean": np.mean(final_grave_patients), "median": np.median(final_grave_patients),
                                 "variance": np.var(final_grave_patients)},
        "final_regular_patients": {"mean": np.mean(final_regular_patients), "median": np.median(final_regular_patients),
                                   "variance": np.var(final_regular_patients)},

        "critical_patients_cured": {"mean": np.mean(critical_patients_cured),
                                    "median": np.median(critical_patients_cured),
                                    "variance": np.var(critical_patients_cured)},
        "grave_patients_cured": {"mean": np.mean(grave_patients_cured), "median": np.median(grave_patients_cured),
                                 "variance": np.var(grave_patients_cured)},
        "regular_patients_cured": {"mean": np.mean(regular_patients_cured), "median": np.median(regular_patients_cured),
                                   "variance": np.var(regular_patients_cured)},

        "critical_patients_died": {"mean": np.mean(critical_patients_died), "median": np.median(critical_patients_died),
                                   "variance": np.var(critical_patients_died)},
        "grave_patients_died": {"mean": np.mean(grave_patients_died), "median": np.median(grave_patients_died),
                                "variance": np.var(grave_patients_died)},
        "regular_patients_died": {"mean": np.mean(regular_patients_died), "median": np.median(regular_patients_died),
                                  "variance": np.var(regular_patients_died)},

        "critical_to_grave": {"mean": np.mean(critical_to_grave), "median": np.median(critical_to_grave),
                              "variance": np.var(critical_to_grave)},
        "critical_to_regular": {"mean": np.mean(critical_to_regular), "median": np.median(critical_to_regular),
                                "variance": np.var(critical_to_regular)},
        "grave_to_critical": {"mean": np.mean(grave_to_critical), "median": np.median(grave_to_critical),
                              "variance": np.var(grave_to_critical)},
        "grave_to_regular": {"mean": np.mean(grave_to_regular), "median": np.median(grave_to_regular),
                             "variance": np.var(grave_to_regular)},
        "regular_to_critical": {"mean": np.mean(regular_to_critical), "median": np.median(regular_to_critical),
                                "variance": np.var(regular_to_critical)},
        "regular_to_grave": {"mean": np.mean(regular_to_grave), "median": np.median(regular_to_grave),
                             "variance": np.var(regular_to_grave)},

        "critical_ICU": {"mean": np.mean(critical_ICU), "median": np.median(critical_ICU),
                         "variance": np.var(critical_ICU)},
        "critical_common": {"mean": np.mean(critical_common), "median": np.median(critical_common),
                            "variance": np.var(critical_common)},
        "critical_none": {"mean": np.mean(critical_none), "median": np.median(critical_none),
                          "variance": np.var(critical_none)},
        "grave_ICU": {"mean": np.mean(grave_ICU), "median": np.median(grave_ICU), "variance": np.var(grave_ICU)},
        "grave_common": {"mean": np.mean(grave_common), "median": np.median(grave_common),
                         "variance": np.var(grave_common)},
        "grave_none": {"mean": np.mean(grave_none), "median": np.median(grave_none), "variance": np.var(grave_none)},
        "regular_ICU": {"mean": np.mean(regular_ICU), "median": np.median(regular_ICU),
                        "variance": np.var(regular_ICU)},
        "regular_common": {"mean": np.mean(regular_common), "median": np.median(regular_common),
                           "variance": np.var(regular_common)},
        "regular_none": {"mean": np.mean(regular_none), "median": np.median(regular_none),
                         "variance": np.var(regular_none)},
    }

    return statistics


def statistics_to_md_table(statistics):
    # Initialize the table with headers
    table = "|Statistic|Mean|Median|Variance|\n|---|---|---|---|\n"

    # Iterate over the statistics dictionary
    for stat, values in statistics.items():
        # Add a row to the table for each statistic
        table += f"|{stat}|{values['mean']}|{values['median']}|{values['variance']}|\n"

    return table


day_statistics = run_simulation_and_collect_statistics()
statistics = calculate_statistics(day_statistics)
md_table = statistics_to_md_table(statistics)
with open('statistics.md', 'w') as f:
    f.write(md_table)
