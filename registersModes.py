import re
str="R1"
str=str.upper()
str=str.replace("SP","R6")
str=str.replace("PC","R7")
autoIncrement=re.fullmatch("\(R[0-9]\)\+",str)
autoDecrement=re.fullmatch("\-\(R[0-9]\)",str)
direct=re.fullmatch("R[0-9]",str)
indexed=re.fullmatch("[^@-]\(R[0-9]\)",str)
autoIncrementIndirect=re.fullmatch("@\(R[0-9]\)\+",str)
autoDecrementIndirect=re.fullmatch("@\-\(R[0-9]\)",str)
directIndirect=re.fullmatch("@R[0-9]",str)
indexedIndirect=re.fullmatch("@[^-]+\(R[0-9]\)",str)
print(autoIncrement)
print(autoDecrement)
print(direct)
print(indexed)
print(autoIncrementIndirect)
print(autoDecrementIndirect)
print(directIndirect)
print(indexedIndirect)

Register={
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "R7":"111",
}
RegisterModes={
    "direct":"000",
    "autoIncrement":"001",
    "autoDecrement":"010",
    "indexed":"011",
    "directIndirect":"100",
    "autoIncrementIndirect":"101",
    "autoDecrementIndirect":"110",
    "indexedIndirect":"111",
}
twoOperands={
    "MOV":"0000",
    "ADD":"0001",
    "ADC":"0010",
    "SUB":"0011",
    "SBC":"0100",
    "AND":"0101",
    "OR":"0110",
    "XOR":"0111",
    "CMP":"1000",
}
oneOperands={
    "INC":"100100",
    "DEC":"100101",
    "CLR":"100110",
    "INV":"100111",
    "LSR":"101000",
    "ROR":"101001",
    "ASR":"101010",
    "LSL":"101011",
    "ROL":"101100",
}
branching={
    "BR":"110000",
    "BEQ":"110001",
    "BNE":"110010",
    "BLO":"110011",
    "BLS":"110100",
    "BHI":"110101",
    "BHS":"110110",
}
noOperands={
    "HLT":"111000",
    "NOP":"111001",
    "RESET":"111010",

}
jumpingInterrupts={
    "JSR":"111100",
    "RTS":"111101",
    "INT":"111110",
    "IRET":"111111",
}