\* AsignacionCursos *\
Maximize
TotalAsignaciones: 20 AsigSugerida_(0,_0) + 20 AsigSugerida_(0,_1)
 + 36 AsigSugerida_(1,_0) + 36 AsigSugerida_(1,_1) + 8 AsigSugerida_(2,_0)
 + 8 AsigSugerida_(2,_1) + 40 AsigSugerida_(3,_0) + 40 AsigSugerida_(3,_1)
 + 8 AsigSugerida_(4,_0) + 8 AsigSugerida_(4,_1) + 44 AsigSugerida_(5,_0)
 + 44 AsigSugerida_(5,_1) + 8 AsigSugerida_(6,_0) + 8 AsigSugerida_(6,_1)
 + 20 AsigSugerida_(7,_0) + 20 AsigSugerida_(7,_1) + 8 AsigSugerida_(8,_0)
 + 8 AsigSugerida_(8,_1) + 20 AsigSugerida_(9,_0) + 20 AsigSugerida_(9,_1)
Subject To
EstAsig_0: AsigSugerida_(0,_2) + AsigSugerida_(0,_3) = 0
EstAsig_1: AsigSugerida_(1,_2) + AsigSugerida_(1,_3) = 0
EstAsig_2: AsigSugerida_(2,_2) + AsigSugerida_(2,_3) = 0
EstAsig_3: AsigSugerida_(3,_2) + AsigSugerida_(3,_3) = 0
EstAsig_4: AsigSugerida_(4,_2) + AsigSugerida_(4,_3) = 0
EstAsig_5: AsigSugerida_(5,_2) + AsigSugerida_(5,_3) = 0
EstAsig_6: AsigSugerida_(6,_2) + AsigSugerida_(6,_3) = 0
EstAsig_7: AsigSugerida_(7,_2) + AsigSugerida_(7,_3) = 0
EstAsig_8: AsigSugerida_(8,_2) + AsigSugerida_(8,_3) = 0
EstAsig_9: AsigSugerida_(9,_2) + AsigSugerida_(9,_3) = 0
_C1: AsigSugerida_(0,_0) <= 1
_C10: AsigSugerida_(2,_1) <= 1
_C100: __dummy <= 1
_C11: AsigSugerida_(2,_2) <= 1
_C12: AsigSugerida_(2,_3) <= 1
_C13: AsigSugerida_(3,_0) <= 1
_C14: AsigSugerida_(3,_1) <= 1
_C15: AsigSugerida_(3,_2) <= 1
_C16: AsigSugerida_(3,_3) <= 1
_C17: AsigSugerida_(4,_0) <= 1
_C18: AsigSugerida_(4,_1) <= 1
_C19: AsigSugerida_(4,_2) <= 1
_C2: AsigSugerida_(0,_1) <= 1
_C20: AsigSugerida_(4,_3) <= 1
_C21: AsigSugerida_(5,_0) <= 1
_C22: AsigSugerida_(5,_1) <= 1
_C23: AsigSugerida_(5,_2) <= 1
_C24: AsigSugerida_(5,_3) <= 1
_C25: AsigSugerida_(6,_0) <= 1
_C26: AsigSugerida_(6,_1) <= 1
_C27: AsigSugerida_(6,_2) <= 1
_C28: AsigSugerida_(6,_3) <= 1
_C29: AsigSugerida_(7,_0) <= 1
_C3: AsigSugerida_(0,_2) <= 1
_C30: AsigSugerida_(7,_1) <= 1
_C31: AsigSugerida_(7,_2) <= 1
_C32: AsigSugerida_(7,_3) <= 1
_C33: AsigSugerida_(8,_0) <= 1
_C34: AsigSugerida_(8,_1) <= 1
_C35: AsigSugerida_(8,_2) <= 1
_C36: AsigSugerida_(8,_3) <= 1
_C37: AsigSugerida_(9,_0) <= 1
_C38: AsigSugerida_(9,_1) <= 1
_C39: AsigSugerida_(9,_2) <= 1
_C4: AsigSugerida_(0,_3) <= 1
_C40: AsigSugerida_(9,_3) <= 1
_C41: AsigSugerida_(0,_0) <= 1
_C42: __dummy <= 1
_C43: AsigSugerida_(0,_1) <= 1
_C44: AsigSugerida_(0,_2) <= 1
_C45: AsigSugerida_(0,_3) <= 1
_C46: __dummy <= 1
_C47: AsigSugerida_(1,_0) <= 1
_C48: __dummy <= 1
_C49: AsigSugerida_(1,_1) <= 1
_C5: AsigSugerida_(1,_0) <= 1
_C50: AsigSugerida_(1,_2) <= 1
_C51: AsigSugerida_(1,_3) <= 1
_C52: __dummy <= 1
_C53: AsigSugerida_(2,_0) <= 1
_C54: __dummy <= 1
_C55: AsigSugerida_(2,_1) <= 1
_C56: AsigSugerida_(2,_2) <= 1
_C57: AsigSugerida_(2,_3) <= 1
_C58: __dummy <= 1
_C59: AsigSugerida_(3,_0) <= 1
_C6: AsigSugerida_(1,_1) <= 1
_C60: __dummy <= 1
_C61: AsigSugerida_(3,_1) <= 1
_C62: AsigSugerida_(3,_2) <= 1
_C63: AsigSugerida_(3,_3) <= 1
_C64: __dummy <= 1
_C65: AsigSugerida_(4,_0) <= 1
_C66: __dummy <= 1
_C67: AsigSugerida_(4,_1) <= 1
_C68: AsigSugerida_(4,_2) <= 1
_C69: AsigSugerida_(4,_3) <= 1
_C7: AsigSugerida_(1,_2) <= 1
_C70: __dummy <= 1
_C71: AsigSugerida_(5,_0) <= 1
_C72: __dummy <= 1
_C73: AsigSugerida_(5,_1) <= 1
_C74: AsigSugerida_(5,_2) <= 1
_C75: AsigSugerida_(5,_3) <= 1
_C76: __dummy <= 1
_C77: AsigSugerida_(6,_0) <= 1
_C78: __dummy <= 1
_C79: AsigSugerida_(6,_1) <= 1
_C8: AsigSugerida_(1,_3) <= 1
_C80: AsigSugerida_(6,_2) <= 1
_C81: AsigSugerida_(6,_3) <= 1
_C82: __dummy <= 1
_C83: AsigSugerida_(7,_0) <= 1
_C84: __dummy <= 1
_C85: AsigSugerida_(7,_1) <= 1
_C86: AsigSugerida_(7,_2) <= 1
_C87: AsigSugerida_(7,_3) <= 1
_C88: __dummy <= 1
_C89: AsigSugerida_(8,_0) <= 1
_C9: AsigSugerida_(2,_0) <= 1
_C90: __dummy <= 1
_C91: AsigSugerida_(8,_1) <= 1
_C92: AsigSugerida_(8,_2) <= 1
_C93: AsigSugerida_(8,_3) <= 1
_C94: __dummy <= 1
_C95: AsigSugerida_(9,_0) <= 1
_C96: __dummy <= 1
_C97: AsigSugerida_(9,_1) <= 1
_C98: AsigSugerida_(9,_2) <= 1
_C99: AsigSugerida_(9,_3) <= 1
maxCupos_0: AsigSugerida_(0,_0) + AsigSugerida_(1,_0) + AsigSugerida_(2,_0)
 + AsigSugerida_(3,_0) + AsigSugerida_(4,_0) + AsigSugerida_(5,_0)
 + AsigSugerida_(6,_0) + AsigSugerida_(7,_0) + AsigSugerida_(8,_0)
 + AsigSugerida_(9,_0) <= 1
maxCupos_1: AsigSugerida_(0,_1) + AsigSugerida_(1,_1) + AsigSugerida_(2,_1)
 + AsigSugerida_(3,_1) + AsigSugerida_(4,_1) + AsigSugerida_(5,_1)
 + AsigSugerida_(6,_1) + AsigSugerida_(7,_1) + AsigSugerida_(8,_1)
 + AsigSugerida_(9,_1) <= 1
maxCupos_2: AsigSugerida_(0,_2) + AsigSugerida_(1,_2) + AsigSugerida_(2,_2)
 + AsigSugerida_(3,_2) + AsigSugerida_(4,_2) + AsigSugerida_(5,_2)
 + AsigSugerida_(6,_2) + AsigSugerida_(7,_2) + AsigSugerida_(8,_2)
 + AsigSugerida_(9,_2) <= 1
maxCupos_3: AsigSugerida_(0,_3) + AsigSugerida_(1,_3) + AsigSugerida_(2,_3)
 + AsigSugerida_(3,_3) + AsigSugerida_(4,_3) + AsigSugerida_(5,_3)
 + AsigSugerida_(6,_3) + AsigSugerida_(7,_3) + AsigSugerida_(8,_3)
 + AsigSugerida_(9,_3) <= 1
maxCur_0: AsigSugerida_(0,_0) + AsigSugerida_(0,_1) + AsigSugerida_(0,_2)
 + AsigSugerida_(0,_3) <= 2
maxCur_1: AsigSugerida_(1,_0) + AsigSugerida_(1,_1) + AsigSugerida_(1,_2)
 + AsigSugerida_(1,_3) <= 2
maxCur_2: AsigSugerida_(2,_0) + AsigSugerida_(2,_1) + AsigSugerida_(2,_2)
 + AsigSugerida_(2,_3) <= 2
maxCur_3: AsigSugerida_(3,_0) + AsigSugerida_(3,_1) + AsigSugerida_(3,_2)
 + AsigSugerida_(3,_3) <= 2
maxCur_4: AsigSugerida_(4,_0) + AsigSugerida_(4,_1) + AsigSugerida_(4,_2)
 + AsigSugerida_(4,_3) <= 2
maxCur_5: AsigSugerida_(5,_0) + AsigSugerida_(5,_1) + AsigSugerida_(5,_2)
 + AsigSugerida_(5,_3) <= 2
maxCur_6: AsigSugerida_(6,_0) + AsigSugerida_(6,_1) + AsigSugerida_(6,_2)
 + AsigSugerida_(6,_3) <= 2
maxCur_7: AsigSugerida_(7,_0) + AsigSugerida_(7,_1) + AsigSugerida_(7,_2)
 + AsigSugerida_(7,_3) <= 2
maxCur_8: AsigSugerida_(8,_0) + AsigSugerida_(8,_1) + AsigSugerida_(8,_2)
 + AsigSugerida_(8,_3) <= 2
maxCur_9: AsigSugerida_(9,_0) + AsigSugerida_(9,_1) + AsigSugerida_(9,_2)
 + AsigSugerida_(9,_3) <= 2
Binaries
AsigSugerida_(0,_0)
AsigSugerida_(0,_1)
AsigSugerida_(0,_2)
AsigSugerida_(0,_3)
AsigSugerida_(1,_0)
AsigSugerida_(1,_1)
AsigSugerida_(1,_2)
AsigSugerida_(1,_3)
AsigSugerida_(2,_0)
AsigSugerida_(2,_1)
AsigSugerida_(2,_2)
AsigSugerida_(2,_3)
AsigSugerida_(3,_0)
AsigSugerida_(3,_1)
AsigSugerida_(3,_2)
AsigSugerida_(3,_3)
AsigSugerida_(4,_0)
AsigSugerida_(4,_1)
AsigSugerida_(4,_2)
AsigSugerida_(4,_3)
AsigSugerida_(5,_0)
AsigSugerida_(5,_1)
AsigSugerida_(5,_2)
AsigSugerida_(5,_3)
AsigSugerida_(6,_0)
AsigSugerida_(6,_1)
AsigSugerida_(6,_2)
AsigSugerida_(6,_3)
AsigSugerida_(7,_0)
AsigSugerida_(7,_1)
AsigSugerida_(7,_2)
AsigSugerida_(7,_3)
AsigSugerida_(8,_0)
AsigSugerida_(8,_1)
AsigSugerida_(8,_2)
AsigSugerida_(8,_3)
AsigSugerida_(9,_0)
AsigSugerida_(9,_1)
AsigSugerida_(9,_2)
AsigSugerida_(9,_3)
End
