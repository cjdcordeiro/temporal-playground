# temporal-playground
Practicing Temporal Workflows

Ref:
 - <https://docs.temporal.io/concepts>
 - <https://learn.temporal.io/courses/temporal_101>

## Deploy the Temporal Cluster

This will deploy the Temporal Server and databases.

```bash
git clone https://github.com/temporalio/docker-compose.git

(cd docker-compose && docker compose up -d)
```

The Temporal web UI will be at http://127.0.0.1:8080.

## Setting up the environment

This exercise is done in Go, so:

```bash
# clone this repo
git clone https://github.com/cjdcordeiro/temporal-playground

cd temporal-playground

go mod tidy
```

## Check the workflow

The workflow is just an hello-world alike, for demonstration purposes.
There is only one workflow, called `Test`, in `app.go`.

This is what is executed by a Temporal worker, whenever the workflow
is triggered.

## Start the worker

The Temporal worker is defined in `worker/main.go`. This is where
the workflow from above is registered into Temporal. If the workflow
changes, then the worker needs to be restarted.

To start the worker:

```bash
go run worker/main.go
```

And you should see something like:

```
2023/02/15 17:53:34 INFO  No logger configured for temporal client. Created default one.
2023/02/15 17:53:34 INFO  Started Worker Namespace default TaskQueue queue-name WorkerID 183868@foo-laptop@
```

## Execute the workflow

The workflow can either be executed from the code itself, via the Go SDK,
or via `tctl`, is can either be installed or used from within one of the
Temporal administration containers deployed earlier:

```bash
docker exec temporal-admin-tools tctl workflow start --workflow_type Test --taskqueue queue-name --workflow_id test-id-1 --input '"artifact"'
```

There will be no output, as we're not `Get`ting the workflow execution output,
but you can see the execution and output from the UI.
