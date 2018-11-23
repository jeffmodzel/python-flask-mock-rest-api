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
            return next(filter(lambda x: x['_id'] == id, self._datastore[resource]),None)
        else:
            return None

    def add(self,resource,data):
        data['_id'] = str(uuid.uuid4())
        if resource not in self._datastore:
            self._datastore[resource] = []
        self._datastore[resource].append(data)
        return data

    def remove(self,resource,id):
        x = self.get_one(resource,id)
        if x is not None:
            self._datastore[resource] = list(filter(lambda x: x['_id'] != id, self._datastore[resource]))
            if len(self._datastore[resource]) == 0:
                del self._datastore[resource]
        return x

    def update(self,resource,id,data):
        x = self.get_one(resource,id)
        if x:
            data['_id'] = id
            self.remove(resource,id)
            if resource not in self._datastore:
                self._datastore[resource] = []
            self._datastore[resource].append(data)
            return data
        else:
            return None

    def status(self):
        total = 0
        resources = []
        for k, v in self._datastore.items():
            total += len(v)
            resources.append({'name':k, 'count': len(v)})
        return {'total_resources_count': total, 'resources': resources}
