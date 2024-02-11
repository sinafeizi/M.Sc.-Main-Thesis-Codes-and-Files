import os
from time import time
from get_all_examples import list_of_slp_s, list_of_to_cover_flights_lists
from PSO_functions import run_pso
from ACO import run_aco
from test import run_aco_old
from GA_functions import run_evolution
from GA_2018 import run_evolution_2018
def shutdown_pc():
   os.system("shutdown /s /t 1")
runtime = 600
for c1 in range(len(list_of_slp_s)):
    for c2 in range(10):
        run_pso(list_of_slp_s[c1], list_of_to_cover_flights_lists[c1], 1, 2, 7, 6.5, 20, 100000, time(), runtime, c1, c2)
        run_aco(list_of_slp_s[c1], list_of_to_cover_flights_lists[c1], 15, 100000, 1, 0.85, time(), runtime, c1, c2)
        run_aco_old(list_of_slp_s[c1], list_of_to_cover_flights_lists[c1], 25, 100000, 100, 0.95, 1, 8, 0.0003, time(), runtime, c1, c2)
        run_evolution(list_of_slp_s[c1], list_of_to_cover_flights_lists[c1], 0.1, 50, 15, 100000, time(), runtime, c1, c2)
        run_evolution_2018(list_of_slp_s[c1], list_of_to_cover_flights_lists[c1], 0.1, 40, 100000, time(), runtime, c1, c2)
shutdown_pc()
