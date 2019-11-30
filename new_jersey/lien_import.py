import pandas as pd
import os
from datetime import datetime, date
import math


def lien_modifier(lien):
    keys_to_delete = []
    for index, tup in enumerate(lien.items()):
        key, value = tup
        if type(value) != str:
            if type(value) != date:
                if math.isnan(value):
                    keys_to_delete.append(key)
    for key in keys_to_delete:
        lien.pop(key)


def lien_import(model):
    liens = pd.read_excel('C:\\Users\\rhughes\\Documents\\django\\tang_dashboard\\new_jersey\\liens_for_dashboard.xlsx')
    lien_models = []
    for index, lien in liens.iterrows():
        fixture = {}
        for column_name, column_value in zip(lien.index, lien):
            if column_name == "sale_date" or column_name == "recording_date":
                if type(column_value) == float:
                    pass
                else:
                    date_obj = datetime.strptime(column_value, '%Y-%m-%d').date()
                    fixture[column_name] = date_obj
            else:
                fixture[column_name] = column_value
        lien_modifier(fixture)
        lien_instance = model(**fixture)
        lien_models.append(lien_instance)
    return lien_models


def sub_modifier(subs):
    #subs = pd.read_excel('C:\\Users\\rhughes\\Documents\\django\\tang_dashboard\\new_jersey\\subs_for_dashboard.xlsx', sheet_name="agg")
    subs_modified = {}
    for index, sub in subs.iterrows():
        sub_date = datetime.strptime(sub['sub_date'], '%Y-%m-%d').date()
        if str(sub['lien_id']) not in subs_modified:
            subs_modified[str(sub['lien_id'])] = []
        subs_modified[str(sub['lien_id'])].append({
            'sub_type': sub['sub_type'],
            'sub_date': sub_date,
            'total': sub['total'],
        })
    return subs_modified


def sub_import(lien_model, sub_model):
    subs = pd.read_excel('C:\\Users\\rhughes\\Documents\\django\\tang_dashboard\\new_jersey\\subs_for_dashboard.xlsx', sheet_name="agg")
    subs = sub_modifier(subs)
    sub_list = []
    for lien_id, subs in subs.items():
        id = int(lien_id)
        lien = lien_model.objects.get(lien_id=id)
        for sub in subs:
            s = sub_model(**sub)
            s.lien = lien
            sub_list.append(s)
    return sub_list
