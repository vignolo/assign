#!/usr/bin/python
__author__ = '@vignolo'
import sys
import random

items = [[10,'Carne'], [10,'Bebida [Vino, Gaseosa (Aquarius Pomelo), Soda]'], [7,'Carbon'], [5,'Verdura [Tomate, Pimiento, Limon]'], [3, 'Pan (Celeste)'], [3,'Postre']]

def process_args(options):

    if '-help' in options:
        print "usage: assing.py [-p] [people..]"
        print "-p: Add 'Picada' as a extra item"
        print "example: assign.py @Joey @Ross @Chandler"
        sys.exit()

    if '-p' in options:
        items.append([2,'Picada'])
        options.remove('-p')

    if len(options) == 0:
        print "something is wrong. use -help"
        sys.exit()

    return options

def randomize_list(people):
    random.shuffle(people)
    return people


def construct_final_list(people):
    assigned_list = {}
    while people:
        p = random.choice(people)
        assigned_list[p] = []
        people.remove(p)
    return assigned_list

def print_list(list):
    print " "
    print '~~ Cenadores ~~'

    for key,value in list.iteritems():
        print key, ": ", ", ".join([item[1] for item in value])

    print " "

def main():

    people = process_args(sys.argv[1:len(sys.argv) + 1])

    final_list = construct_final_list(randomize_list(people))
    print "final list: ", final_list

    for item in items:
        p = sorted(final_list.items(), key=lambda e: sum(i for i, j in e[1]))[0][0]
        final_list[p].append(item)

    print_list(final_list)

if __name__ == "__main__":
    main()
