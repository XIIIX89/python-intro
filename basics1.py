# following https://www.youtube.com/watch?v=fLAfa-BQtOQ
# and ZTM cheat sheet
# comment
"""
multi
line
comment
"""
print("Hello World!")
name = 'David'
birthDate = 19891209
print(name, birthDate) #adds a space between them

# Python does not ignore white space in code
"""
Normal int and float types
Operands:
+ add
- subtract
* multiply
/ divide
// --> floor division - returns integer
% modulous
** --> power
"""
floorDivide = 10 // 3
powerNumber = 5 ** 2
print(floorDivide, powerNumber)

"""
pow(#1, #2) --> power of #1^#2. Same as **
abs(#) --> absolute value
round(#.#) --> rounds
round(#.#, n) --> rounds to nth digit 
bin(#) --> binary of number
hex(#) --> hex number
"""
print(pow(5, 2))
print(abs(-50))
print(round(5.5))
print(round(5.123123, 3))
print(bin(1))
print(hex(8))

print(type(name))
print(type(birthDate))
print(type(5.123))

print("Name: " + name)
