# CS355 - Probability
# Program VI - A Tale of Two Airlines
# Hunter Wesson
# hcwesson@uab.edu

import numpy as np


# Calculates a single flight duration based on flight probability data
def get_flight_time(depart_time, mu, sd):
    flight_time = np.random.normal(mu, sd, 1)
    return flight_time


# Returns arrival time or stranded flag for one passenger through a system of cities
def transit(init_flight=(), mid_flights=[], end_flights=[]):
    time = init_flight[0] + get_flight_time(*init_flight)
    tries = 0
    mid_flight_num = len(mid_flights)
    for flight in mid_flights:
        new_time = get_flight_time(*flight)
        if time < flight[0]:
            time = time + new_time
            break
        tries += 1
        if tries >= mid_flight_num:
            return -1   # Indicates stranded passenger; removed from transit time calculation
    tries = 0
    end_flight_num = len(end_flights)
    for flight in end_flights:
        new_time = get_flight_time(*flight)
        if time < flight[0]:
            time = time + new_time
            break
        tries += 1
        if tries >= end_flight_num:
            return -1   # Indicates stranded passenger; removed from transit time calculation
    return time


# Flights defined as tuples

# Airline 1 flights
a1 = (8, 4, .4)
b0 = (12.5, 4, .4)
b1 = (13, 4, .4)
b = [b0, b1]
c0 = (17, 3.5, .4)
c1 = (17.5, 3.5, .4)
c2 = (18, 3.5, .4)
c = [c0, c1, c2]

# Airline 2 flights
a2 = (8, 3.5, .6)
e0 = (12, 4, .6)
e1 = (12.5, 4, .6)
e = [e0, e1]
f0 = (16.5, 3.5, .6)
f1 = (17, 3.5, .6)
f2 = (17.5, 3.5, 6)
f = [f0, f1, f2]

passengers_per_airline = 10000
a_arrivals = []
a_stranded = 0
b_arrivals = []
b_stranded = 0

# Simulates transits for (passengers_per_airline) passengers.
for i in range(0, passengers_per_airline):
    a_transit = transit(a1, b, c)
    if not a_transit == -1:
        a_arrivals.append(float(a_transit))
    else:
        a_stranded += 1

    b_transit = transit(a2, e, f)
    if not b_transit == -1:
        b_arrivals.append(float(b_transit))
    else:
        b_stranded += 1

a_arr = np.asarray(a_arrivals)
b_arr = np.asarray(b_arrivals)

a_30over = (a_arr > 21).sum()
b_30over = (b_arr > 20).sum()
a_30under = passengers_per_airline - a_30over
b_30under = passengers_per_airline - b_30over
prob_a_30under = float(a_30under / passengers_per_airline)
prob_b_30under = float(b_30under / passengers_per_airline)

a_mean = np.round(np.mean(a_arrivals), 4)
a_mean_hrs = int(np.floor(a_mean))              # Converting to standard clock notation
a_mean_mins = int(60 * (a_mean - a_mean_hrs))

b_mean = np.round(np.mean(b_arrivals), 4)
b_mean_hrs = int(np.floor(b_mean))              # Converting to standard clock notation
b_mean_mins = int(60 * (b_mean - b_mean_hrs))

# Output begins
print('\n For %s runs:' % passengers_per_airline)
print('\nAverage arrival time on Airline 1: %s:%s' % (a_mean_hrs, a_mean_mins))
print('Probability of a 30 minute overrun or less: %s' % prob_a_30under)
print('Number stranded: %s' % a_stranded)
print('Probability of stranding: %s\n' % float(a_stranded / passengers_per_airline))
print('Average arrival time on Airline 2: %s:%s' % (b_mean_hrs, b_mean_mins))
print('Probability of a 30 minute overrun or less: %s' % prob_b_30under)
print('Number stranded: %s' % b_stranded)
print('Probability of stranding: %s\n' % float(b_stranded / passengers_per_airline))

