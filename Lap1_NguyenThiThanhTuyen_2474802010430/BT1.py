#1
danhsach1 = [1. , 3.] 
danhsach2 = [5. , 7.] 
danhsach = danhsach1 + danhsach2
danhsach_gapdoi = 2 * danhsach 
print(danhsach)
print(danhsach_gapdoi)



mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1] 
diem_so = [10, 9, 8, 7] 
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print(list(anh_xa))
tap_hop = set(anh_xa) 
print(list(tap_hop))
lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print(list(zip(range(4), range(7, 12), reversed(range(11) ) ) ))