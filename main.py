# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import scipy
import scipy.stats
import statistics
import math
lst = [6, 6, 10, 15, 9, 8, 17, 5]

def average(num):
    return lambda x: x//num
Avgresult = average(len(lst))
print("Average\t", Avgresult(sum(lst)))


def meanDeviation(lst):
    """
    Computes the mean deviation.
    Mean Deviation is average of distance of each value from that mean(average).
    """
    average = sum(lst) // len(lst)
    mean_deviation = 0
    for v in lst:
        mean_deviation += abs(average - v)
    return mean_deviation / len(lst)
print("MD\t", meanDeviation(lst))


def count(lst, value):
    """
    Counts the occurrence of a value in a list of values.
    """
    return lst.count(value)
print("Count\t", count(lst,value=6))


def variance(lst):
    """
    Computes the variance.
    Variance is useful to see how the list of values varied against the average.
    """
    average = Avgresult(sum(lst))
    variance = 0
    for v in lst:
        variance += ((average - v) ** 2)
    return variance / len(lst)
print("Variance\t", variance(lst))


def standardDeviation(lst):
    """
    Computes the standard deviation.
    Standard Deviation is useful to give an idea about range of normal values(i.e. location of most of values).
    """
    return variance(lst) ** 0.5

print("SD\t", standardDeviation(lst))


def median(lst):
    """
    Computes the median.
    Median is the middle value in a sorted list of values.
    """
    return statistics.median(lst)
print("Median\t", median(lst))


def maximum(lst):
    """
    Returns the max value.
    """
    return max(lst)

print("Max\t", maximum(lst))


def minimum(lst):
    """
    Returns the min value.
    """
    return min(lst)

print("Min\t", minimum(lst))


def range(lst):
    """
    Returns the difference between max and min values.
    """
    return maximum(lst) - minimum(lst)
print("Range\t", range(lst))


def summation(lst):
    """
    Returns summation of all values in a list.
    """
    return sum(lst)
print("Sum\t", summation(lst))

def length(lst):
    """
    Returns the length of list.
    """
    return len(lst)
print("Length\t", length(lst))

def sort(lst):
    """
    Sorts the list.
    """
    return sorted(lst)
print("sort\t", sort(lst))