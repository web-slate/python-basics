from stylepy import h1, h2, h3, h4, h5, h6
h1('To determine whether your Mac is 32-bit or 64-bit, you can use a command in the Terminal. ') 

h2('Below for mac / linux system.') 

h3("uname -m ")


# Output `x86_64``

# Windows


h4("wmic os get osarchitecture")


# Output below


#OSArchitecture

#64-bit


# is integer variable depends on my bit system ?

# In Python, the size of an integer is not constrained by the number of bits in a byte but by the available memory. Thus, integers can be of any size until the memory is exhausted.

# An int in Java is always 32 bits, regardless of whether the system is 32-bit or 64-bit.

# In NodeJS, all numbers are represented as double-precision 64-bit binary format IEEE 754 numbers

# In Go, int and uint types are platform dependent. On a 32-bit system, these types are 32 bits, while on a 64-bit system, they are 64 bits.

# In Rust, integer types have fixed sizes regardless of the platform. Types such as i32, i64, u32, u64,
