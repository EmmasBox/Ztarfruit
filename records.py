import ztarfruit as zfruit

#0100
group_basic_data_record_fields = [
    zfruit.Field(name="GPBD_NAME",data_type=zfruit.DataType.Char,start=6,end=13),
    zfruit.Field(name="GPBD_SUPGRP_ID",data_type=zfruit.DataType.Char,start=15,end=22),
    zfruit.Field(name="GPBD_CREATE_DATE",data_type=zfruit.DataType.Char,start=24,end=33),
    zfruit.Field(name="GPBD_OWNER_ID",data_type=zfruit.DataType.Char,start=35,end=42),
    zfruit.Field(name="GPBD_UACC",data_type=zfruit.DataType.Char,start=44,end=51),
    zfruit.Field(name="GPBD_NOTERMUACC",data_type=zfruit.DataType.Char,start=53,end=56),
    zfruit.Field(name="GPBD_INSTALL_DATA",data_type=zfruit.DataType.Char,start=58,end=312),
    zfruit.Field(name="GPBD_MODEL",data_type=zfruit.DataType.Char,start=314,end=357),
    zfruit.Field(name="GPBD_UNIVERSAL",data_type=zfruit.DataType.Char,start=359,end=362)
]

#0101
group_subgroups_data_record_fields = [
    zfruit.Field(name="GPSGRP_NAME",data_type=zfruit.DataType.Char,start=6,end=13),
    zfruit.Field(name="GPSGRP_SUBGRP_ID",data_type=zfruit.DataType.Char,start=15,end=22),
]

records = [
    zfruit.Record(name="Group basic data record",identifier="0100",fields=group_basic_data_record_fields),
    zfruit.Record(name="Group subgroups record",identifier="0101",fields=group_subgroups_data_record_fields)
]