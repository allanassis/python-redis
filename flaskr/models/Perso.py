from stdnet import odm


class Perso(odm.StdModel):
    name = odm.SymbolField(unique=True)
    last_name = odm.AtomField()
    age = odm.IntegerField()
