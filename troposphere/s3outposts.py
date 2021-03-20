# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import integer


class VpcConfiguration(AWSProperty):
    props = {
        'VpcId': (basestring, False),
    }


class AccessPoint(AWSObject):
    resource_type = "AWS::S3Outposts::AccessPoint"

    props = {
        'Bucket': (basestring, True),
        'Name': (basestring, True),
        'Policy': (dict, False),
        'VpcConfiguration': (VpcConfiguration, True),
    }


class AbortIncompleteMultipartUpload(AWSProperty):
    props = {
        'DaysAfterInitiation': (integer, True),
    }


class Rule(AWSProperty):
    props = {
        'AbortIncompleteMultipartUpload':
            (AbortIncompleteMultipartUpload, False),
        'ExpirationDate': (basestring, False),
        'ExpirationInDays': (integer, False),
        'Filter': (dict, False),
        'Id': (basestring, False),
        'Status': (basestring, False),
    }


class LifecycleConfiguration(AWSProperty):
    props = {
        'Rules': ([Rule], True),
    }


class Bucket(AWSObject):
    resource_type = "AWS::S3Outposts::Bucket"

    props = {
        'BucketName': (basestring, True),
        'LifecycleConfiguration': (LifecycleConfiguration, False),
        'OutpostId': (basestring, True),
        'Tags': (Tags, False),
    }


class BucketPolicy(AWSObject):
    resource_type = "AWS::S3Outposts::BucketPolicy"

    props = {
        'Bucket': (basestring, True),
        'PolicyDocument': (dict, True),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::S3Outposts::Endpoint"

    props = {
        'OutpostId': (basestring, True),
        'SecurityGroupId': (basestring, True),
        'SubnetId': (basestring, True),
    }