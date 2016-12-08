from main import *

import numpy as np

a = np.zeros((3,7))
a = rect(a,3,2)
print to_string(a)
a = rotate(a,'x',1,1)
print to_string(a)
a = rotate(a,'y',0,4)
print to_string(a)
a = rotate(a,'x',1,1)
print to_string(a)
print to_string(a)
