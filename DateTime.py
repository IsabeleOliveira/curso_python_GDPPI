from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5)

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao = dt.strftime('%A, %d, de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')



if __name__ == "__main__":
    print(data.strftime('%d/%m/%Y %H:%M:%S'))
    print(dif)
    print(formatacao)
    print(formatacao2)
    print(mes_atual, mdays[mes_atual])