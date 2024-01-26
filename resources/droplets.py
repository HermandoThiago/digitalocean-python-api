import digitalocean as do
import os

from dotenv import load_dotenv
from digitalocean import Droplet, DropletError

load_dotenv()


def list_all_droplets() -> list[Droplet]:
    """
    Retrieve a list of all DigitalOcean droplets associated with the provided API token.

    Returns:
    list: A list of DigitalOcean droplets, where each droplet is represented as a dictionary.

    Note:
    Ensure that the DigitalOcean API token is set as the 'DIGITAL_OCEAN_TOKEN' environment variable
    using the `dotenv` library before calling this function.
    """
    TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

    manager = do.Manager(token=TOKEN)
    droplets = manager.get_all_droplets()

    return droplets


def create_droplet(request) -> Droplet:
    """
    Create a new DigitalOcean droplet based on the provided request parameters.

    Args:
    request (DropletCreateRequest): An object containing the necessary parameters for creating a droplet.

    Returns:
    Droplet: The newly created DigitalOcean droplet.

    Raises:
    DropletError: If an error occurs during the creation of the droplet.
    """
    try:
        TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

        droplet = do.Droplet(token=TOKEN,
                             name=request.name,
                             region=request.region,
                             image=request.image,
                             size_slug=request.size_slug)
        droplet.create()

        return droplet
    except DropletError as err:
        return err


def destroy_droplet(droplet_id: str) -> None:
    """
    Destroy (delete) a DigitalOcean Droplet.

    Args:
    droplet_id (str): The ID of the droplet to be destroyed.

    Returns:
    None

    Raises:
    DropletError: If an error occurs during the destruction of the droplet.
    """
    try:
        TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

        manager = do.Manager(token=TOKEN)
        droplet = manager.get_droplet(droplet_id)

        droplet.destroy()

    except DropletError as err:
        return err

