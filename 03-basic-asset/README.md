# Lab 03 - basic asset

1. Create a new CDK app
2. Add a lambda function, and point it to the `handler` folder
3. Deploy the app
4. List the functions

```bash
aws lambda list-functions
```

5. Invoke the function. Output will be stored in your specified <OUTFILE>

```bash
aws lambda invoke --function-name <FUNCTION_NAME> <OUTFILE>
```

6. Make a change to the handler, deploy it again, and invoke it again.
   ~
