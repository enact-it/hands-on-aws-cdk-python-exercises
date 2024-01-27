# Lab 07 - Kinesis

1. Create a new CDK app.
1. We need an extra library here: `pip install aws-cdk.aws-kinesisfirehose-alpha aws-cdk.aws-kinesisfirehose-destinations-alpha`. Otherwise, we'd have to use "raw" CloudFormation.
1. Create a Kinesis stream with a shard count of 1.
1. Create an S3 bucket. This will be the destination for Kinesis firehose.
1. Create a firehose delivery stream.
1. Set an s3 destination configuration on the destination. Use the following data and error prefixes:

```python
data_output_prefix              = "data/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/"
error_output_prefix = "errors/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/!{firehose:error-output-type}/"
```

7. Set a Kinesis source configuration on the firehose delivery stream.
1. Grant write on the bucket to the firehose delivery stream
1. Grant read on the Kinesis stream to the firehose delivery stream
1. Set an output for the stream name
1. Install the requirements in the `./files/requirements.txt` file (`boto3` and `markovclick`)
1. Set the Kinesis client stream name from the output in the `producer.py` script. Tune some parameters if you want to.
1. Run the `producer.py` script and observe the kinesis goodness!
