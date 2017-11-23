from datetime import datetime


def verificar_idade(datanasc:datetime):
    if datanasc.month == datetime.today().month:
        return datetime.today().year - datanasc.year
    else:
        return (datetime.today().year - datanasc.year) - 1