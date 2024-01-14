# My First Stack - building one from scratch

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
