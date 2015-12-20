from hulu import Hulu
h = HuluAPI()
try:
    h.get_companies()
except HuluError as e:
    print e

try:
    h.get_video_info(60153655)
except HuluError as e:
    print e
