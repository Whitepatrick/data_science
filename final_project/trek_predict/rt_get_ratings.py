from rottentomatoes import RT
from secret import RT_KEY as rt_key

RT(rt_key).search('some movie here')
