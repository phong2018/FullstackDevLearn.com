import os
import boto3
from dotenv import load_dotenv
from Common import saveData, getData

data = getData()


# ====================
def createClientSession():
    # config credentials from .env file
    load_dotenv()
    AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
    REGION_NAME = os.environ.get("REGION_NAME")

    # or config credentials directly
    # AWS_ACCESS_KEY = xxxxxxxxxxxxxxxx
    # AWS_SECRET_KEY = yyyyyyyyyyyyyyyy
    # REGION_NAME    = zzzzzzzzzzzzzzzz

    # create session with the credentials
    session = boto3.Session(
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"),
        region_name=os.environ.get("REGION_NAME"),
    )
    ec2Client = session.client("ec2")

    return ec2Client


# ====================
def createVpc(ec2):
    # create the VPC
    vpc_name = "Your Vpc Name"
    response = ec2.create_vpc(
        CidrBlock="10.0.0.0/16",
        AmazonProvidedIpv6CidrBlock=True,
        InstanceTenancy="default",
        TagSpecifications=[
            {
                "ResourceType": "vpc",
                "Tags": [
                    {"Key": "Name", "Value": vpc_name},
                ],
            },
        ],
    )

    print("################\ncreate_vpc", response)

    # get the ID of the new VPC
    data["vpcId"] = response["Vpc"]["VpcId"]
    print("Created VPC with ID:", data["vpcId"])
    saveData(data)


# ====================
def deleteVpc(ec2):
    # delete the VPC
    data = getData()
    response = ec2.delete_vpc(VpcId=data["vpcId"]) 
    print("################\ndelete_vpc", response)


#####################
if __name__ == "__main__":
    ec2Client = createClientSession()
    createVpc(ec2Client)
    # deleteVpc(ec2Client)
