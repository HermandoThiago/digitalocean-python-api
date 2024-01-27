# from resources.droplets import create_droplet, list_all_droplets, destroy_droplet
#
# create_droplet_request = {
#     "name": "testando",
#     "region": "nyc1",
#     "image": "ubuntu-20-04-x64",
#     "size_slug": "s-1vcpu-1gb"
# }
#
# droplet = create_droplet(create_droplet_request)
#
# all_droplets = list_all_droplets()
#
# for droplet in all_droplets:
#     print(droplet.id)
#
# destroy_droplet('397865214')
#

from resources.projects import list_all_projects, list_resources_by_project

projects = list_all_projects()

print(projects)

project = list_resources_by_project(projects[0].id)

print(projects[0].id)

print(project)
