

from faker import Faker

def generate_random_username():
    """File generated based on
        https://github.com/danielmiessler/SecLists/tree/master/Usernames-
        /Names
        https://github.com/danielmiessler/SecLists/blob/master/Usernames-
        /cirt-default-usernames.txt
    
    """
    return Faker().simple_profile()["username"]

def generate_random_ipv4_address():
    return Faker().ipv4()

def generate_random_hostname():
    return Faker().hostname()

def generate_random_port_number():
    return Faker().port_number()