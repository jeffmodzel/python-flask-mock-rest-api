import uuid

class InMemoryDatabase:

    def __init__(self):
        self._datastore = {}

    def dump(self):
        return self._datastore

    def get_all(self,resource):
        if resource in self._datastore:
            return self._datastore[resource]
        else:
            return None

    def get_one(self,resource,id):
        if resource in self._datastore:
            return next(filter(lambda x: x['id'] == id, self._datastore[resource]),None)
        else:
            return None

    def add(self,resource,data):
        data['id'] = str(uuid.uuid4())
        if resource not in self._datastore:
            self._datastore[resource] = []
        self._datastore[resource].append(data)
        return data

    def remove(self,resource,id):
        x = self.get_one(resource,id)
        if x is not None:
            self._datastore[resource] = list(filter(lambda x: x['id'] != id, self._datastore[resource]))
        return x

    def update(self,resource,id,data):
        x = self.get_one(resource,id)
        if x:
            data['id'] = id
            self.remove(resource,id)
            self._datastore[resource].append(data)
            return data
        else:
            return None

    def status(self):
        total_count = 0
        for k in self._datastore.keys():
            total_count += len(self._datastore[k])
        return {'total_count':total_count}

#
# Dev todo, ideas
#
# lowercase the resource names?
# add prune() function to get rid of empty arrays
# find_by_id(id)
# delete_by_id(id)
# delete all resource  delete('persons')
# merge get_one + get_all (get)
# _id and _resource_name _created_on _last_updated to objects?
# add event notifcation?
