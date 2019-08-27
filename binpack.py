#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 1/27/2019
"""


def mergesort_decreasing(item_array):
    def merge(array, start, midpoint, end):
        n1 = midpoint + 1
        left_array = array[start:n1]  # separate the subarrays to be merged.
        right_array = array[n1:end + 1]
        left_array.append(float("-inf"))
        right_array.append(float("-inf"))
        i = j = 0
        for k in range(start, end + 1):  # merge the partial arrays to a combined, ordered array.
            if left_array[i] > right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1

    def mergesort(array, start, end):
        if start < end:
            midpoint = (start + end) // 2  # floor division --Python3
            mergesort(array, start, midpoint)
            mergesort(array, midpoint + 1, end)
            merge(array, start, midpoint, end)

    mergesort(item_array, 0, len(item_array) - 1)
    return


def first_fit(item_array, capacity):
    bins = [0]
    for item in item_array:
        put = False
        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                put = True
                break
        if not put:
            bins.append(item)

    return len(bins)


def first_fit_decreasing(item_array, capacity):
    mergesort_decreasing(item_array)
    return first_fit(item_array, capacity)


def best_fit(item_array, capacity):
    bins = [capacity]
    for item in item_array:
        best_remaining = float("inf")
        best_bin = -1
        for b in range(len(bins)):
            if 0 <= bins[b] - item < best_remaining:
                best_remaining = bins[b] - item
                best_bin = b
        if best_bin >= 0:
            bins[best_bin] -= item
        else:
            bins.append(capacity - item)

    return len(bins)


# MAIN
if __name__ == "__main__":
    with open("bin.txt", "r") as ifile:  # read and parse integer lists from file.
        test_cases = int(ifile.readline())

        for i in range(test_cases):
            bin_capacity = int(ifile.readline())
            items_length = int(ifile.readline())  # not really needed here, used to throw away line.

            items = [int(item) for item in (ifile.readline()).split()]  # array of item weights.

            ff = first_fit(items.copy(), bin_capacity)
            ffd = first_fit_decreasing(items.copy(), bin_capacity)
            bf = best_fit(items.copy(), bin_capacity)

            print("Test Case: {}, Bin Capacity: {}, Total Items: {}\n"
                  "First Fit: {}, First Fit Decreasing: {}, Best Fit: {}\n".format(
                      i + 1, bin_capacity, items_length, ff, ffd, bf
                  ))


