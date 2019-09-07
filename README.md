# Webhook script execution

This module provides a simple method for automatically execution calling scripts when a webhook-call is received.

In the configurationfile you define, wich script will be called on wich request. e.g.:

```
[/print/hello]
method: POST
command: echo "Hello!"

[/git/pull/webhook_script_execution]
method: POST
path: /data/scripts/webhook_script_execution
command: git pull
```