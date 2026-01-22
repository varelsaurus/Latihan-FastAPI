# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel #Library untuk validasi data, user friendly jg
# 2. Mendekelarasikan tipe data dari setiap variabel
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float