# Exercise 01 - my first Stack - building one from scratch

1. Initialize the app:

```bash
cdk init <YOUR_APP_NAME> --language python
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

9. Tear it down

```bash
cdk destroy
```
