d = float(input('Digite uma distancia em metros: '))
km = d / 1000
mm = d * 1000
print('A medida de {}m corresponde a {}km \nE são {}mm'.format(d, km, mm))
print('A medida de {}m corresponde a {}cm \n{}dam'.format(d, (d * 100), (d / 10)))
