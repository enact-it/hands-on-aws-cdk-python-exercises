from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_ecr_assets as ecr_assets,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    CfnOutput,
)
import os
from constructs import Construct


class FinalStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO create a VPC
        ec2.Vpc(self, "VPC", cidr="10.0.0.0/16")

        # TODO create an ECR repository
        ecr.Repository(self, "Repository")

        # TODO create a Docker asset
        asset = ecr_assets.DockerImageAsset(
            self, "Nginx", directory=os.path.join("../files")
        )

        # TODO create an ECS cluster
        cluster = ecs.Cluster(self, "Cluster")

        # TODO create a load balanced fargate service
        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "Service",
            cluster=cluster,
            assign_public_ip=True,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_docker_image_asset(asset)
            ),
            memory_limit_mib=512,
            public_load_balancer=True,
        )

        CfnOutput(
            self, "LoadBalancerDNS", value=service.load_balancer.load_balancer_dns_name
        )
