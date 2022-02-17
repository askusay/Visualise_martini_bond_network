#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 askusay

# create Martini go or elastic contacts from file, see https://github.com/askusay/Visualise_martini_bond_network for exmaple

from pymol import cmd
import pandas as pd

def create_martini_contacts(obj, file):
    bonds_list = []
    df = pd.read_csv(file, delim_whitespace=True, names=['a1','a2','form','e1','e2']).astype(str)

    for _,r in df.iterrows():
        bonds_list.append(r[0])
        bonds_list.append(r[1])

        cmd.bond(f'{obj} and ID {int(r[0])}', f'{obj} and ID {int(r[1])}')

    bonds_sele = list(set(bonds_list))
    joined_sele = f"{obj} and ID " + "+".join(bonds_sele)

    print(f"selecting {joined_sele}")
    cmd.select(f"{obj}_contact_bonds", f"{joined_sele}")

    cmd.show("sticks",joined_sele)

    return 

cmd.extend('create_martini_contacts', create_martini_contacts)

cmd.auto_arg[0]['create_martini_contacts']=[cmd.object_sc, 'objects', ',']
