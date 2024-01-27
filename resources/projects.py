import digitalocean as do
import os

from dotenv import load_dotenv
from digitalocean import Project

load_dotenv()


def list_all_projects() -> list[Project]:
    """
    Retrieve a list of all DigitalOcean projects associated with the provided API token.

    Returns:
    list[Project]: A list of DigitalOcean projects, where each project is represented as a Project object.

    Example:
    projects = list_all_projects()
    for project in projects:
        print(f'Project ID: {project.id}, Name: {project.name}, Description: {project.description}')

    Note:
    Ensure that the DigitalOcean API token is set as the 'DIGITAL_OCEAN_TOKEN' environment variable
    before calling this function using the `dotenv` library.
    """
    TOKEN = os.getenv('DIGITAL_OCEAN_TOKEN')

    manager = do.Manager(token=TOKEN)
    projects = manager.get_all_projects()

    return projects


def list_resources_by_project(project_id: str) -> list:
    """
    Retrieve a list of resources associated with a specific DigitalOcean project.

    Args:
    project_id (str): The ID of the DigitalOcean project for which resources are to be listed.

    Returns:
    list: A list of resources associated with the specified project.

    Note:
    Ensure that the DigitalOcean API token is set as the 'DIGITAL_OCEAN_TOKEN' environment variable
    before calling this function using the `dotenv` library.
    """
    TOKEN = os.getenv('DIGITAL_OCEAN_TOKEN')

    manager = do.Manager(token=TOKEN)
    project = manager.get_project(project_id)
    resources = project.get_all_resources()

    return resources
