import database

def test_initialization():
    db = database.InMemoryDatabase()

    data = db.get_all(None)
    assert data is None

    data = db.get_all('missing_resource')
    assert data is None

    assert db.status()['total_resources_count'] == 0
    assert len(db.status()['resources']) == 0

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

    # add resources
    for i in range(number_of_resources_to_create):
        x = db.add('dog', {'name' : 'Stella' + str(i)})
        assert x is not None
        assert db.status()['total_resources_count'] == i + 1
        assert len(db.status()['resources']) == 1
        z = list(filter(lambda x: x['name'] == 'dog', db.status()['resources']))
        assert z[0]['count'] == i + 1
        ids_to_delete.append(x['_id'])

    assert db.status()['total_resources_count'] == number_of_resources_to_create
    assert len(db.status()['resources']) == 1
    z = list(filter(lambda x: x['name'] == 'dog', db.status()['resources']))
    assert z[0]['count'] == number_of_resources_to_create

    # remove resources
    expected_resource_count = number_of_resources_to_create
    for id in ids_to_delete:
        x = db.remove('dog',id)
        assert x is not None
        expected_resource_count -= 1
        assert db.status()['total_resources_count'] == expected_resource_count
        if expected_resource_count > 0:
            z = list(filter(lambda x: x['name'] == 'dog', db.status()['resources']))
            assert z[0]['count'] == expected_resource_count

    assert db.status()['total_resources_count'] == 0
    assert len(db.status()['resources']) == 0

def test_database_status():
    db = database.InMemoryDatabase()

    assert db.status()['total_resources_count'] == 0
    assert len(db.status()['resources']) == 0

    dog = {'resource':'dog'}
    cat = {'resource':'cat'}
    weasel = {'resource':'weasel'}

    db.add('dog',dog)
    db.add('dog',dog)
    db.add('dog',dog)
    db.add('cat',cat)
    db.add('cat',cat)
    db.add('weasel',weasel)

    assert db.status()['total_resources_count'] == 6
    assert len(db.status()['resources']) == 3

    resources = db.status()['resources']
    x = list(filter(lambda x: x['name'] == 'dog', resources))
    assert x[0]['count'] == 3
    x = list(filter(lambda x: x['name'] == 'cat', resources))
    assert x[0]['count'] == 2
    x = list(filter(lambda x: x['name'] == 'weasel', resources))
    assert x[0]['count'] == 1
