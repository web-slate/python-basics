print('\n >>>> Boolean Data Type Example')
print('\n >>> When boolean returns `False`')

print('For False ', bool(False));
print('For Zero ', bool(0));
print('For Empty String ', bool(''));
print('For Empty List ', bool([]));
print('For Empty Tuple ', bool(()));
print('For Empty Dictionary ', bool({}));
print('For None ', bool(None));

print('\n >>> When boolean returns `True`')
print('For greater than Zero ', bool(1));
print('For atleast one String ', bool('a'));
print('For atleast one item in List ', bool(['a']));
print('For atleast one item in Tuple ', bool(('a')));
print('For atleast one item in Dictionary ', bool({'a': 'A'}));