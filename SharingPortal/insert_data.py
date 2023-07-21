import os
import sys
import uuid
import json
from datetime import datetime
from flask import render_template, flash
#import hashlib

def get_profile_name(id):
    with open("profiles.json","r") as file:
        profiles = json.load(file)
        for i in profiles['profiles']:
            if i["id"]== id:
                return i["Name"]

def get_username(id):
    with open("profiles.json","r") as file:
        profiles = json.load(file)
        for i in profiles['profiles']:
            if i["id"]== id:
                return i["userName"]

def get_id(userName):
    with open("profiles.json","r") as file:
        profiles = json.load(file)
        for i in profiles['profiles']:
            if i["userName"]== userName:
                return i["id"]

def get_info_by_id(id):
    with open("profiles.json","r") as file:
        profiles = json.load(file)
        for i in profiles['profiles']:
            if i["id"]== id:
                del i['Password']
                return i

def get_info_by_userName(userName):
    with open("profiles.json","r") as file:
        profiles = json.load(file)
        for i in profiles['profiles']:
            if i["userName"]== userName:
                del i['Password']
                return i


def check_uuid(uuid_no):
    if uuid is None:
        return None
    
    check_file = os.stat("profiles.json").st_size
    if check_file:
        with open("profiles.json","r") as file:
            profile_Data = json.load(file)
            #checking pre-existance of uuid

            for i in profile_Data['profiles']:
                    if i["id"] == uuid_no:
                        return True
        
            return False
    else:
        return False

def add_profile(Name, Email, Password, prof_id=None):
    is_new = False
    if Name is None:
        flash("Enter Valid Name")
        return render_template("Signup.html")
    if Email is None:
        flash("Enter Valid Email")
        return render_template("Signup.html")
    if len(Password)<8:
        flash("Password must have atleast 8 characters")
        return render_template("Signup.html")
    
    elif prof_id is None:
        is_exist=True
        while is_exist != False:
            prof_id = uuid.uuid4()
            is_exist = check_uuid(prof_id)
        
        is_new=True
        #print("new profile to be add"+ Name +" " +str(prof_id))
                 
    if is_new :
        profile = {
            "id":str(prof_id),
            "Name":Name,
            "userName":Email,
            "Created on":str(datetime.now().strftime("%d-%m-%y %H:%M:%S")),
            "Password":str(Password),
            }
        try:
            with open("profiles.json","r+") as file:
                profiles_Data = json.load(file)
                profiles_Data["profiles"].append(profile)
                file.seek(0)
                json.dump(profiles_Data,file,indent=4)
                file.close()
                flash("Successful Registration")
            return render_template("login.html")
        except:
            flash("Some Error has occured")
            return render_template("Signup.html")

if __name__ == "__main__":
    name = input("Enter Name:")
    print(get_info_by_userName(name))
    #Email = input("\nEnter Email:")
    #Password = input("\nEnter password:")
    #add_profile(name,Email=Email,Password=Password)



    
    
