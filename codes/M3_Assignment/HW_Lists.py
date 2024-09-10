#!/usr/bin/env python
# coding: utf-8

#Start your assignment here
print("Assignment 3")

# Problem 1: Lists, Sets and Coersion
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
one_b = one_a.copy()
one_b[5] = one_b[5]+3
one_c = [float(i) for i in one_b]
one_d = set(one_c)
one_e = one_d.copy()
one_e.add(10)
one_f = one_e.copy()
one_f.pop()
one_g = len(one_f)
one_h = len(set(one_f)) == len(list(one_f))
one_i = list(one_f) + list(one_a)
one_j = set(one_i)
one_k = len(one_j)
# Problem 2: Dictionary woes
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}
two_a = {
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi
}
two_b = two_patient_dictionary_dango['name']
# two_c
two_a['two_patient_dictionary_mochi']['year'] = 2018
two_d = {'Kinoko':2021,'Dango':2019,'Mochi':2019}
two_e = list(two_d.keys())
two_f = list(two_d.values())
two_g = dict(zip(two_e, two_f))
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
three_a = three_setE.issubset(three_setA)
three_b = three_setE < three_setA
three_c = three_setA.intersection(three_setB)
three_d = three_setC.union(three_setD, three_setE)
three_e = three_d.copy()
three_e.add(9)
three_f = three_d == one_a
# three g
# a list and a set cannot be equal
# need to take 0 out of one_a and make it a set to make it equal to three_d
type_list = []
# a
four_a = int(8)
type_list.append(type(four_a))
# b
four_b = []
type_list.append(type(four_b))
# c
type_list.append(type(four_a))
# d
four_d = four_a + 0.39
type_list.append(type(four_d))
# e
type_list.append(type(0.39))
# f
four_f = round(four_d ** -10)
type_list.append(type(four_f))
# g
type_list.append(type(four_f))
# Problem 5: More variable type changes
# a
five_a = {index: value for index, value in enumerate(type_list)}
print(five_a)
# b
five_b = str(four_f + 300)
# c
type_list.append(type(five_b))
# d
five_d = five_b[:2]
# e
type_list.append(type(five_d))
# f
five_f = [int(i) for i in five_d]
# g
type_list.append(type(five_f))
# h
type_list.append(type(three_setA))




