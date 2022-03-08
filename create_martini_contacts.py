#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 askusay

# create Martini go or elastic contacts from file, see https://github.com/askusay/Visualise_martini_bond_network for exmaple

from itertools import chain

from pymol import cmd

def create_martini_contacts(obj, file):
    bonds_list = []

    with open(file,'r') as f:
        for i in f:
            bonds_list.append(i.split()[:2])

    for i, j in bonds_list:
        cmd.bond(f'{obj} and ID {int(i)}', f'{obj} and ID {int(j)}')

    bonds_sele = list(set(chain(*bonds_list)))
    joined_sele = f"{obj} and ID " + "+".join(bonds_sele)

    print(f"selecting {joined_sele}")
    cmd.select(f"{obj}_contact_bonds", f"{joined_sele}")

    cmd.show("sticks",joined_sele)

    return 

cmd.extend('create_martini_contacts', create_martini_contacts)

cmd.auto_arg[0]['create_martini_contacts']=[cmd.object_sc, 'objects', ',']
