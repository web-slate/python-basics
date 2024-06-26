from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Boolean Data Type Example')
h2('\n >>> When boolean returns `False`')

h5('For False ', bool(False));
h6('For Zero ', bool(0));
h5('For Empty String ', bool(''));
h6('For Empty List ', bool([]));
h6('For Empty Tuple ', bool(()));
h5('For Empty Dictionary ', bool({}));
h6('For None ', bool(None));

h3('\n >>> When boolean returns `True`')
h5('For greater than Zero ', bool(1));
h6('For atleast one String ', bool('a'));
h5('For atleast one item in List ', bool(['a']));
h6('For atleast one item in Tuple ', bool(('a')));
h5('For atleast one item in Dictionary ', bool({'a': 'A'}));