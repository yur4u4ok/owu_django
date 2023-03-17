import json
from rest_framework.response import Response
from rest_framework.views import APIView

import random


class UsersAPIViewGetPost(APIView):

    @staticmethod
    def get(self, *args, **kwargs):
        try:
            with open("users/users.json") as file:
                return Response(json.load(file))
        except Exception as err:
            print(err)

    def post(self, *args, **kwargs):
        data = self.request.data

        def get_id(length):
            return random.randint(1, length + 1)

        with open("users/users.json", 'r') as readFile:
            arr_users = json.load(readFile)
            users_id = []

            for user in arr_users:
                users_id.append(user['id'])

            while True:
                id = get_id(len(arr_users))
                if id not in users_id:
                    data['id'] = id
                    break

            arr_users.append(data)

            with open("users/users.json", 'w') as writeFile:
                json.dump(arr_users, writeFile)

        return Response(data)


class UserGetPutDelete(APIView):

    @staticmethod
    def get(self, *args, **kwargs):
        with open("users/users.json") as readFile:
            for user in json.load(readFile):
                if user['id'] == kwargs['pk']:
                    return Response(user)
        return Response("not found user")

    def put(self, *args, **kwargs):
        data = self.request.data
        update_user = False

        users = []

        with open("users/users.json") as readFile:
            for user in json.load(readFile):
                users.append(user)

        for user in users:
            if user['id'] == kwargs['pk']:
                users[users.index(user)]['name'] = data['name']
                users[users.index(user)]['age'] = data['age']
                update_user = True

        with open("users/users.json", 'w') as writeFile:
            json.dump(users, writeFile)

        if update_user:
            return Response(data)
        else:
            return Response("Not Found User with that ID")

    @staticmethod
    def delete(self, *args, **kwargs):
        delete_user = {}
        delete = False

        users = []

        with open("users/users.json") as readFile:
            for user in json.load(readFile):
                users.append(user)

        for user in users:
            if user['id'] == kwargs['pk']:
                users.remove(user)
                delete_user = user
                delete = True

        with open("users/users.json", 'w') as writeFile:
            json.dump(users, writeFile)

        if delete:
            return Response(delete_user)
        else:
            return Response("Not Found User with that ID")
