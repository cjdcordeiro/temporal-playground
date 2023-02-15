package app

import (
            "go.temporal.io/sdk/workflow"
)

func Test(ctx workflow.Context, artifact string) (string, error) {
    // The testing code would go here
    return "Testing " + artifact, nil
}
