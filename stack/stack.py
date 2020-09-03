from aws_cdk import aws_lambda, aws_stepfunctions, aws_stepfunctions_tasks, core


class SflefsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        func = aws_lambda.Function(
            self,
            "dummy_function",
            code=aws_lambda.InlineCode("""
def handler(event, context):
    print(event)
            """),
            handler="index.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            timeout=core.Duration.seconds(10)
        )

        _ = aws_stepfunctions.StateMachine(
            self,
            "sflefs-step",
            definition=aws_stepfunctions.Chain.start(
                aws_stepfunctions_tasks.LambdaInvoke(
                    self,
                    "invoke-function",
                    lambda_function=func,
                    invocation_type=aws_stepfunctions_tasks.InvocationType.EVENT,
                    payload=aws_stepfunctions.TaskInput.from_object(
                        {
                            'Execution.$': '$$.Execution.Id'
                        }
                    )
                )
            )
        )
