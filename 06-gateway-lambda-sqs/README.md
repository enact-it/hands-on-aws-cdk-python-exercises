# Lab 06 - API Gateway with Lambda and SQS

1. Create a new CDK app
1. Create an SQS queue
1. Create a `producer` Lambda with a NodeJS runtime. Use the `files/producer` function code. Set an environment `QUEUE_URL` that points to the SQS queue you created before.
1. Grant the `producer` Lambda rights to send messages
1. Add an API gateway (`LambdaRestApi`) and point it to the `producer` Lambda.
1. Add a `consumer` Lambda with a NodeJS runtime. Use the `files/consumer` function code.
1. Add an SQS event source to the `consumer` Lambda with a batch size of 1. Use the library `aws_lambda_event_sources`
1. Grant the `consumer` rights to consume messages.
1. Create a queue URL output
1. Create an API gateway URL output
1. Post data to your endpoint, e.g.:

```bash
curl --request POST \
  --url $API_GATEWAY_URL \
  --header 'Content-Type: application/json' \
  --data '{"body":"test"}'
```

12. Check the logs of the consumer in the console!
