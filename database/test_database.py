import database

def test_database():
    db = database.InMemoryDatabase()
    data = db.get_all('missing_resource')
    assert data is None
    data = db.get_all(None)
    assert data is None
    assert db.status()['total_count'] == 0

def test_basic_crud():
    db = database.InMemoryDatabase()

    # test data
    id = None
    name = 'Stella'
    new_field = 'some new data'
    dog = {'name' : name}

    # add a new resource
    added_resource = db.add('dog',dog)
    assert '_id' in added_resource

    id = added_resource['_id']

    # get added resource
    get_resource = db.get_one('dog',id)
    assert get_resource is not None
    assert get_resource['_id'] == id
    assert get_resource['name'] == name

    # update resource with new field
    get_resource['new_field'] = new_field
    updated_resource = db.update('dog',id,get_resource)
    assert updated_resource is not None
    assert updated_resource['_id'] == id
    assert updated_resource['name'] == name
    assert updated_resource['new_field'] == new_field

    # update resource with new field removed
    del updated_resource['new_field']
    updated_resource = db.update('dog',id,updated_resource)
    assert updated_resource is not None
    assert updated_resource['_id'] == id
    assert updated_resource['name'] == name
    assert 'new_field' not in updated_resource

    # remove resource
    deleted_resource = db.remove('dog',id)
    assert deleted_resource is not None
    assert deleted_resource['_id'] == id
    assert deleted_resource['name'] == name
    assert 'new_field' not in deleted_resource

    # get deleted resource
    missing_resource = db.get_one('dog',id)
    assert missing_resource is None

def test_edge_cases():
    db = database.InMemoryDatabase()

    # test data
    name = 'Stella'
    dog = {'name' : name}

    added_resource = db.add('dog',dog)

    get_bad_resource = db.get_one('dog','123_bogus_id')
    assert get_bad_resource is None

    get_bad_resource = db.get_one('cat','1234567890')
    assert get_bad_resource is None

def test_load():
    # create 1000 objects, delete them all
    number_of_resources_to_create = 1000
    ids_to_delete = []

    db = database.InMemoryDatabase()

    for i in range(number_of_resources_to_create):
        x = db.add('dog', {'name' : 'Stella' + str(i)})
        assert x is not None
        ids_to_delete.append(x['_id'])

    assert db.status()['total_count'] == number_of_resources_to_create

    for id in ids_to_delete:
        x = db.remove('dog',id)
        assert x is not None

    assert db.status()['total_count'] == 0
