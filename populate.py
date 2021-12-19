import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRFFilteringProject.settings')
import django
django.setup()
from DRFFilteringApp.models import WFMTModel
import faker
import random
import string
def populate(n):
    for _ in range(n):
        fcp_number_first="CP00"
        fcp_number_last=''.join([random.choice(string.ascii_uppercase)for _ in range(2)])
        fcp_number_middle=str(random.randint(11,99))
        fcp_number=fcp_number_first+fcp_number_middle+fcp_number_last
        fsne_id=random.randint(111111,999999)
        fscheme_number=random.randint(111111,444444)
        ftrs="".join([random.choice(string.ascii_uppercase) for _ in range (2)])
        WFMTModel.objects.get_or_create(cp_number=fcp_number,sne_id=fsne_id,scheme_number=fscheme_number,trs=ftrs)

populate(110)

# print(fcp_number)