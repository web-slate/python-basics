from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Number Data Type Example')

h2('\n >>>> Integer Data Type Example')
age = 25
h3(f'Int age ({age}) can be whole number, positive or negative, without decimals, of unlimited length.')
h4('examples: 35656222554887711, -3255522, 25')

h3('\n >>>> Float Data Type Example')
weight = 76.50
h4(f'Float weight ({weight}) can be number, positive or negative, containing one or more decimals')
h5('examples: 1.10, 1.0, -35.59, 35e3, 12E4, -87.7e100')

h4('\n >>>> Complex Data Type Example')
something = 1j
h5(f'complex something ({something}) are written with a "j" as the imaginary part')
h6('examples: 1.10, 1.0, -35.59, 35e3, 12E4, -87.7e100')
 
h5('\n >>>> Type Case Functions');
h6('examples: float(weight), int(age), complex()');