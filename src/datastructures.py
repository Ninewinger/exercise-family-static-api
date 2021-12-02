
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = member.get("id", None)
        if member["first_name"] is None or member["age"] is None or member["lucky_numbers"] is None:
            return "You must include 'first_name', 'age' and 'lucky_numbers'", 400

        elif type(member["lucky_numbers"]) is not list:
            return "'lucky_numbers' must be a list of numbers", 400

        elif member["id"] is not None and self.get_member(member["id"])[1] == 200:
            return f"member with id {member['id']} already exists", 400

        else:
            try:
                formattedMember = {
                    "id": member["id"] or self._generateId(),
                    "first_name": member["first_name"],
                    "last_name": self.last_name,
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
                self._members.append(formattedMember)
                # fill this method and update the return
                return formattedMember, 200

            except:
                return "Internal error", 500

    def delete_member(self, id):
        # fill this method and update the return
        try:
            for position in range(len(self._members)):
                if self._members[position]["id"] == id:
                    nombre = self._members[position]["first_name"]
                    self._members.pop(position)
                    return f"Member with id {id}, and first name {nombre}, deleted", 200

            return f"Member with id {id} not found, you must include a valid id", 404

        except:
            return "Internal error", 500

    def get_member(self, id):
        # fill this method and update the return
        try:
            for member in self._members:
                if member["id"] == int(id):
                    return member, 200

            return f"Member with id {id} not found, you must include a valid id", 404
        except:
            return "Internal error", 500

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        try:
            if type(self._members) is list:
                return self._members, 200
            else:
                return "Bad request", 400
        except:
            return "Internal error", 500
