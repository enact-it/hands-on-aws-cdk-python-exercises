# Exercise 01 - my first stack - initializing a new stack

1. Initialize the app:

```bash
cdk init sample-app --language python
```

2. Activate the virtual environment

```bash
source .venv/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. Check out the CloudFormation template

```bash
cdk synth
```

5. Run a test to make sure we're golden!

```bash
pytest
```

6. Check out the stacks we're deploying

```bash
cdk ls
```

7. Check the diff

```bash
cdk diff
```

8. Try to deploy the stack!

```bash
cdk deploy
```

9. Find the SNS topic, and post a message to it (you can also do this in the console)

```bash
aws sns list-topics
aws sns publish --topic-arn <YOUR_TOPIC> --message "hi"
```

10. Find the SQS queue, and poll for messages (you can also do this in the console)

```bash
aws sqs list-queues
aws sqs receive-message --queue-url <YOUR_QUEUE_URL>
```

11. Tear everything down

```bash
cdk destroy
```
