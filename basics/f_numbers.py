from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Number Data Type Example')

h2('\n >>>> Integer Data Type Example')
age = 25
print(f'Int age ({age}) can be whole number, positive or negative, without decimals, of unlimited length.')
print('examples: 35656222554887711, -3255522, 25')

h3('\n >>>> Float Data Type Example')
weight = 76.50
print(f'Float weight ({weight}) can be number, positive or negative, containing one or more decimals')
print('examples: 1.10, 1.0, -35.59, 35e3, 12E4, -87.7e100')

h4('\n >>>> Complex Data Type Example')
something = 1j
print(f'complex something ({something}) are written with a "j" as the imaginary part')
print('examples: 1.10, 1.0, -35.59, 35e3, 12E4, -87.7e100')
 
h5('\n >>>> Type Case Functions');
print('examples: float(weight), int(age), complex()');