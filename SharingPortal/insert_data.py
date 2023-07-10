import os
import sys
import uuid
from flask import Response

def add_profile(Name, prof_id=None):
    is_new = False
    if Name is None:
        return Response("Enter Valid Name",status=400)
    
    elif prof_id is None:
        prof_id = uuid.uuid4()
        is_new=True

    
    
