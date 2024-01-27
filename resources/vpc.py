import digitalocean as do
import os

from dotenv import load_dotenv

load_dotenv()


def list_all_vpcs() -> list[do.VPC]:
    """
    Retrieve a list of all Virtual Private Clouds (VPCs) associated with the provided DigitalOcean API token.

    Returns:
    list[do.VPC]: A list of DigitalOcean VPCs, where each VPC is represented as a VPC object.

    Example:
    vpcs = list_all_vpcs()
    for vpc in vpcs:
        print(f'VPC ID: {vpc.id}, Name: {vpc.name}, Region: {vpc.region}, Default: {vpc.default}')
    """
    TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

    manager = do.Manager(token=TOKEN)
    vpcs = manager.get_all_vpcs()

    return vpcs


def create_vpc(request) -> do.VPC:
    """
    Create a new Virtual Private Cloud (VPC) in DigitalOcean based on the provided request parameters.

    Args:
    request (dict): A dictionary containing the necessary parameters for creating a VPC.
                    Required keys: 'name', 'description', 'region', 'ip_range'.

    Returns:
    do.VPC: The newly created DigitalOcean VPC.

    Raises:
    Exception: If an error occurs during the creation of the VPC.
    """
    try:
        TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

        vpc = do.VPC(token=TOKEN,
                     name=request['name'],
                     description=request['description'],
                     region=request['region'],
                     ip_range=request['ip_range'])

        vpc.create()

        return vpc

    except Exception as err:
        return err


def delete_vpc(vpc_id: str) -> None:
    """
    Delete (destroy) a Virtual Private Cloud (VPC) in DigitalOcean.

    Args:
    vpc_id (str): The ID of the VPC to be deleted.

    Raises:
    Exception: If an error occurs during the deletion of the VPC.
    """
    try:
        TOKEN = os.getenv("DIGITAL_OCEAN_TOKEN")

        manager = do.Manager(token=TOKEN)
        vpc = manager.get_vpc(vpc_id)

        vpc.destroy()

    except Exception as err:
        return err
