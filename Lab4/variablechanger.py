print("1:" + str(a and b and c))
print("2:" + str(a or b or c))
print("3:" + str((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)))
# !((a & !b) || (!c & b)) & (! b) || (!a & b & !c) || (a & !b))
print("4" + str((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))))
# (!((b || !c) & (!a || !c))) || (!(c || !(b & c))) || (a && !c) & (!a || (a & b & c) or (a & ((b & ! c) or (! b)))))
print("5:" + str((a or b) and not (a == b)))
print("6:" + (not (b and c) or (c and a) or (a and b)))
# (!(a &! b) || (!c & b ) & !b || (!a & b & !c) || (a & !b)
# !a & b or                !b || !(a & c) & b
# !(a||c) & b
# (!(a||c) & b ) & !b || (!a & b & !c) || (a & !b)
#                         !(a&c) & b || (a&!b)
print("7:" + str(False))
# (!((b || !c) & (!a || !c))) || (!(c || !(b & c))) || (a && !c) & (!a || (a & b & c) or (a & ((b & ! c) or (! b)))))
#  (!b&a||c) || (!c || b and c) || !a || 
