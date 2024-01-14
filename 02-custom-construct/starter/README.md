# Exercise 02 - a custom construct

1. Open the file `02-custom-construct/starter/custom_construct/custom_construct.py` and complete all TODOs.
2. Run `pytest` to check if your code complies
3. Open the file `02-custom-construct/starter/app.py` and complete all TODOs. Subscribe to the SNS topic using [webhook.site](https://webhook.site)
4. Check the synthesized template. Any questions?
5. Deploy the stack.
6. Check your `webhook.site` endpoint, confirm the subscription.
7. Upload a file to your bucket and check if `webhook.site` receives it

```bash
aws s3 cp test.txt s3://<YOUR_BUCKET>/test2.txt
```
