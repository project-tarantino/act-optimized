"""File to read in the results of cProfile and print."""

import pstats
from pstats import SortKey

PROFILE_RESULTS_FILE = "profilestats.txt"

p = pstats.Stats(PROFILE_RESULTS_FILE)
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
