import string
import random

# Create your utils here.

def generate_invitation_code(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
