\* AsignacionCursos *\
Maximize
TotalAsignaciones: AsigSugerida_(0,_2) + AsigSugerida_(0,_3)
 + AsigSugerida_(1,_0) + AsigSugerida_(1,_1) + AsigSugerida_(1,_3)
 + AsigSugerida_(1,_4) + AsigSugerida_(3,_2) + AsigSugerida_(4,_2)
Subject To
EstAsig_0: AsigSugerida_(0,_0) + AsigSugerida_(0,_1) + AsigSugerida_(0,_4)
 + AsigSugerida_(0,_5) + AsigSugerida_(0,_6) + AsigSugerida_(0,_7)
 + AsigSugerida_(0,_8) = 0
EstAsig_1: AsigSugerida_(1,_2) + AsigSugerida_(1,_5) + AsigSugerida_(1,_6)
 + AsigSugerida_(1,_7) + AsigSugerida_(1,_8) = 0
EstAsig_2: AsigSugerida_(2,_0) + AsigSugerida_(2,_1) + AsigSugerida_(2,_2)
 + AsigSugerida_(2,_3) + AsigSugerida_(2,_4) + AsigSugerida_(2,_5)
 + AsigSugerida_(2,_6) + AsigSugerida_(2,_7) + AsigSugerida_(2,_8) = 0
EstAsig_3: AsigSugerida_(3,_0) + AsigSugerida_(3,_1) + AsigSugerida_(3,_3)
 + AsigSugerida_(3,_4) + AsigSugerida_(3,_5) + AsigSugerida_(3,_6)
 + AsigSugerida_(3,_7) + AsigSugerida_(3,_8) = 0
EstAsig_4: AsigSugerida_(4,_0) + AsigSugerida_(4,_1) + AsigSugerida_(4,_3)
 + AsigSugerida_(4,_4) + AsigSugerida_(4,_5) + AsigSugerida_(4,_6)
 + AsigSugerida_(4,_7) + AsigSugerida_(4,_8) = 0
_C1: AsigSugerida_(0,_0) <= 1
_C10: AsigSugerida_(1,_0) <= 1
_C11: AsigSugerida_(1,_1) <= 1
_C12: AsigSugerida_(1,_2) <= 1
_C13: AsigSugerida_(1,_3) <= 1
_C14: AsigSugerida_(1,_4) <= 1
_C15: AsigSugerida_(1,_5) + AsigSugerida_(1,_8) <= 1
_C16: AsigSugerida_(1,_6) <= 1
_C17: AsigSugerida_(1,_7) <= 1
_C18: AsigSugerida_(1,_5) + AsigSugerida_(1,_8) <= 1
_C19: AsigSugerida_(2,_0) <= 1
_C2: AsigSugerida_(0,_1) <= 1
_C20: AsigSugerida_(2,_1) <= 1
_C21: AsigSugerida_(2,_2) <= 1
_C22: AsigSugerida_(2,_3) <= 1
_C23: AsigSugerida_(2,_4) <= 1
_C24: AsigSugerida_(2,_5) + AsigSugerida_(2,_8) <= 1
_C25: AsigSugerida_(2,_6) <= 1
_C26: AsigSugerida_(2,_7) <= 1
_C27: AsigSugerida_(2,_5) + AsigSugerida_(2,_8) <= 1
_C28: AsigSugerida_(3,_0) <= 1
_C29: AsigSugerida_(3,_1) <= 1
_C3: AsigSugerida_(0,_2) <= 1
_C30: AsigSugerida_(3,_2) <= 1
_C31: AsigSugerida_(3,_3) <= 1
_C32: AsigSugerida_(3,_4) <= 1
_C33: AsigSugerida_(3,_5) + AsigSugerida_(3,_8) <= 1
_C34: AsigSugerida_(3,_6) <= 1
_C35: AsigSugerida_(3,_7) <= 1
_C36: AsigSugerida_(3,_5) + AsigSugerida_(3,_8) <= 1
_C37: AsigSugerida_(4,_0) <= 1
_C38: AsigSugerida_(4,_1) <= 1
_C39: AsigSugerida_(4,_2) <= 1
_C4: AsigSugerida_(0,_3) <= 1
_C40: AsigSugerida_(4,_3) <= 1
_C41: AsigSugerida_(4,_4) <= 1
_C42: AsigSugerida_(4,_5) + AsigSugerida_(4,_8) <= 1
_C43: AsigSugerida_(4,_6) <= 1
_C44: AsigSugerida_(4,_7) <= 1
_C45: AsigSugerida_(4,_5) + AsigSugerida_(4,_8) <= 1
_C46: AsigSugerida_(0,_0) + AsigSugerida_(0,_4) <= 1
_C47: AsigSugerida_(0,_1) + AsigSugerida_(0,_5) + AsigSugerida_(0,_8) <= 1
_C48: __dummy <= 1
_C49: AsigSugerida_(0,_3) + AsigSugerida_(0,_7) <= 1
_C5: AsigSugerida_(0,_4) <= 1
_C50: __dummy <= 1
_C51: __dummy <= 1
_C52: AsigSugerida_(1,_0) + AsigSugerida_(1,_4) <= 1
_C53: AsigSugerida_(1,_1) + AsigSugerida_(1,_5) + AsigSugerida_(1,_8) <= 1
_C54: __dummy <= 1
_C55: AsigSugerida_(1,_3) + AsigSugerida_(1,_7) <= 1
_C56: __dummy <= 1
_C57: __dummy <= 1
_C58: AsigSugerida_(2,_0) + AsigSugerida_(2,_4) <= 1
_C59: AsigSugerida_(2,_1) + AsigSugerida_(2,_5) + AsigSugerida_(2,_8) <= 1
_C6: AsigSugerida_(0,_5) + AsigSugerida_(0,_8) <= 1
_C60: __dummy <= 1
_C61: AsigSugerida_(2,_3) + AsigSugerida_(2,_7) <= 1
_C62: __dummy <= 1
_C63: __dummy <= 1
_C64: AsigSugerida_(3,_0) + AsigSugerida_(3,_4) <= 1
_C65: AsigSugerida_(3,_1) + AsigSugerida_(3,_5) + AsigSugerida_(3,_8) <= 1
_C66: __dummy <= 1
_C67: AsigSugerida_(3,_3) + AsigSugerida_(3,_7) <= 1
_C68: __dummy <= 1
_C69: __dummy <= 1
_C7: AsigSugerida_(0,_6) <= 1
_C70: AsigSugerida_(4,_0) + AsigSugerida_(4,_4) <= 1
_C71: AsigSugerida_(4,_1) + AsigSugerida_(4,_5) + AsigSugerida_(4,_8) <= 1
_C72: __dummy <= 1
_C73: AsigSugerida_(4,_3) + AsigSugerida_(4,_7) <= 1
_C74: __dummy <= 1
_C75: __dummy <= 1
_C8: AsigSugerida_(0,_7) <= 1
_C9: AsigSugerida_(0,_5) + AsigSugerida_(0,_8) <= 1
maxCupos_0: AsigSugerida_(0,_0) + AsigSugerida_(1,_0) + AsigSugerida_(2,_0)
 + AsigSugerida_(3,_0) + AsigSugerida_(4,_0) <= 20
maxCupos_1: AsigSugerida_(0,_1) + AsigSugerida_(1,_1) + AsigSugerida_(2,_1)
 + AsigSugerida_(3,_1) + AsigSugerida_(4,_1) <= 20
maxCupos_2: AsigSugerida_(0,_2) + AsigSugerida_(1,_2) + AsigSugerida_(2,_2)
 + AsigSugerida_(3,_2) + AsigSugerida_(4,_2) <= 20
maxCupos_3: AsigSugerida_(0,_3) + AsigSugerida_(1,_3) + AsigSugerida_(2,_3)
 + AsigSugerida_(3,_3) + AsigSugerida_(4,_3) <= 20
maxCupos_4: AsigSugerida_(0,_4) + AsigSugerida_(1,_4) + AsigSugerida_(2,_4)
 + AsigSugerida_(3,_4) + AsigSugerida_(4,_4) <= 20
maxCupos_5: AsigSugerida_(0,_5) + AsigSugerida_(1,_5) + AsigSugerida_(2,_5)
 + AsigSugerida_(3,_5) + AsigSugerida_(4,_5) <= 0
maxCupos_6: AsigSugerida_(0,_6) + AsigSugerida_(1,_6) + AsigSugerida_(2,_6)
 + AsigSugerida_(3,_6) + AsigSugerida_(4,_6) <= 0
maxCupos_7: AsigSugerida_(0,_7) + AsigSugerida_(1,_7) + AsigSugerida_(2,_7)
 + AsigSugerida_(3,_7) + AsigSugerida_(4,_7) <= 20
maxCupos_8: AsigSugerida_(0,_8) + AsigSugerida_(1,_8) + AsigSugerida_(2,_8)
 + AsigSugerida_(3,_8) + AsigSugerida_(4,_8) <= 10
maxCur_0: AsigSugerida_(0,_0) + AsigSugerida_(0,_1) + AsigSugerida_(0,_2)
 + AsigSugerida_(0,_3) + AsigSugerida_(0,_4) + AsigSugerida_(0,_5)
 + AsigSugerida_(0,_6) + AsigSugerida_(0,_7) + AsigSugerida_(0,_8) <= 2
maxCur_1: AsigSugerida_(1,_0) + AsigSugerida_(1,_1) + AsigSugerida_(1,_2)
 + AsigSugerida_(1,_3) + AsigSugerida_(1,_4) + AsigSugerida_(1,_5)
 + AsigSugerida_(1,_6) + AsigSugerida_(1,_7) + AsigSugerida_(1,_8) <= 2
maxCur_2: AsigSugerida_(2,_0) + AsigSugerida_(2,_1) + AsigSugerida_(2,_2)
 + AsigSugerida_(2,_3) + AsigSugerida_(2,_4) + AsigSugerida_(2,_5)
 + AsigSugerida_(2,_6) + AsigSugerida_(2,_7) + AsigSugerida_(2,_8) <= 2
maxCur_3: AsigSugerida_(3,_0) + AsigSugerida_(3,_1) + AsigSugerida_(3,_2)
 + AsigSugerida_(3,_3) + AsigSugerida_(3,_4) + AsigSugerida_(3,_5)
 + AsigSugerida_(3,_6) + AsigSugerida_(3,_7) + AsigSugerida_(3,_8) <= 2
maxCur_4: AsigSugerida_(4,_0) + AsigSugerida_(4,_1) + AsigSugerida_(4,_2)
 + AsigSugerida_(4,_3) + AsigSugerida_(4,_4) + AsigSugerida_(4,_5)
 + AsigSugerida_(4,_6) + AsigSugerida_(4,_7) + AsigSugerida_(4,_8) <= 2
Binaries
AsigSugerida_(0,_0)
AsigSugerida_(0,_1)
AsigSugerida_(0,_2)
AsigSugerida_(0,_3)
AsigSugerida_(0,_4)
AsigSugerida_(0,_5)
AsigSugerida_(0,_6)
AsigSugerida_(0,_7)
AsigSugerida_(0,_8)
AsigSugerida_(1,_0)
AsigSugerida_(1,_1)
AsigSugerida_(1,_2)
AsigSugerida_(1,_3)
AsigSugerida_(1,_4)
AsigSugerida_(1,_5)
AsigSugerida_(1,_6)
AsigSugerida_(1,_7)
AsigSugerida_(1,_8)
AsigSugerida_(2,_0)
AsigSugerida_(2,_1)
AsigSugerida_(2,_2)
AsigSugerida_(2,_3)
AsigSugerida_(2,_4)
AsigSugerida_(2,_5)
AsigSugerida_(2,_6)
AsigSugerida_(2,_7)
AsigSugerida_(2,_8)
AsigSugerida_(3,_0)
AsigSugerida_(3,_1)
AsigSugerida_(3,_2)
AsigSugerida_(3,_3)
AsigSugerida_(3,_4)
AsigSugerida_(3,_5)
AsigSugerida_(3,_6)
AsigSugerida_(3,_7)
AsigSugerida_(3,_8)
AsigSugerida_(4,_0)
AsigSugerida_(4,_1)
AsigSugerida_(4,_2)
AsigSugerida_(4,_3)
AsigSugerida_(4,_4)
AsigSugerida_(4,_5)
AsigSugerida_(4,_6)
AsigSugerida_(4,_7)
AsigSugerida_(4,_8)
End
