#!/usr/bin/python
__author__ = '@vignolo'
import sys
import random

items = [[10,'Carne'], 
        [10,'Bebida [Vino, Gaseosa (Aquarius Pomelo), Soda]'], 
        [7,'Carbon'], 
        [5,'Verdura [Tomate, Pimiento, Limon, Huevo]'], 
        [3, 'Pan (Celeste)'], 
        [3,'Postre']]

def process_args(options):
    options = options[1:]
    current_items = items[:]

    if '-help' in options:
        print "usage: assing.py [-p] [people..]"
        print "-p: Add 'Picada' as a extra item"
        print "example: assign.py @Joey @Ross @Chandler"
        sys.exit()


    if '-p' in options:
        current_items.append([2,'Picada'])
        options = options[options.index("-p")+1:]

    if len(options) == 0:
        print "something is wrong. use -help"
        sys.exit()

    return options[:], current_items


def print_list(cenadores):
    print " "
    print '~~ Cenadores ~~'

    for key,value in cenadores:
        print key, ": ", ", ".join([item[1] for item in value])

    print " "

def fair_sort_key(element):
    # put the people with least item assignment weight first.
    assignment_weight = 0
    for weight, _ in element[1]:
        assignment_weight += weight
    return assignment_weight

def fair_put(assignment_list, item):
    sorted_list = sorted(assignment_list, key=fair_sort_key)
    # assign item to the person with least/lightest things.
    assigned = assignment_list.index(sorted_list[0])
    assignment_list[assigned][1].append(item)


def main():
    people, current_items = process_args(sys.argv)
    people = zip(people, [list() for x in xrange(len(people))])
    random.shuffle(people)
    for item in current_items:
        fair_put(people, item)

    print_list(people)

if __name__ == "__main__":
    main()
