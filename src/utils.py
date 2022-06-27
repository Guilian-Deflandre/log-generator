

from faker import Faker

"""This file implement common utilities functions generating fake data used in
   the forged logs based on the Faker Python's library. Data generated are
   usernames, IPv4 addresses, host names, port numbers and session ID.
   See:
    - https://faker.readthedocs.io/en/master/
    - https://github.com/joke2k/faker
"""
def generate_random_username():
    return Faker().user_name()

def generate_random_ipv4_address():
    return Faker().ipv4()

def generate_random_hostname():
    return Faker().hostname()

def generate_random_port_number():
    return Faker().port_number()

def generate_session_id():
    return Faker().sha1()