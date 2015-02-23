from models import Voucher, Campaign
import string
import random

def link_generator(campaign):
    char_list = string.ascii_letters + string.digits
    for i in range(campaign.count):
        while (True):
            new_char_url = ''.join(random.choice(char_list) for j in range(12))
            try:
                Voucher.objects.get(char_url=new_char_url)
            except:
                v = Voucher(campaign=campaign,char_url=new_char_url)
                v.save()
                break
