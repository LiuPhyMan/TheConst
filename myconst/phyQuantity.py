# -*- coding: utf-8 -*-
"""
@author: Liu.Jinbao
@contact: liu.jinbao@outlook.com
@time: 23.May.2023
"""


def Length(value, unit):
    match unit:
        case "m":
            return value
        case "cm":
            return value*1e-2
        case "mm":
            return value*1e-3
        case "nm":
            return value*1e-9
        case _:
            raise Exception("unit of {unit} is error.")
