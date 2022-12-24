input = '1110000'  # 7

seg0 = '1111111'
seg1 = '1100000'
seg2 = '1101101'
seg = [seg0, seg1, seg2]

for i in seg:
    if int(i,2) & int(input,2) == int(input,2):
        print(i)
