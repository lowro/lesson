FILE_NAME = 'rabotniki.txt'
with open(FILE_NAME, 'r',) as f:
    lines = f.readlines()
    rabotniki_s_malou_zp = []
    zp_malay = 0
    for line in lines:
        familiy, zp = line.split()
        zp = float(zp)
        zp_malay += zp
        if zp < 30000:
            rabotniki_s_malou_zp.append(familiy)
    print(f'сотрудники с окладом меньше 30000: {rabotniki_s_malou_zp}')
    print(f'окалд: {round(zp_malay/ len(line),2)}')

