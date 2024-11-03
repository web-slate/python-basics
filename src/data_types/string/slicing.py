from stylepy import h1,h2,h3,h4,h5,h6
h1('\n >>>> String Slicing Example')
print('s[start:end] extracts the substring from index start to lesser than end index / end - 1.')
print('s[start:end:step] extracts the substring from index start to lesser than end index / end - 1')

greet = "welcome"
debit_card = "1234-5678-9012-3456"
slicing_detailed_desc = '''Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5]'''
tutorial_site = 'https://webslate.io/blogs/algorithms/big-o-notations'
email_id = 'username@example.com'
phone_number = '+1-800-555-1234'
file_name = 'slicing.pdf'
transaction_timestamp = '2023-01-15 09:30:00'

h4('\n >>>> Get last four digit of debit card', '[-4:]')
print(debit_card[-4:])

h4('\n >>>> Get short description from long string', '[:140]')
print(slicing_detailed_desc[:140], '...')

h4('\n >>>> Get Mobile Country and Area Code', '[0:6]')
print(phone_number[0:6])

h4('\n >>>> Get US Mobile Number without Country Code', '[3:]')
print(phone_number[3:])

h4('\n >>>> Get File extension', '[-3]')
print(file_name[-3:])

h4('\n >>>> Get Transaction Date', '[0:10]')
print(transaction_timestamp[:10])
print('\n >>>> Get Transaction Date in DD-MM-YYYY', '[0:10]')
print(f'{transaction_timestamp[8:10]}-{transaction_timestamp[5:7]}-{transaction_timestamp[:4]}')

h4('\n >>>> Get Transaction Year', '[0:4]')
print(transaction_timestamp[:4])

h4('\n >>>> Get Transaction Month', '[5:7]')
print(transaction_timestamp[5:7])

h4('\n >>>> Get Transaction Time with seconds', '[-8:] / [11:]')
print(transaction_timestamp[-8:])
print(transaction_timestamp[11:])

h4('\n >>>> Get Transaction hour in Time without seconds', '[-8:-3]')
print(transaction_timestamp[-8:-3])

h4('\n >>>> Get Time String Revered', '[::-1]')
print(transaction_timestamp[::-1])
