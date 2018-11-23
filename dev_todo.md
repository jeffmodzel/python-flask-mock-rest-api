possibly add a query param thing for searching

add health status - status=pass
https://tools.ietf.org/id/draft-inadarei-api-health-check-01.html

add metadata fields for _last_updated _created_on

purge empty resource fields

add better logging

echo the url back in the deploy script

on POST, accept an array of resources



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
