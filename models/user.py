#!/usr/bin/python3
"""
Module: user.py
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
