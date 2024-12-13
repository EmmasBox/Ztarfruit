#This module defines all of the records and fields that can exist in IRRDBU00 output

import record_definition as definition

#0100
group_basic_data_record_fields = [
    definition.Field(name="GPBD_NAME",data_type=DataType.Char,start=6,end=13),
    definition.Field(name="GPBD_SUPGRP_ID",data_type=DataType.Char,start=15,end=22),
    definition.Field(name="GPBD_CREATE_DATE",data_type=DataType.Char,start=24,end=33),
    definition.Field(name="GPBD_OWNER_ID",data_type=DataType.Char,start=35,end=42),
    definition.Field(name="GPBD_UACC",data_type=DataType.Char,start=44,end=51),
    definition.Field(name="GPBD_NOTERMUACC",data_type=DataType.Char,start=53,end=56),
    definition.Field(name="GPBD_INSTALL_DATA",data_type=DataType.Char,start=58,end=312),
    definition.Field(name="GPBD_MODEL",data_type=DataType.Char,start=314,end=357),
    definition.Field(name="GPBD_UNIVERSAL",data_type=DataType.Char,start=359,end=362)
]

#0101
group_subgroups_data_record_fields = [
    definition.Field(name="GPSGRP_NAME",data_type=DataType.Char,start=6,end=13),
    definition.Field(name="GPSGRP_SUBGRP_ID",data_type=DataType.Char,start=15,end=22),
]

#Records
database_records = [
    definition.Record(name="Group basic data record",identifier="0100",fields=group_basic_data_record_fields),
    definition.Record(name="Group subgroups record",identifier="0101",fields=group_subgroups_data_record_fields)
]